import unittest
from app import app  # Importe o aplicativo Flask
from flask import jsonify

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configura o ambiente de teste
        cls.app = app
        cls.client = cls.app.test_client()
        cls.app.testing = True

    def setUp(self):
        # Configura o contexto para cada teste
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Limpa o contexto após cada teste
        self.app_context.pop()

    def test_info_endpoint(self):
        # Testa o endpoint /letmecook/info
        response = self.client.get('/letmecook/info')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'LetMeCook, qual sua dúvida gastronômica hoje?', response.data)

    def test_response_endpoint(self):
        # Testa o endpoint /letmecook/response/{message}
        response = self.client.get('/letmecook/response/Como fazer um bolo?')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('response', data)
        self.assertIn('confianca', data)

    @classmethod
    def tearDownClass(cls):
        # Limpeza após todos os testes (se necessário)
        pass


class TestChatbotResponses(BaseTestCase):
    def setUp(self):
        super().setUp()
        # Defina as perguntas e respostas esperadas
        self.test_data = [
            {
                "mensagens": ["oi", "olá", "tudo bem?", "como vai?"],
                "resposta": "Olá, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"
            },
            {
                "mensagens": ["bom dia"],
                "resposta": "Bom dia, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"
            },
            {
                "mensagens": ["boa tarde"],
                "resposta": "Boa tarde, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"
            },
            {
                "mensagens": ["boa noite"],
                "resposta": "Boa noite, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"
            },
            {
                "mensagens": ["O que você faz?", "Qual é a sua função?", "Para que você serve?"],
                "resposta": "Eu sou o LetMeCook, um assistente virtual especializado em culinária e gastronomia. Estou aqui para responder suas dúvidas sobre receitas, técnicas de cozinha e dicas culinárias."
            },
            {
                "mensagens": ["Como fazer creme de confeiteiro?", "Como preparar creme de confeiteiro?", "Qual a receita de creme de confeiteiro?"],
                "resposta": "Para fazer creme de confeiteiro, você vai precisar de leite, açúcar, gemas de ovo, amido de milho e essência de baunilha. Primeiro, aqueça o leite com a essência de baunilha. Em uma tigela, misture as gemas e o açúcar, depois adicione o amido de milho. Despeje o leite quente lentamente na mistura de gemas, mexendo constantemente. Volte a mistura para a panela e cozinhe até engrossar."
            }
        ]

    def test_chatbot_responses(self):
        for item in self.test_data:
            for mensagem in item["mensagens"]:
                with self.subTest(mensagem=mensagem):
                    response = self.client.get(f'/letmecook/response/{mensagem}')
                    self.assertEqual(response.status_code, 200)
                    data = response.get_json()
                    self.assertEqual(data['response'], item["resposta"])

if __name__ == "__main__":
    unittest.main()
