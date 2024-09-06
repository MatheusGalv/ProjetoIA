import spacy

# Carrega o modelo de linguagem em português
nlp = spacy.load('pt_core_news_sm')

def analyze_text(text):
    doc = nlp(text)
    
    # Extrai entidades e categorias de palavras (POS tags)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    tokens = [token.text for token in doc]
    lemmas = [token.lemma_ for token in doc]
    pos_tags = [token.pos_ for token in doc]

    return {
        "entities": entities,
        "tokens": tokens,
        "lemmas": lemmas,
        "pos_tags": pos_tags
    }

def detect_intent(text):
    doc = nlp(text)
    
    # Simples detecção de intenção baseada em palavras-chave
    if any(token.lemma_ in ["somar", "adicionar", "+", "mais"] for token in doc):
        return "calculation"
    elif any(token.lemma_ in ["hora", "data", "hoje"] for token in doc):
        return "time_query"
    elif any(token.lemma_ in ["oi", "olá", "tudo", "bem"] for token in doc):
        return "greeting"
    else:
        return "unknown"
