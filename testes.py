import unittest
from bot import configurar, CONFIANCA_MINIMA

class TesteBot(unittest.TestCase):
    def setUp(self):
        """Configura o bot antes de cada teste."""
        self.configurado, self.bot = configurar()

    def verificar_configuracao(self):
        """Verifica se o bot está corretamente configurado."""
        self.assertTrue(self.configurado)

    def verificar_resposta(self, mensagem, resposta_esperada):
        """Verifica se o bot responde corretamente com confiança adequada."""
        resposta = self.bot.get_response(mensagem)
        self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
        self.assertIn(resposta_esperada, resposta.text)

    def teste_saudacoes(self):
        """Testa saudações básicas e suas variabilidades."""
        saudacoes = [
            ("oi", "Olá, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("olá", "Olá, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("tudo bem?", "Olá, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("como vai?", "Olá, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("oi, tudo bem?", "Olá, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("olá, tudo bem?", "Olá, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("como vai, tudo bem?", "Olá, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("bom dia", "Bom dia, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("boa tarde", "Boa tarde, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?"),
            ("boa noite", "Boa noite, sou o LetMeCook, seu assistente de culinária. Como posso te ajudar hoje?")
        ]

        for saudacao, resposta_esperada in saudacoes:
            with self.subTest(mensagem=saudacao):
                self.verificar_resposta(saudacao, resposta_esperada)

    def teste_informacoes_culinarias(self):
        """Testa informações culinárias e suas variações."""
        informacoes = [
            ("Como fazer creme de confeiteiro?", 
             "Para fazer creme de confeiteiro, você vai precisar de leite, açúcar, gemas de ovo, amido de milho e essência de baunilha. Primeiro, aqueça o leite com a essência de baunilha. Em uma tigela, misture as gemas e o açúcar, depois adicione o amido de milho. Despeje o leite quente lentamente na mistura de gemas, mexendo constantemente. Volte a mistura para a panela e cozinhe até engrossar."),
            ("Qual a receita de creme de confeiteiro?",
             "Para fazer creme de confeiteiro, você vai precisar de leite, açúcar, gemas de ovo, amido de milho e essência de baunilha. Primeiro, aqueça o leite com a essência de baunilha. Em uma tigela, misture as gemas e o açúcar, depois adicione o amido de milho. Despeje o leite quente lentamente na mistura de gemas, mexendo constantemente. Volte a mistura para a panela e cozinhe até engrossar."),
            ("Como preparar creme de confeiteiro?",
             "Para fazer creme de confeiteiro, você vai precisar de leite, açúcar, gemas de ovo, amido de milho e essência de baunilha. Primeiro, aqueça o leite com a essência de baunilha. Em uma tigela, misture as gemas e o açúcar, depois adicione o amido de milho. Despeje o leite quente lentamente na mistura de gemas, mexendo constantemente. Volte a mistura para a panela e cozinhe até engrossar."),
            ("Quais são os diferentes tipos de cortes de legumes?",
             "Os diferentes tipos de cortes de legumes incluem: julienne (tiras finas), brunoise (cubos pequenos), chiffonade (tirinhas finas, geralmente de folhas), batonnets (tiras mais grossas), e rondelle (rodelas). Cada tipo de corte tem uma aplicação específica em receitas e apresentações."),
            ("Tipos de cortes de legumes?",
             "Os diferentes tipos de cortes de legumes incluem: julienne (tiras finas), brunoise (cubos pequenos), chiffonade (tirinhas finas, geralmente de folhas), batonnets (tiras mais grossas), e rondelle (rodelas). Cada tipo de corte tem uma aplicação específica em receitas e apresentações."),
            ("Pode me dizer os tipos de cortes de legumes?",
             "Os diferentes tipos de cortes de legumes incluem: julienne (tiras finas), brunoise (cubos pequenos), chiffonade (tirinhas finas, geralmente de folhas), batonnets (tiras mais grossas), e rondelle (rodelas). Cada tipo de corte tem uma aplicação específica em receitas e apresentações."),
            ("Quais cortes de legumes existem?",
             "Os diferentes tipos de cortes de legumes incluem: julienne (tiras finas), brunoise (cubos pequenos), chiffonade (tirinhas finas, geralmente de folhas), batonnets (tiras mais grossas), e rondelle (rodelas). Cada tipo de corte tem uma aplicação específica em receitas e apresentações."),
            ("Qual a diferença entre cozinhar e assar?", 
             "Cozinhar geralmente se refere ao processo de preparar alimentos usando calor, e pode incluir métodos como fervura, cozimento a vapor ou fritura. Assar, por outro lado, é o processo de cozinhar alimentos no forno, utilizando calor seco, que geralmente resulta em uma crosta dourada e crocante."),
            ("Diferença entre cozinhar e assar?", 
             "Cozinhar geralmente se refere ao processo de preparar alimentos usando calor, e pode incluir métodos como fervura, cozimento a vapor ou fritura. Assar, por outro lado, é o processo de cozinhar alimentos no forno, utilizando calor seco, que geralmente resulta em uma crosta dourada e crocante."),
            ("Qual a distinção entre cozinhar e assar?", 
             "Cozinhar geralmente se refere ao processo de preparar alimentos usando calor, e pode incluir métodos como fervura, cozimento a vapor ou fritura. Assar, por outro lado, é o processo de cozinhar alimentos no forno, utilizando calor seco, que geralmente resulta em uma crosta dourada e crocante."),
            ("Qual é a melhor maneira de temperar um bife?", 
             "A melhor maneira de temperar um bife é usar sal e pimenta como base. Polvilhe sal grosso e pimenta-do-reino moída na hora em ambos os lados do bife. Você também pode adicionar alho, ervas como alecrim ou tomilho, e um fio de azeite para realçar o sabor. Deixe o bife descansar por alguns minutos antes de cozinhar."),
            ("Como temperar um bife?", 
             "A melhor maneira de temperar um bife é usar sal e pimenta como base. Polvilhe sal grosso e pimenta-do-reino moída na hora em ambos os lados do bife. Você também pode adicionar alho, ervas como alecrim ou tomilho, e um fio de azeite para realçar o sabor. Deixe o bife descansar por alguns minutos antes de cozinhar."),
            ("Qual o melhor jeito de temperar um bife?", 
             "A melhor maneira de temperar um bife é usar sal e pimenta como base. Polvilhe sal grosso e pimenta-do-reino moída na hora em ambos os lados do bife. Você também pode adicionar alho, ervas como alecrim ou tomilho, e um fio de azeite para realçar o sabor. Deixe o bife descansar por alguns minutos antes de cozinhar."),
            ("Pode me ensinar a temperar um bife?", 
             "A melhor maneira de temperar um bife é usar sal e pimenta como base. Polvilhe sal grosso e pimenta-do-reino moída na hora em ambos os lados do bife. Você também pode adicionar alho, ervas como alecrim ou tomilho, e um fio de azeite para realçar o sabor. Deixe o bife descansar por alguns minutos antes de cozinhar."),
            ("Como fazer uma lasanha tradicional italiana?", 
             "Para fazer uma lasanha tradicional italiana, você vai precisar de massa de lasanha, molho à bolonhesa, molho bechamel, queijo parmesão e mussarela. Monte a lasanha alternando camadas de massa, molho à bolonhesa, molho bechamel e queijo. Termine com uma camada de molho bechamel e bastante queijo parmesão. Asse em forno pré-aquecido até dourar e borbulhar."),
            ("Receita de lasanha tradicional italiana?", 
             "Para fazer uma lasanha tradicional italiana, você vai precisar de massa de lasanha, molho à bolonhesa, molho bechamel, queijo parmesão e mussarela. Monte a lasanha alternando camadas de massa, molho à bolonhesa, molho bechamel e queijo. Termine com uma camada de molho bechamel e bastante queijo parmesão. Asse em forno pré-aquecido até dourar e borbulhar."),
            ("Pode me ensinar a fazer uma lasanha italiana?", 
             "Para fazer uma lasanha tradicional italiana, você vai precisar de massa de lasanha, molho à bolonhesa, molho bechamel, queijo parmesão e mussarela. Monte a lasanha alternando camadas de massa, molho à bolonhesa, molho bechamel e queijo. Termine com uma camada de molho bechamel e bastante queijo parmesão. Asse em forno pré-aquecido até dourar e borbulhar."),
            ("Como preparar uma lasanha italiana tradicional?", 
             "Para fazer uma lasanha tradicional italiana, você vai precisar de massa de lasanha, molho à bolonhesa, molho bechamel, queijo parmesão e mussarela. Monte a lasanha alternando camadas de massa, molho à bolonhesa, molho bechamel e queijo. Termine com uma camada de molho bechamel e bastante queijo parmesão. Asse em forno pré-aquecido até dourar e borbulhar.")
        ]

        for pergunta, resposta_esperada in informacoes:
            with self.subTest(mensagem=pergunta):
                self.verificar_resposta(pergunta, resposta_esperada)

    def teste_informacoes_basicas(self):
        """Testa informações básicas sobre o bot e suas respostas."""
        informacoes_basicas = [
            ("O que você faz?", "Eu sou o LetMeCook, um assistente virtual especializado em culinária e gastronomia. Estou aqui para responder suas dúvidas sobre receitas, técnicas de cozinha e dicas culinárias."),
            ("Qual é a sua função?", "Eu sou o LetMeCook, um assistente virtual especializado em culinária e gastronomia. Estou aqui para responder suas dúvidas sobre receitas, técnicas de cozinha e dicas culinárias."),
            ("Para que você serve?", "Eu sou o LetMeCook, um assistente virtual especializado em culinária e gastronomia. Estou aqui para responder suas dúvidas sobre receitas, técnicas de cozinha e dicas culinárias."),
            ("Quem te criou?", "Eu fui desenvolvido por uma equipe de entusiastas da culinária e tecnologia, que queriam criar um assistente virtual para ajudar pessoas a cozinhar melhor e aprender mais sobre gastronomia."),
            ("Quem desenvolveu você?", "Eu fui desenvolvido por uma equipe de entusiastas da culinária e tecnologia, que queriam criar um assistente virtual para ajudar pessoas a cozinhar melhor e aprender mais sobre gastronomia."),
            ("Qual é a origem do LetMeCook?", "Eu fui desenvolvido por uma equipe de entusiastas da culinária e tecnologia, que queriam criar um assistente virtual para ajudar pessoas a cozinhar melhor e aprender mais sobre gastronomia."),
            ("Como posso usar você?", "Para usar o LetMeCook, basta fazer perguntas relacionadas a culinária e gastronomia. Você pode perguntar sobre receitas, técnicas, dicas e qualquer outra dúvida culinária que tiver."),
            ("Como funciona o LetMeCook?", "Para usar o LetMeCook, basta fazer perguntas relacionadas a culinária e gastronomia. Você pode perguntar sobre receitas, técnicas, dicas e qualquer outra dúvida culinária que tiver."),
            ("Como interajo com você?", "Para usar o LetMeCook, basta fazer perguntas relacionadas a culinária e gastronomia. Você pode perguntar sobre receitas, técnicas, dicas e qualquer outra dúvida culinária que tiver.")
        ]

        for pergunta, resposta_esperada in informacoes_basicas:
            with self.subTest(mensagem=pergunta):
                self.verificar_resposta(pergunta, resposta_esperada)

if __name__ == "__main__":
    unittest.main()
