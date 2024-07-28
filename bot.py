from chatterbot import ChatBot
import time

CONFIANCA_MINIMA = 0.55

def configurar_bot():
    """Configura e retorna o chatbot LetMeCook."""
    time.clock = time.time

    bot = ChatBot(
        "LetMeCook",
        read_only=True,
        logic_adapters=[
            {"import_path": "chatterbot.logic.BestMatch"}
        ]
    )
    return bot

def executar_bot(bot):
    """Executa o chatbot, processando entradas do usuário e fornecendo respostas."""
    while True:
        mensagem = input("Digite alguma coisa...\n").lower()
        resposta = bot.get_response(mensagem)
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(f"LetMeCook >> {resposta.text} [confiança={resposta.confidence:.2f}]")
        else:
            print(f"Infelizmente, eu não sei responder essa pergunta [confiança={resposta.confidence:.2f}, resposta={resposta.text}]")
            print("Pergunte outra coisa.")

if __name__ == "__main__":
    bot = configurar_bot()
    executar_bot(bot)
