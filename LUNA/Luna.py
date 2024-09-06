from Processor import process_input
from database import log_conversation

def main():
    print("Olá, eu sou a Luna. Como posso ajudar?")
    
    while True:
        user_input = input("Você: ")
        
        if user_input.lower() in ["sair", "exit"]:
            print("Luna: Até mais!")
            break
        
        # Processa a entrada do usuário e gera uma resposta
        response = process_input(user_input)
        
        # Exibe a resposta da Luna
        print(f"Luna: {response}")
        
        # Salva a conversa no banco de dados
        log_conversation(user_input, response)

if __name__ == "__main__":
    main()
