import json
import csv
import os
import re
import time
from datetime import datetime
from base_conhecimento import BaseConhecimento


class Assistente:
    """Gerencia o atendimento ao cidadão, histórico e indicadores."""

    def __init__(self, nome: str, base: BaseConhecimento):
        self.nome = nome
        self.base = base
        self.historico: list[dict] = []
        self._carregar_historico()

    # ------------------------------------------------------------------ #
    #  Histórico persistente                                              #
    # ------------------------------------------------------------------ #

    def _caminho_historico(self) -> str:
        return os.path.join("data", "historico.json")

    def _carregar_historico(self):
        """Carrega histórico anterior, se existir."""
        caminho = self._caminho_historico()
        if os.path.exists(caminho):
            try:
                with open(caminho, "r", encoding="utf-8") as f:
                    self.historico = json.load(f)
            except (json.JSONDecodeError, Exception):
                self.historico = []

    def _salvar_historico(self):
        """Salva o histórico completo em JSON."""
        caminho = self._caminho_historico()
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(self.historico, f, ensure_ascii=False, indent=2)

    # ------------------------------------------------------------------ #
    #  Proteção de dados pessoais                                         #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _contem_dado_pessoal(texto: str) -> bool:
        """Verifica se o texto contém CPF, telefone ou e-mail."""
        # 8 ou mais dígitos (possível CPF ou telefone)
        digitos = re.sub(r"\D", "", texto)
        if len(digitos) >= 8:
            return True
        # E-mail
        if "@" in texto:
            return True
        return False

    # ------------------------------------------------------------------ #
    #  Menu principal                                                     #
    # ------------------------------------------------------------------ #

    def executar(self):
        """Loop principal do assistente."""
        print(f"\n{'='*60}")
        print(f"  Bem-vindo ao {self.nome}!")
        print(f"  Assistente de orientação para jovens no primeiro emprego")
        print(f"{'='*60}")

        while True:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Fazer uma pergunta")
            print("2. Navegar por categorias")
            print("3. Ver indicadores")
            print("4. Exportar atendimentos (CSV)")
            print("0. Sair")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                self.perguntar()
            elif opcao == "2":
                self.navegar()
            elif opcao == "3":
                self.indicadores()
            elif opcao == "4":
                self.exportar_csv()
            elif opcao == "0":
                self._pedir_nota()
                self._salvar_historico()
                self.exportar_csv()
                print(f"\nObrigado por usar o {self.nome}. Até a próxima!")
                break
            else:
                print("Opção inválida. Digite 1, 2, 3, 4 ou 0.")

    # ------------------------------------------------------------------ #
    #  Perguntar (busca por texto livre)                                  #
    # ------------------------------------------------------------------ #

    def perguntar(self):
        """Permite ao cidadão fazer perguntas em texto livre."""
        tentativas = 0

        while True:
            pergunta = input("\nDigite sua dúvida (0 para voltar): ").strip()

            if pergunta == "0":
                return

            if not pergunta:
                print("Entrada vazia. Digite sua dúvida ou 0 para voltar.")
                continue

            # Bloquear dados pessoais
            if self._contem_dado_pessoal(pergunta):
                print("Atenção: não digite CPF, telefone ou e-mail. Reescreva.")
                continue

            inicio = time.time()
            tentativas += 1
            resultados = self.base.buscar(pergunta)

            if not resultados or resultados[0][0] < 3:
                tempo = round(time.time() - inicio, 1)
                print("\nNão encontrei uma orientação para essa dúvida.")
                print("Tente usar outras palavras ou navegue pelas categorias:")
                for cat in self.base.categorias():
                    print(f"  • {cat}")
                self.registrar(
                    origem="pergunta",
                    pergunta=pergunta,
                    id_orientacao=None,
                    encontrou=False,
                    ajudou=False,
                    tentativas=tentativas,
                    tempo=tempo
                )
                tentativas = 0
                continue

            pontos, melhor = resultados[0]

            # Nível de confiança
            if pontos >= 6:
                confianca = "ALTA"
            else:
                confianca = "MÉDIA"

            print(f"\nConfiança da resposta: {confianca} ({pontos} pontos)")
            melhor.exibir()

            # Alternativas (até 2)
            if len(resultados) > 1:
                print("\nOutras orientações relacionadas:")
                for p, o in resultados[1:3]:
                    print(f"  • {o.titulo} ({p} pontos)")

            tempo = round(time.time() - inicio, 1)

            # Feedback
            ajudou = self._perguntar_sn("Essa orientação respondeu sua dúvida? (s/n): ")

            self.registrar(
                origem="pergunta",
                pergunta=pergunta,
                id_orientacao=melhor.id,
                encontrou=True,
                ajudou=ajudou,
                tentativas=tentativas,
                tempo=tempo
            )
            tentativas = 0

    # ------------------------------------------------------------------ #
    #  Navegar por categorias                                             #
    # ------------------------------------------------------------------ #

    def navegar(self):
        """Permite navegar pelas categorias e orientações."""
        while True:
            categorias = self.base.categorias()
            print("\n--- CATEGORIAS ---")
            for i, cat in enumerate(categorias, 1):
                qtd = len(self.base.por_categoria(cat))
                print(f"{i}. {cat} ({qtd} orientações)")
            print("0. Voltar")

            escolha = input("\nEscolha uma categoria: ").strip()

            if escolha == "0":
                return

            try:
                idx = int(escolha) - 1
                if idx < 0 or idx >= len(categorias):
                    print("Opção fora da faixa. Tente novamente.")
                    continue
            except ValueError:
                print("Entrada inválida. Digite um número.")
                continue

            categoria = categorias[idx]
            self._listar_orientacoes(categoria)

    def _listar_orientacoes(self, categoria: str):
        """Lista orientações de uma categoria e permite ver detalhes."""
        while True:
            orientacoes = self.base.por_categoria(categoria)
            print(f"\n--- {categoria.upper()} ---")
            for i, o in enumerate(orientacoes, 1):
                print(f"{i}. {o.titulo}")
            print("0. Voltar")

            escolha = input("\nEscolha uma orientação: ").strip()

            if escolha == "0":
                return

            try:
                idx = int(escolha) - 1
                if idx < 0 or idx >= len(orientacoes):
                    print("Opção fora da faixa. Tente novamente.")
                    continue
            except ValueError:
                print("Entrada inválida. Digite um número.")
                continue

            inicio = time.time()
            orientacao = orientacoes[idx]
            print(f"\nConfiança da resposta: ALTA (acesso direto)")
            orientacao.exibir()
            tempo = round(time.time() - inicio, 1)

            ajudou = self._perguntar_sn("Essa orientação respondeu sua dúvida? (s/n): ")

            self.registrar(
                origem="categoria",
                pergunta=orientacao.titulo,
                id_orientacao=orientacao.id,
                encontrou=True,
                ajudou=ajudou,
                tentativas=1,
                tempo=tempo
            )

    # ------------------------------------------------------------------ #
    #  Registrar atendimento                                              #
    # ------------------------------------------------------------------ #

    def registrar(self, origem: str, pergunta: str, id_orientacao,
                  encontrou: bool, ajudou: bool, tentativas: int, tempo: float):
        """Registra um atendimento no histórico."""
        atendimento = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "origem": origem,
            "pergunta": pergunta,
            "id_orientacao": id_orientacao,
            "encontrou": encontrou,
            "ajudou": ajudou,
            "tentativas": tentativas,
            "tempo": tempo
        }
        self.historico.append(atendimento)
        self._salvar_historico()

    # ------------------------------------------------------------------ #
    #  Indicadores                                                        #
    # ------------------------------------------------------------------ #

    def indicadores(self):
        """Calcula e exibe os indicadores dos atendimentos."""
        if not self.historico:
            print("\nNenhum atendimento registrado ainda.")
            return

        total = len(self.historico)
        encontrados = sum(1 for a in self.historico if a["encontrou"])
        ajudou = sum(1 for a in self.historico if a["ajudou"])
        tempos = [a["tempo"] for a in self.historico if a["encontrou"]]
        tentativas_lista = [a["tentativas"] for a in self.historico]
        sem_solucao = [a["pergunta"] for a in self.historico if not a["encontrou"]]

        taxa_encontrado = round((encontrados / total) * 100, 1) if total > 0 else 0
        taxa_ajudou = round((ajudou / total) * 100, 1) if total > 0 else 0
        tempo_medio = round(sum(tempos) / len(tempos), 1) if tempos else 0
        tentativas_media = round(sum(tentativas_lista) / len(tentativas_lista), 1) if tentativas_lista else 0

        # Nota de facilidade (últimas notas registradas)
        notas = [a.get("nota_facilidade") for a in self.historico if a.get("nota_facilidade")]
        facilidade_media = round(sum(notas) / len(notas), 1) if notas else "N/A"

        print(f"\n{'='*50}")
        print(f"  INDICADORES DO {self.nome.upper()}")
        print(f"{'='*50}")
        print(f"  Total de atendimentos:       {total}")
        print(f"  Resposta encontrada:          {taxa_encontrado}%")
        print(f"  Taxa de acerto (ajudou):      {taxa_ajudou}%")
        print(f"  Tempo médio para encontrar:   {tempo_medio}s")
        print(f"  Tentativas por atendimento:   {tentativas_media}")
        print(f"  Facilidade de uso (1 a 5):    {facilidade_media}")

        if sem_solucao:
            print(f"\n  Dúvidas sem solução:")
            for d in sem_solucao:
                print(f"    • {d}")
        print(f"{'='*50}")

    # ------------------------------------------------------------------ #
    #  Exportar CSV                                                       #
    # ------------------------------------------------------------------ #

    def exportar_csv(self):
        """Exporta atendimentos para data/atendimentos.csv."""
        if not self.historico:
            print("\nNenhum atendimento para exportar.")
            return

        caminho = os.path.join("data", "atendimentos.csv")
        campos = ["data", "origem", "pergunta", "id_orientacao",
                   "encontrou", "ajudou", "tentativas", "tempo"]

        try:
            with open(caminho, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
                writer.writeheader()
                writer.writerows(self.historico)
            print(f"\nAtendimentos exportados para '{caminho}'.")
        except Exception as e:
            print(f"Erro ao exportar CSV: {e}")

    # ------------------------------------------------------------------ #
    #  Utilitários                                                        #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _perguntar_sn(mensagem: str) -> bool:
        """Pergunta sim/não com validação."""
        while True:
            resposta = input(mensagem).strip().lower()
            if resposta in ("s", "sim"):
                return True
            elif resposta in ("n", "nao", "não"):
                return False
            else:
                print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

    def _pedir_nota(self):
        """Pede nota de facilidade de uso ao sair."""
        while True:
            nota = input("\nDe 1 a 5, quão fácil foi usar o assistente? ").strip()
            try:
                nota_int = int(nota)
                if 1 <= nota_int <= 5:
                    # Registra a nota no último atendimento ou cria um registro especial
                    if self.historico:
                        self.historico[-1]["nota_facilidade"] = nota_int
                    else:
                        self.historico.append({
                            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "origem": "avaliacao",
                            "pergunta": "",
                            "id_orientacao": None,
                            "encontrou": False,
                            "ajudou": False,
                            "tentativas": 0,
                            "tempo": 0,
                            "nota_facilidade": nota_int
                        })
                    print(f"Obrigado pela avaliação! Nota: {nota_int}/5")
                    return
                else:
                    print("Digite um número de 1 a 5.")
            except ValueError:
                print("Entrada inválida. Digite um número de 1 a 5.")
