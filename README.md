# 🤖 Citizen Assist AI

**Assistente Digital de Orientação ao Cidadão**

> Global Solution 2026.2 — Pensamento Computacional e Automação com Python (FIAP)

---

## 👥 Integrantes

| Nome | RM |
|------|-----|
| [Seu Nome 1] | [RM1] |
| [Seu Nome 2] | [RM2] |
| [Seu Nome 3] | [RM3] |

---

## 🎯 Público e Problema Escolhidos

**Público-alvo:** Jovens no primeiro emprego (16 a 24 anos)

**Problema:** Muitos jovens que estão entrando no mercado de trabalho pela primeira vez não sabem quais documentos precisam tirar, quais são seus direitos trabalhistas ou como lidar com suas primeiras finanças. A informação existe, mas está espalhada por vários sites governamentais e muitas vezes é difícil de entender.

**Tema:** Documentos, trabalho e finanças para jovens entrando no mercado

---

## 🌍 ODS Relacionados

- **ODS 8 — Trabalho Decente e Crescimento Econômico:** orientar jovens sobre seus direitos trabalhistas e como acessar o mercado de trabalho
- **ODS 10 — Redução das Desigualdades:** democratizar o acesso à informação sobre serviços públicos
- **ODS 16 — Paz, Justiça e Instituições Eficazes:** facilitar o acesso a documentos e serviços governamentais

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.8+** instalado
2. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/citizen-assist-ai.git
   cd citizen-assist-ai
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```

> Não são necessárias bibliotecas externas. O projeto usa apenas módulos padrão do Python.

---

## 📐 Regra de Pontuação

A busca funciona por **pontuação baseada em regras**:

| Regra | Pontos |
|-------|--------|
| Palavra-chave da orientação aparece na pergunta | **+3** por palavra-chave |
| Palavra da pergunta (4+ letras) aparece no título | **+1** por palavra |

**Níveis de confiança:**

| Pontuação | Confiança |
|-----------|-----------|
| 6 ou mais | **ALTA** |
| 3 a 5 | **MÉDIA** |
| Menos que 3 | Não encontrado — sugere categorias |

**Normalização:** antes da comparação, textos são convertidos para minúsculas, sem acentos e sem pontuação.

---

## 🏗️ Estrutura do Projeto

```
citizen-assist-ai/
├── README.md                      # Este arquivo
├── main.py                        # Ponto de entrada do programa
├── orientacao.py                  # Classe Orientacao
├── base_conhecimento.py           # Classe BaseConhecimento + normalizar()
├── assistente.py                  # Classe Assistente
└── data/
    ├── base_conhecimento.json     # Base de conhecimento (12 orientações)
    ├── historico.json             # Histórico de atendimentos (gerado)
    └── atendimentos.csv           # Exportação CSV (gerado)
```

---

## 🔗 Integrações com Outras Disciplinas

*(Preencher se houver integrações com outras disciplinas da GS)*

---

## 📚 Fontes Consultadas

| Fonte | URL |
|-------|-----|
| Gov.br — Trabalho e Emprego | https://www.gov.br/trabalho-e-emprego |
| Receita Federal | https://www.gov.br/receitafederal |
| TSE — Título de Eleitor | https://www.tse.jus.br |
| Gov.br — Carteira de Identidade Nacional | https://www.gov.br/gestao/pt-br/cin |
| Gov.br — Governo Digital | https://www.gov.br/governodigital |
| Lei do Estágio (11.788/2008) | https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm |
| Banco Central do Brasil | https://www.bcb.gov.br |
| Serasa | https://www.serasa.com.br |
| Caixa — FGTS | https://www.caixa.gov.br/beneficios-trabalhador/fgts |

---

## 🧪 Resultado do Teste com Usuários

O assistente foi testado com **3 pessoas de fora da equipe**, totalizando **10+ atendimentos**.

### Indicadores obtidos:

| Indicador | Resultado |
|-----------|-----------|
| Resposta encontrada | __%% |
| Taxa de acerto (ajudou) | __%% |
| Tempo médio | __s |
| Tentativas por atendimento | __ |
| Facilidade de uso (1 a 5) | __ |

### Dúvidas sem solução encontradas no teste:
- *(preencher após o teste)*

### Melhoria feita a partir do teste:
- *(ex.: adicionada a palavra-chave "X" na orientação Y)*

---

## ⚠️ Limitações

- O assistente **não** é um canal oficial do governo. Todas as informações são baseadas em fontes públicas verificadas.
- A busca é baseada em **palavras-chave e regras**, não em inteligência artificial. Perguntas muito diferentes das palavras-chave cadastradas podem não retornar resultados.
- O assistente **não coleta** nem armazena dados pessoais (CPF, telefone, e-mail).
- As informações podem ficar desatualizadas. Sempre confira no site oficial.

---

## 🎬 Link do Vídeo

📹 [Vídeo técnico no YouTube](https://youtube.com/SEU-LINK-AQUI) *(não listado)*

---

## 📄 Licença

Projeto acadêmico — FIAP Global Solution 2026.2
