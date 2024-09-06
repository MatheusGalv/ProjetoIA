from nlp_pipeline import analyze_text, detect_intent

def process_input(user_input):
    # Usa o pipeline NLP para analisar o texto
    analysis = analyze_text(user_input)
    intent = detect_intent(user_input)
    
    if intent == "greeting":
        return "Olá! Como posso te ajudar hoje?"
    elif intent == "calculation":
        return "Parece que você quer fazer um cálculo. Como posso te ajudar com isso?"
    elif intent == "time_query":
        return "Você quer saber a hora ou a data? Agora são 14:00."
    
    # Entidades reconhecidas
    if analysis["entities"]:
        return f"Entidades reconhecidas: {analysis['entities']}"
    
    return "Ainda estou aprendendo. Pode perguntar outra coisa?"

