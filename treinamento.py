from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import json

CONVERSAS = [
    "topics/saudacoes.json",
    "topics/informacoes_basicas.json",
    "topics/cook_tips.json"
]

def configurar_bot():
    """
    Configura o chatbot LetMeCook.
    """
    time.clock = time.time
    bot = ChatBot("LetMeCook")
    treinador = ListTrainer(bot)
    return True, treinador

def carregar_conversas():
    """
    Carrega as conversas dos arquivos JSON especificados em CONVERSAS.
    """
    conversas = []
    try:
        for arquivo_de_conversas in CONVERSAS:
            with open(arquivo_de_conversas, "r", encoding="utf-8") as arquivo:
                para_treinar = json.load(arquivo)
                conversas.extend(para_treinar["conversas"])
        return True, conversas
    except Exception as e:
        print(f"Erro ao carregar conversas: {e}")
        return False, []

def treinar(treinador, conversas):
    """
    Treina o chatbot com as conversas fornecidas.
    """
    for conversa in conversas:
        mensagens = conversa["mensagens"]
        resposta = conversa["resposta"]
        print(f"Treinando o robô, mensagens: {mensagens}, resposta: {resposta}")
        for mensagem in mensagens:
            treinador.train([mensagem, resposta])

if __name__ == "__main__":
    configurado, treinador = configurar_bot()
    if configurado:
        carregadas, conversas = carregar_conversas()
        if carregadas:
            treinar(treinador, conversas)
