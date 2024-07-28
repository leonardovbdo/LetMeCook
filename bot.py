from chatterbot import ChatBot
import time

CONFIANCA_MINIMA = 0.55

def configurar():
    time.clock = time.time

    bot = ChatBot("LetMeCook", read_only = True, logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}])

    return True, bot

def executar(bot):
    while True:
        mensagem = input("digite alguma coisa...\n")
        resposta = bot.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(f"LetMeCook >> {resposta.text} [confiança={resposta.confidence}]")
        else:
            print(f"infelizmente, eu não sei responder essa pergunta [confiança={resposta.confidence}, resposta={resposta.text}]")
            print("pergunte outra coisa")

if __name__ == "__main__": 
    configurado, bot = configurar()

    if configurado:
        executar(bot)