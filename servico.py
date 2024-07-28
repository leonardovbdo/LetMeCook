from flask import Flask, jsonify
from flask_cors import CORS  # Importar CORS
from robo import configurar

app = Flask(__name__)
CORS(app)  # Ativar CORS

configurado, robo = configurar()

@app.route("/letmecook/info", methods=['GET'])
def get_informacoes():
    return jsonify(
        descricao="LetMeCook, qual sua dúvida gastronômica hoje?",
        email="leonardovbdo25@gmail.com",
        versao="1.0",
        robo_online=configurado
    )

@app.route("/letmecook/response/<string:message>", methods=['GET'])
def get_resposta(message):
    try:
        response = robo.get_response(message)
        return jsonify(
            response=response.text,
            confianca=response.confidence
        )
    except Exception as e:
        return jsonify(
            error=str(e)
        ), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Certifique-se de que a porta está correta
