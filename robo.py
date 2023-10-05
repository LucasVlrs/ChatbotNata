from chatterbot import ChatBot
from difflib import SequenceMatcher

CONFIANCA_MINIMA = 0.65


def comparar_mensagens(mensagem_digitada, mensagem_possivel):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_possivel.text
    if digitada and candidata:
        confianca = SequenceMatcher(None,
                                    digitada,
                                    candidata)
        confianca = round(confianca.ratio(), 2)

    return confianca


def iniciar():
    robo = ChatBot("Robo Nata",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])

    return robo


def executar(robo):
    while True:
        mensagem = input("Diga alguma coisa: \n")
        resposta = robo.get_response(mensagem.lower())
        print(f"Confiança: {resposta.confidence}")
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(">>", resposta.text)
        else:
            print("Ainda não sei responder isso")
            print("Faça outra pergunta")


if __name__ == "__main__":
    robo = iniciar()

    executar(robo)
