from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import json

CONVERSAS = [
    "topics/saudacoes.json",
    "topics/informacoes_basicas.json",
    "topics/cook_tips.json"
]

def configurar():
    time.clock = time.time
    treinador = ListTrainer(ChatBot("LetMeCook"))

    return True, treinador


def carregar_conversas():
    carregadas, conversas = True, []

    for arquivo_de_conversas in CONVERSAS:
        try:
            with open(arquivo_de_conversas, "r", encoding="utf-8") as arquivo:
                para_treinar = json.load(arquivo)
                conversas.append(para_treinar["conversas"])

                arquivo.close()
        except Exception as e:
            carregadas = False

    return carregadas, conversas

def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]

            print(f"treinando o robô, mensagens: {mensagens}, resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])

if __name__ == "__main__":
    configurado, treinador = configurar()

    if configurado:
        carregadas, conversas = carregar_conversas()
        if carregadas:
            treinar(treinador, conversas)