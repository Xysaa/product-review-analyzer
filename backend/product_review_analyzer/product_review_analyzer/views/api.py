import json
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest, HTTPInternalServerError

from ..models import Review
from ..services.sentiment import analyze_sentiment
from ..services.gemini import extract_key_points


def _json_body(request):
    try:
        data = request.json_body
        if not isinstance(data, dict):
            raise ValueError
        return data
    except Exception:
        raise HTTPBadRequest(json_body={"error": "Invalid JSON body"})


@view_config(route_name="analyze_review", request_method="OPTIONS", renderer="json")
def analyze_review_options(request):
    return {"ok": True}


@view_config(route_name="get_reviews", request_method="OPTIONS", renderer="json")
def get_reviews_options(request):
    return {"ok": True}


@view_config(route_name="analyze_review", request_method="POST", renderer="json")
def analyze_review(request):
    data = _json_body(request)
    review_text = (data.get("review_text") or "").strip()
    if len(review_text) < 5:
        raise HTTPBadRequest(json_body={"error": "review_text is required (min 5 chars)"})

    settings = request.registry.settings

    gemini_key = settings.get("gemini.api_key")
    if not gemini_key:
        raise HTTPInternalServerError(json_body={"error": "Gemini API key not configured"})

    hf_token = settings.get("hf.api_token")
    hf_model_id = settings.get(
        "hf.model_id",
        "cardiffnlp/twitter-roberta-base-sentiment-latest"
    )
    if not hf_token:
        raise HTTPInternalServerError(json_body={"error": "Hugging Face API token not configured"})

    try:
        # Sentiment via HF Inference API (no model download)
        hf_model = settings.get("hf.model_name", "distilbert-base-uncased-finetuned-sst-2-english")
        sentiment, score = analyze_sentiment(review_text, hf_model)


        # Key points via Gemini
        key_points = extract_key_points(review_text, gemini_key)

        # Save to DB
        row = Review(
            review_text=review_text,
            sentiment=sentiment,
            sentiment_score=score,
            key_points=json.dumps(key_points, ensure_ascii=False),
        )
        request.dbsession.add(row)
        request.dbsession.flush()
        request.dbsession.commit()


        return {
            "id": row.id,
            "review_text": row.review_text,
            "sentiment": row.sentiment,
            "sentiment_score": row.sentiment_score,
            "key_points": key_points,
            "created_at": row.created_at.isoformat() if row.created_at else None,
        }

    except HTTPBadRequest:
        raise
    except Exception as e:
        request.dbsession.rollback()
        raise HTTPInternalServerError(json_body={"error": "Analysis failed", "detail": str(e)})


@view_config(route_name="get_reviews", request_method="GET", renderer="json")
def get_reviews(request):
    rows = request.dbsession.query(Review).order_by(Review.id.desc()).all()

    items = []
    for r in rows:
        try:
            kp = json.loads(r.key_points)
        except Exception:
            kp = {"pros": [], "cons": [], "summary": ""}

        items.append({
            "id": r.id,
            "review_text": r.review_text,
            "sentiment": r.sentiment,
            "sentiment_score": r.sentiment_score,
            "key_points": kp,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        })

    return {"items": items}
