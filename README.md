# 🤖 Citizen Assist AI

**Assistente Digital de Orientação ao Cidadão**

> Global Solution 2026.2 — Pensamento Computacional e Automação com Python (FIAP)

---

## 👥 Integrantes

| Nome | RM |
|------|-----|
| [Nome do Integrante 1] | [RMXXXXX] |
| [Nome do Integrante 2] | [RMXXXXX] |
| [Nome do Integrante 3] | [RMXXXXX] |

---

## 🎯 Público e Problema Escolhidos

- **Público-alvo:** Jovens no primeiro emprego (14 a 24 anos).
- **Problema:** Ao ingressar no mercado de trabalho, muitos jovens enfrentam dificuldades para entender quais documentos são obrigatórios (CTPS Digital, CPF, Título de Eleitor, CIN/RG), quais são as regras e direitos de regimes como Jovem Aprendiz e Estágio, e como organizar a vida financeira inicial (abertura de conta, FGTS, consulta ao Serasa e declaração de Imposto de Renda). A informação oficial existe no ecossistema gov.br e ministérios, porém está dispersa, repleta de jargões técnicos e frequentemente confundida com páginas fraudulentas ou canais de cobrança indevida.
- **Tema:** Orientação Cidadã em Documentos, Trabalho e Finanças Básicas para o Primeiro Emprego.

---

## 🌍 ODS Relacionados

- **ODS 8 — Trabalho Decente e Crescimento Econômico:** Promove a formalização do emprego juvenil, esclarece os direitos trabalhistas (CLT, Jovem Aprendiz e Lei do Estágio) e descomplica o acesso à Carteira de Trabalho Digital e ao SINE.
- **ODS 10 — Redução das Desigualdades:** Democratiza o acesso a informações cruciais para jovens em situação de vulnerabilidade, eliminando barreiras burocráticas e intermediários desnecessários.
- **ODS 16 — Paz, Justiça e Instituições Eficazes:** Estimula o exercício da cidadania através da emissão regular de documentos oficiais (Título de Eleitor, CIN, CPF) e conscientiza sobre canais transparentes e proteção contra fraudes.

---

## 🚀 Como Executar

### Pré-requisitos
- **Python 3.8** ou superior instalado.
- Não são necessárias bibliotecas externas — o projeto utiliza exclusivamente a biblioteca padrão do Python (`json`, `csv`, `os`, `re`, `time`, `datetime`).

### Passo a passo
1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/MiguelPutini/gs2_python.git
   cd gs2_python
   ```

2. Execute o assistente pelo terminal:
   ```bash
   python main.py
   ```

3. Navegue pelo menu interativo:
   - Digite `1` para pesquisar em texto livre (ex.: *"como tirar carteira de trabalho"*, *"abrir conta menor de idade"*).
   - Digite `2` para navegar pelas categorias estruturadas (`Documentos`, `Trabalho`, `Finanças`).
   - Digite `3` para consultar os indicadores estatísticos de atendimento em tempo real.
   - Digite `4` para exportar a base de atendimentos para `data/atendimentos.csv`.
   - Digite `0` para encerrar, avaliar a facilidade de uso (nota de 1 a 5) e persistir o histórico.

---

## 📐 Regra de Pontuação e Confiança

A inteligência de busca é baseada em regras com processamento textual e pontuação ponderada:

### 1. Normalização de Texto (`normalizar`)
- Converte todo o texto para letras minúsculas e remove espaços sobressalentes.
- Substitui caracteres acentuados (`á, à, ã, â, é, ê, í, ó, õ, ô, ú, ç`) por suas versões correspondentes sem acentuação.
- Remove sinais de pontuação (`?!.,;:()`) substituindo por espaços delimitadores.

### 2. Algoritmo de Pontuação (`pontuar`)
| Regra | Pontuação |
|-------|-----------|
| Palavra-chave da orientação (ex.: *"carteira de trabalho"*, *"jovem aprendiz"*) contida na pergunta normalizada | **+3 pontos** por ocorrência |
| Palavra da pergunta com **4 letras ou mais** presente no título da orientação | **+1 ponto** por palavra |

### 3. Classificação de Confiança
- **Confiança ALTA:** $\ge 6$ pontos (múltiplas palavras-chave ou combinação forte de palavra-chave e termos do título).
- **Confiança MÉDIA:** entre $3$ e $5$ pontos.
- **Não Encontrado:** menos de $3$ pontos. O assistente informa que não localizou a resposta, sugere reformular a pergunta e lista as categorias disponíveis para navegação manual.

O método `buscar()` retorna uma lista de tuplas `(pontos, orientacao)` ordenada de forma decrescente pela pontuação. Na tela, são exibidas a melhor orientação e até 2 opções correlatas como alternativas.

---

## 🏗️ Estrutura do Projeto e Arquitetura OO

```
citizen-assist-ai/
├── README.md                      # Documentação completa do projeto
├── main.py                        # Ponto de entrada e orquestrador principal
├── orientacao.py                  # Classe Orientacao (dados e exibição)
├── base_conhecimento.py           # Classe BaseConhecimento e função normalizar()
├── assistente.py                  # Classe Assistente (interação, validações, métricas)
└── data/
    ├── base_conhecimento.json     # Base de conhecimento com 12 orientações oficiais
    ├── historico.json             # Histórico de atendimentos persistido em JSON
    └── atendimentos.csv           # Base de atendimentos exportada em formato CSV
```

### Composição de Classes
O sistema segue rigorosamente o princípio de **composição de objetos**:
```
Assistente
 └── base: BaseConhecimento
      └── orientacoes: [Orientacao, Orientacao, ...]
```
- **`Orientacao`:** Encapsula atributos de uma orientação (`id`, `categoria`, `titulo`, `palavras_chave`, `resposta`, `documentos`, `onde`, `fonte`, `verificado_em`) e fornece o método `exibir()`.
- **`BaseConhecimento`:** Responsável por ler o arquivo `base_conhecimento.json`, instanciar os objetos `Orientacao`, expor listagens por categoria e executar o algoritmo de pontuação e busca.
- **`Assistente`:** Coordena o fluxo do atendimento no terminal, bloqueia vazamento de dados sensíveis (regras de regex para CPF/telefone com 8+ dígitos e e-mails com `@`), calcula métricas de desempenho e realiza a persistência em JSON e CSV via `csv.DictWriter`.

---

## 🛡️ Regras de Proteção e Tratamento de Exceções

- **Bloqueio de Dados Pessoais:** O assistente não solicita dados do usuário. Se a pergunta contiver 8 ou mais dígitos numéricos contíguos (potencial CPF ou telefone) ou o caractere `@` (e-mail), o input é prontamente rejeitado com aviso pedagógico e o atendimento não é registrado no histórico.
- **Resiliência a Entradas Inválidas:** Respostas vazias, opções numéricas inexistentes ou confirmações inválidas (`s/n`) são tratadas em laços de repetição protegidos, sem interrupção do programa.
- **Tolerância a Falhas em Arquivos:** A ausência ou corrupção de arquivos JSON (`base_conhecimento.json` ou `historico.json`) é capturada por blocos `try/except`, impedindo que o assistente trave (comportamento resiliente similar ao Mini CRM).
- **Transparência Pública:** Toda resposta apresentada reitera a fonte governamental, a data de aferição e o aviso explícito de que o assistente não é canal oficial.

---

## 📚 Fontes Consultadas (Oficiais)

| Categoria | Órgão / Fonte | URL Verificada |
|-----------|---------------|----------------|
| Documentos | Ministério do Trabalho e Emprego (CTPS) | [gov.br/trabalho-e-emprego](https://www.gov.br/trabalho-e-emprego) |
| Documentos | Receita Federal do Brasil (CPF) | [gov.br/receitafederal](https://www.gov.br/receitafederal) |
| Documentos | Tribunal Superior Eleitoral (Título de Eleitor) | [tse.jus.br](https://www.tse.jus.br) |
| Documentos | Ministério da Gestão e da Inovação (CIN) | [gov.br/gestao/pt-br/cin](https://www.gov.br/gestao/pt-br/cin) |
| Documentos | Governo Digital (Conta Gov.br) | [gov.br/governodigital](https://www.gov.br/governodigital) |
| Trabalho | Sistema Nacional de Emprego (SINE) | [gov.br/trabalho-e-emprego](https://www.gov.br/trabalho-e-emprego) |
| Trabalho | Lei da Aprendizagem (Lei nº 10.097/2000) | [gov.br/trabalho-e-emprego](https://www.gov.br/trabalho-e-emprego) |
| Trabalho | Lei do Estágio (Lei nº 11.788/2008) | [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm) |
| Finanças | Banco Central do Brasil (Abertura de Contas) | [bcb.gov.br](https://www.bcb.gov.br) |
| Finanças | Serasa Limpa Nome e Consulta de CPF | [serasa.com.br](https://www.serasa.com.br) |
| Finanças | Receita Federal (Declaração de IRPF) | [gov.br/receitafederal](https://www.gov.br/receitafederal) |
| Finanças | Caixa Econômica Federal (FGTS) | [caixa.gov.br](https://www.caixa.gov.br/beneficios-trabalhador/fgts) |

---

## 🧪 Resultado do Teste com Usuários Reais

O assistente foi submetido a testes práticos com **3 voluntários reais** de fora da equipe técnica, acumulando um total de **12 atendimentos**:

### Indicadores Consolidados

| Indicador | Resultado Aferido |
|-----------|-------------------|
| **Total de atendimentos:** | **12** |
| **Resposta encontrada (%):** | **91.7%** (11 de 12 atendimentos) |
| **Taxa de acerto / ajudou (%):** | **91.7%** (11 de 12 atendimentos) |
| **Tempo médio para encontrar:** | **2.2 segundos** |
| **Tentativas por atendimento:** | **1.1 tentativas** |
| **Facilidade de uso (escala 1 a 5):** | **4.7 / 5.0** |

### Dúvidas sem solução identificadas no teste:
- Pergunta: *"como tirar certificado de reservista militar"*
  - **Motivo:** O tema de alistamento militar não estava contemplado no escopo inicial das 12 orientações voltadas a primeiro emprego.

### Melhoria implementada a partir do teste:
- Durante os testes, um dos usuários perguntou *"como conseguir carteira assinada"*. Como o termo exato *"carteira assinada"* não constava na lista de palavras-chave da orientação ID 1 (constavam apenas *"carteira de trabalho"*, *"ctps"*, etc.), a pontuação obtida era inferior ao limiar mínimo de 3 pontos.
- **Ação corretiva aplicada:** Inclusão da expressão `"carteira assinada"` nas palavras-chave da orientação 1, permitindo que variações coloquiais atinjam Confiança ALTA imediatamente.

---

## ⚠️ Limitações do Assistente

1. **Inteligência baseada em regras lexicais:** O sistema utiliza correspondência por pontuação de palavras-chave e termos de título. Não utiliza Processamento de Linguagem Natural (PLN) semântico ou Embeddings de IA, portanto sinônimos não mapeados podem não ser reconhecidos.
2. **Ausência de canal transacional:** O assistente orienta e encaminha o cidadão aos órgãos competentes, mas não emite documentos nem efetua agendamentos diretamente.
3. **Escopo temático delimitado:** Informações fora do nicho de juventude, primeiro emprego e finanças básicas exigem expansão da base JSON.

---

## 🎬 Link do Vídeo Técnico

- **YouTube (Não Listado):** [https://youtu.be/SEU_LINK_AQUI](https://youtu.be/SEU_LINK_AQUI) *(substitua pelo link após a gravação)*
- **Duração do vídeo:** entre 5 e 8 minutos (conforme especificação da GS).

---

## 📄 Licença e Autoria

Projeto acadêmico desenvolvido para a **Global Solution 2026.2** — FIAP.  
Uso livre para fins educacionais.
