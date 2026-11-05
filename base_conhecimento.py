import json
import os
from orientacao import Orientacao

# Mapa de acentos para normalização
ACENTOS = {
    "á": "a", "à": "a", "ã": "a", "â": "a",
    "é": "e", "ê": "e",
    "í": "i",
    "ó": "o", "õ": "o", "ô": "o",
    "ú": "u",
    "ç": "c"
}


def normalizar(texto: str) -> str:
    """Remove acentos, pontuação e converte para minúsculas."""
    texto = texto.lower().strip()
    for letra, troca in ACENTOS.items():
        texto = texto.replace(letra, troca)
    for sinal in "?!.,;:()":
        texto = texto.replace(sinal, " ")
    return " " + " ".join(texto.split()) + " "


class BaseConhecimento:
    """Gerencia o conjunto de orientações carregadas do JSON."""

    def __init__(self, caminho: str):
        self.caminho = caminho
        self.orientacoes: list[Orientacao] = []

    def carregar(self):
        """Lê o JSON e cria os objetos Orientacao."""
        if not os.path.exists(self.caminho):
            print(f"Erro: arquivo '{self.caminho}' não encontrado.")
            return
        try:
            with open(self.caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
            self.orientacoes = [Orientacao(d) for d in dados]
            print(f"Base carregada: {len(self.orientacoes)} orientações.")
        except json.JSONDecodeError:
            print(f"Erro: arquivo '{self.caminho}' está corrompido.")
        except Exception as e:
            print(f"Erro ao carregar base: {e}")

    def categorias(self) -> list[str]:
        """Retorna lista de categorias únicas, em ordem alfabética."""
        cats = sorted(set(o.categoria for o in self.orientacoes))
        return cats

    def por_categoria(self, categoria: str) -> list[Orientacao]:
        """Retorna orientações de uma categoria específica."""
        return [o for o in self.orientacoes if o.categoria == categoria]

    def pontuar(self, pergunta_norm: str, orientacao: Orientacao) -> int:
        """Calcula a pontuação de uma orientação em relação à pergunta."""
        pontos = 0

        # +3 pontos para cada palavra-chave encontrada na pergunta
        for chave in orientacao.palavras_chave:
            chave_norm = normalizar(chave)
            if chave_norm.strip() in pergunta_norm:
                pontos += 3

        # +1 ponto para cada palavra da pergunta (4+ letras) no título
        titulo_norm = normalizar(orientacao.titulo)
        palavras_pergunta = pergunta_norm.split()
        for palavra in palavras_pergunta:
            if len(palavra) >= 4 and f" {palavra} " in titulo_norm:
                pontos += 1

        return pontos

    def buscar(self, pergunta: str) -> list[tuple[int, Orientacao]]:
        """Busca orientações por pontuação. Retorna lista de tuplas (pontos, orientacao)."""
        pergunta_norm = normalizar(pergunta)
        resultados = []

        for orientacao in self.orientacoes:
            pontos = self.pontuar(pergunta_norm, orientacao)
            if pontos > 0:
                resultados.append((pontos, orientacao))

        # Ordena da maior para a menor pontuação
        resultados.sort(key=lambda x: x[0], reverse=True)
        return resultados

