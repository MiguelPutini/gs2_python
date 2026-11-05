"""
Citizen Assist AI - Assistente Digital de Orientação ao Cidadão
Global Solution 2026.2 - Pensamento Computacional e Automação com Python

Público-alvo: Jovens no primeiro emprego
Tema: Documentos, trabalho e finanças para quem está entrando no mercado
"""

from base_conhecimento import BaseConhecimento
from assistente import Assistente


def main():
    # Carrega a base de conhecimento a partir do JSON
    base = BaseConhecimento("data/base_conhecimento.json")
    base.carregar()

    # Verifica se a base foi carregada com sucesso
    if not base.orientacoes:
        print("Não foi possível iniciar o assistente: base de conhecimento vazia.")
        return

    # Cria e executa o assistente
    assistente = Assistente("Citizen Assist AI", base)
    assistente.executar()


if __name__ == "__main__":
    main()
