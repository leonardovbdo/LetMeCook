from chatterbot import ChatBot
import time

CONFIANCA_MINIMA = 0.55

def configurar():
    time.clock = time.time

    robo = ChatBot("LetMeCook", read_only = True, logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}])

    return True, robo

def executar(robo):
    while True:
        mensagem = input("digite alguma coisa...\n")
        resposta = robo.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(f"LetMeCook >> {resposta.text} [confiança={resposta.confidence}]")
        else:
            print(f"infelizmente, eu não sei responder essa pergunta [confiança={resposta.confidence}, resposta={resposta.text}]")
            print("pergunte outra coisa")

if __name__ == "__main__": 
    configurado, robo = configurar()

    if configurado:
        executar(robo)