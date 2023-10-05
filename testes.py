import unittest
from robo import *


class testeSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def test_01_oi(self):
        saudacoes = ["oi", "olá", "tudo bem?"]

        for saudacao in saudacoes:
            print(f'Testando a saudação {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá, meu nome é Nata, sou um robô de atendimento que responde perguntas sobre o corpo humano,é só me perguntar algo.", resposta.text)

    def test_02_bom_dia(self):
        saudacoes = ["bom dia"]

        for saudacao in saudacoes:
            print(f'Testando a saudação {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                f"Bom dia, meu nome é Nata, sou um robô de atendimento que responde perguntas sobre o corpo humano,é só me perguntar algo.", resposta.text)

    def test_02_boa_tarde(self):
        saudacoes = ["boa tarde"]

        for saudacao in saudacoes:
            print(f'Testando a saudação {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                f"Boa tarde, meu nome é Nata, sou um robô de atendimento que responde perguntas sobre o corpo humano,é só me perguntar algo.", resposta.text)

    def test_03_boa_noite(self):
        saudacoes = ["boa noite"]

        for saudacao in saudacoes:
            print(f'Testando a saudação {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                f"Boa noite, meu nome é Nata, sou um robô de atendimento que responde perguntas sobre o corpo humano,é só me perguntar algo.", resposta.text)


class testePerguntasAnatomia(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def test_01_pergunta_01(self):
        perguntas = ["Quais são os sistemas que compões o corpo humano?"]

        for pergunta in perguntas:
            print(f'Testando a pergunta {pergunta}')

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Entre os principais sistemas do corpo humano, podemos citar o tegumentar, esquelético, muscular, cardiovascular, respiratório, digestório, urinário, nervoso e genital.", resposta.text)

    def test_02_pergunta_02(self):
        perguntas = ["qual o maior osso do corpo humano?"]

        for pergunta in perguntas:
            print(f'Testando a pergunta {pergunta}')

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("O fêmur é o osso que liga o quadril até o joelho, e é posição líder nesta seleção, dos 10 maiores ossos do corpo humano. Localizado na coxa, o fêmur calcula a média de quase 50.8 cm em comprimento, e é também o osso mais forte do corpo.", resposta.text)

    def test_03_pergunta_03(self):
        perguntas = ["qauntos músculos existem no corpo humano?"]

        for pergunta in perguntas:
            print(f'Testando a pergunta {pergunta}')

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("O corpo humano é formado por aproximadamente 600 músculos, que trabalham em conjunto com ossos, articulações e tendões para permitir que façamos diversos movimentos.", resposta.text)

    def test_04_pergunta_04(self):
        perguntas = [
            "quais os principais tipos de tecidos que existem no corpo humano?"]

        for pergunta in perguntas:
            print(f'Testando a pergunta {pergunta}')

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Os principais tecidos humanos são o tecido epitelial, tecido conjuntivo, tecido muscular e tecido nervoso.", resposta.text)

    def test_05_pergunta_05(self):
        perguntas = ["qual é a função do coração no corpo humano?"]

        for pergunta in perguntas:
            print(f'Testando a pergunta {pergunta}')

            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("O coração é um órgão musculoso responsável por impulsionar o sangue pelo corpo. Ele é encontrado entre os dois pulmões e sobre o diafragma, com aproximadamente dois terços de sua massa mais alinhados à esquerda. Esse órgão é revestido por um tecido muscular cardíaco chamado de miocárdio e, internamente, é dividido em quatro câmaras: dois átrios e dois ventrículos.", resposta.text)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(testeSaudacoes))
    testes.addTest(carregador.loadTestsFromTestCase(testePerguntasAnatomia))

    executor = unittest.TextTestRunner()
    executor.run(testes)
