from transformers import pipeline

_PIPE = None

def get_pipe(model_name: str):
    global _PIPE
    if _PIPE is None:
        _PIPE = pipeline("sentiment-analysis", model=model_name)
    return _PIPE

def analyze_sentiment(text: str, model_name: str):
    pipe = get_pipe(model_name)
    out = pipe(text[:2000])[0]
    label = (out.get("label") or "").upper()
    score = float(out.get("score") or 0.0)

    if label == "POSITIVE":
        return ("positive", score)
    if label == "NEGATIVE":
        return ("negative", score)
    return ("neutral", score)
