def analyze_text(text: str):
    # Placeholder: simple heuristic
    label = "romantic-calm" if any(w in text.lower() for w in ["love","عاشق","آروم","calm"]) else "energetic"
    intensity = 70 if label == "energetic" else 40
    suggested = [
        {"id": 1, "title": "Mock Track 1", "artist": "AI DJ"},
        {"id": 2, "title": "Mock Track 2", "artist": "AI DJ"},
    ]
    return label, intensity, suggested
