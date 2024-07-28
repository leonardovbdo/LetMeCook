from flask import Flask, jsonify
from flask_cors import CORS
from bot import configurar_bot

app = Flask(__name__)
CORS(app)

configurado, bot = configurar_bot()

# Rota que retorna informações sobre o chatbot
@app.route("/letmecook/info", methods=['GET'])
def get_informacoes():
    return jsonify(
        descricao="LetMeCook, qual sua dúvida gastronômica hoje?",
        email="leonardovbdo25@gmail.com",
        versao="1.0",
        robo_online=configurado
    )

# Rota que recebe uma mensagem do usuário e retorna uma resposta do chatbot
@app.route("/letmecook/response/<string:message>", methods=['GET'])
def get_resposta(message):
    try:
        response = bot.get_response(message)
        return jsonify(
            response=response.text,
            confianca=response.confidence
        )
    except Exception as e:
        return jsonify(
            error=str(e)
        ), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
