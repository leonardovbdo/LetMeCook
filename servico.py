from flask import Flask, jsonify
from robo import *

servico = Flask("ifbabot")

configurado, robo = configurar()

@servico.get("/ifba/info")
def get_informacoes():
    return jsonify(
        descricao = "Robô de Atendimento do IFBA, Vitória da Conquista",
        email = "luispscarvalho@gmail.com",
        versao = "1.0",
        robo_online = configurado
    )

@servico.get("/ifba/resposta/<string:mensagem>")
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem)

    return jsonify(
        resposta = resposta.text,
        confianca = resposta.confidence
    )

if __name__ == "__main__":
    servico.run(debug=True)