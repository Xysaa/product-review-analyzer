import json
import google.generativeai as genai

def _pick_model():
    # Prefer model yang umum tersedia
    preferred = [
        "gemini-1.5-flash-latest",
        "gemini-1.5-flash-8b",
        "gemini-1.5-pro-latest",
        "gemini-pro",
    ]

    models = list(genai.list_models())
    names = [m.name for m in models]  # e.g. "models/gemini-pro"

    # cari preferred yang ada dan support generateContent
    for want in preferred:
        full = f"models/{want}"
        for m in models:
            if m.name == full and "generateContent" in (m.supported_generation_methods or []):
                return want

    # fallback: model pertama yang support generateContent
    for m in models:
        if "generateContent" in (m.supported_generation_methods or []):
            # m.name format "models/xxxx"
            return m.name.replace("models/", "")

    raise RuntimeError("No Gemini model available that supports generateContent")

def extract_key_points(review_text: str, api_key: str):
    genai.configure(api_key=api_key)
    model_name = _pick_model()
    model = genai.GenerativeModel(model_name)

    prompt = f"""
Return ONLY valid JSON with schema:
{{
  "pros": ["..."],
  "cons": ["..."],
  "summary": "one short sentence"
}}
Review:
{review_text}
"""

    resp = model.generate_content(prompt)
    text = (resp.text or "").strip()

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"Gemini did not return valid JSON (model={model_name})")

    data = json.loads(text[start:end+1])
    if not isinstance(data, dict):
        raise ValueError(f"Invalid JSON structure (model={model_name})")

    data.setdefault("pros", [])
    data.setdefault("cons", [])
    data.setdefault("summary", "")
    return data
