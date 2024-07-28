from flask import Flask, jsonify
from robo import *

servico = Flask("letmecook")

configurado, robo = configurar()

@servico.get("/letmecook/info")
def get_informacoes():
    return jsonify(
        descricao = "LetMeCook, qual sua dúvida gastronômica hoje?",
        email = "leonardovbdo25@gmail.com",
        versao = "1.0",
        robo_online = configurado
    )

@servico.get("/letmecook/response/<string:message>")
def get_resposta(message):
    response = robo.get_response(message)

    return jsonify(
        response = response.text,
        confianca = response.confidence
    )

if __name__ == "__main__":
    servico.run(debug=True)