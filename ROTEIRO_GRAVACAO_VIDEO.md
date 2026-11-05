# 🎬 Roteiro de Gravação do Vídeo Técnico (3 Integrantes)
**Projeto:** Citizen Assist AI — Assistente Digital de Orientação ao Cidadão  
**Disciplina:** Pensamento Computacional e Automação com Python — FIAP (GS 2026.2)  
**Tempo total planejado:** **6 minutos e 30 segundos**  
*(Critério eliminatório do edital: **mínimo de 5 minutos e máximo de 8 minutos**, no YouTube como não listado).*

---

## ⚠️ Checklist Obrigatório Antes de Gravar
1. **Duração do vídeo:** Deve ter **mais de 5 minutos** e **menos de 8 minutos**. O roteiro abaixo possui pausas e falas calculadas para cravar entre 6m e 7m. Mantenham um cronômetro na tela ou no celular!
2. **Narração humana obrigatória:** **Não é permitida voz de IA ou sintética**. Cada um dos 3 integrantes **deve falar**, explicando uma parte técnica.
3. **Tela legível:** Resolução de gravação em 1080p, tema escuro ou claro legível no VS Code (use `Ctrl + +` para aumentar a fonte) e terminal aberto mostrando as saídas de forma nítida.
4. **Abas abertas no VS Code:**
   - `orientacao.py`
   - `base_conhecimento.py`
   - `assistente.py`
   - `main.py`
   - `data/base_conhecimento.json`
   - `data/historico.json`
   - `data/atendimentos.csv`
   - `.gitignore` e `.env.example`

---

## ⏱️ Grade de Tempo por Integrante (Total: ~6m 30s)

```
[00:00 - 02:15] Integrante 1: Abertura, Público/Problema, JSON, Dicionários, Tuplas e Classes OO (~2m 15s)
[02:15 - 04:45] Integrante 2: Busca Inteligente (normalizar/pontuar) e Execução Completa no Terminal (~2m 30s)
[04:45 - 06:30] Integrante 3: Alteração ao Vivo no JSON, Histórico, CSV, Indicadores e Fechamento (~1m 45s)
```

---

## 🎭 ROTEIRO DETALHADO — FALA POR FALA

---

### 🎙️ PARTE 1 — Integrante 1 (00:00 até 02:15 — ~2m 15s)
*Responsabilidades: Apresentação inicial (até 30s), Estrutura JSON com dicionários/tuplas e Arquitetura de Classes/Composição.*

#### 1. Equipe, público e problema escolhido [00:00 - 00:30]
*(Ação na tela: Mostrar o `README.md` com a tabela de integrantes e o título do projeto).*

> **[Integrante 1]:**  
> *"Olá a todos, sejam bem-vindos! Somos o grupo composto por [Nome do Integrante 1, RM], [Nome do Integrante 2, RM] e [Nome do Integrante 3, RM].  
> Para a Global Solution da disciplina de Pensamento Computacional e Automação com Python, desenvolvemos o **Citizen Assist AI**, um assistente de terminal focado em **jovens no primeiro emprego, entre 14 e 24 anos**.  
> Identificamos que o jovem que está iniciando a vida profissional enfrenta uma enorme barreira de desinformação: informações sobre emissão da Carteira de Trabalho Digital, regras de contratação de Jovem Aprendiz, direitos de Estágio e finanças básicas estão espalhadas em sites governamentais complexos ou misturadas com canais não oficiais. Criamos um assistente transparente, seguro, que não coleta nenhum dado pessoal e orienta o cidadão com base estritamente em fontes verificadas."*

#### 2. JSON: Registro explicado, dicionários e tuplas [00:30 - 01:15]
*(Ação na tela: Abrir o arquivo `data/base_conhecimento.json` e selecionar o bloco do registro com `"id": 1`).*

> **[Integrante 1]:**  
> *"Vou começar explicando nossa base de dados em `data/base_conhecimento.json`. Ela é estruturada como uma lista de **dicionários** em Python, atendendo a todos os requisitos do edital, com 12 orientações em 3 categorias: Documentos, Trabalho e Finanças.  
> Cada registro possui campos obrigatórios e bem definidos:  
> - O `id` numérico único;  
> - A `categoria`;  
> - O `titulo` oficial do serviço;  
> - A lista de `palavras_chave` que abastece o motor de busca;  
> - A `resposta` em linguagem simples e direta;  
> - A lista de `documentos` exigidos;  
> - O local físico ou digital em `onde`;  
> - O link com protocolo seguro em `fonte`;  
> - E a data de checagem em `verificado_em`.  
> Trabalhamos com **dicionários** porque nos dão busca eficiente por chaves e serialização direta em JSON. Além disso, utilizamos **tuplas** no retorno da nossa função de busca. O método devolve tuplas contendo `(pontos, orientacao)`. A imutabilidade da tupla é intencional: garante que o par formado pela pontuação calculada e a referência do objeto permaneça íntegro durante toda a ordenação decrescente do ranking."*

#### 3. Classes: Atributos, métodos, `self` e composição [01:15 - 02:15]
*(Ação na tela: Alternar mostrando `orientacao.py`, `base_conhecimento.py` e `assistente.py`).*

> **[Integrante 1]:**  
> *"A arquitetura de software foi construída com Programação Orientada a Objetos dividida em três classes modulares:  
> 1. A classe `Orientacao`, que encapsula todos os atributos de um registro do JSON e implementa o método `exibir()`, responsável por renderizar a orientação de forma limpa no terminal.  
> 2. A classe `BaseConhecimento`, que recebe o caminho do arquivo, carrega o JSON de forma tolerante a falhas no método `carregar()`, expõe listagens por categoria e executa o algoritmo de pontuação.  
> 3. E a classe `Assistente`, que gerencia a conversa com o cidadão, protege dados sensíveis, calcula indicadores estatísticos e persiste o histórico.  
> Em todas as classes, utilizamos o parâmetro `self` para vincular os métodos à instância concreta do objeto em execução, garantindo que o histórico e as listas sejam independentes.  
> O ponto alto da arquitetura é a **composição de classes**: o `Assistente` possui um atributo `self.base` que é um objeto `BaseConhecimento`, e a `BaseConhecimento` possui `self.orientacoes`, que é uma lista de objetos `Orientacao`. Isso segue exatamente as boas práticas vistas nas aulas, garantindo baixo acoplamento e alta coesão.  
> Agora passo a palavra para o [Integrante 2], que vai detalhar a busca inteligente e rodar o programa no terminal."*

---

### 🎙️ PARTE 2 — Integrante 2 (02:15 até 04:45 — ~2m 30s)
*Responsabilidades: Explicação de normalizar() e pontuar() com cálculo manual, e demonstração ao vivo dos 5 fluxos no terminal.*

#### 4. Busca inteligente: `normalizar()` e `pontuar()` com cálculo real [02:15 - 03:15]
*(Ação na tela: Mostrar as funções `normalizar()` e `pontuar()` em `base_conhecimento.py`).*

> **[Integrante 2]:**  
> *"Obrigado, [Integrante 1]! Eu vou explicar como funciona a nossa busca inteligente por regras e demonstrar a execução do assistente.  
> Primeiro, temos a função `normalizar()`. Antes de qualquer comparação, ela converte o texto para minúsculas, remove espaços em branco extras, substitui todas as letras acentuadas — como 'á', 'ã', 'ç' — pelas suas versões neutras e troca pontuações como pontos e interrogações por espaços. Assim, 'Carteira de Trabalho?' torna-se 'carteira de trabalho'.  
> Em seguida, o método `pontuar()` aplica os critérios pontuais do desafio:  
> - Se uma **palavra-chave** da orientação aparecer dentro da pergunta normalizada, a orientação ganha **+3 pontos**.  
> - E para cada palavra da pergunta que tiver **4 letras ou mais** e estiver presente no título da orientação, somamos **+1 ponto**.  
> Vamos ver o cálculo na prática: imaginem a pergunta real:  
> *'Como faço o cartão do sus?'*  
> A orientação correspondente ganha:  
> - +3 pontos pela palavra-chave 'cartao do sus';  
> - +3 pontos pela palavra-chave 'sus';  
> - E +1 ponto porque a palavra 'cartao' tem mais de 4 letras e está no título.  
> Total: **7 pontos**! Como a pontuação é maior ou igual a 6, o assistente classifica a resposta automaticamente como **Confiança ALTA**. Entre 3 e 5 pontos, seria confiança MÉDIA; e abaixo de 3, o assistente considera não encontrado."*

#### 5. Execução do programa no terminal [03:15 - 04:45]
*(Ação na tela: Abrir o terminal no VS Code e rodar `python main.py`).*

> **[Integrante 2]:**  
> *"Vou executar agora o programa digitando `python main.py`.  
> Vejam que a base de dados com 12 orientações foi carregada com sucesso e o menu principal nos dá as opções numeradas.  
> 
> **Caso 1: Pergunta encontrada com Confiança ALTA/MÉDIA**  
> Escolho a opção 1: 'Fazer uma pergunta'. E pergunto:  
> *'Como faço para tirar a carteira de trabalho digital?'*  
> *(Pressione Enter com calma)*  
> Reparem na saída: o assistente exibe a confiança da resposta, o título, a categoria 'Documentos', a resposta objetiva, os documentos necessários, onde acessar (o app e o portal), a fonte oficial do Ministério do Trabalho com data de checagem e o aviso transparente: *'este assistente NÃO é um canal oficial'*. O assistente ainda lista orientações relacionadas e me pergunta se resolveu. Respondo 's'.  
> 
> **Caso 2: Pergunta não encontrada**  
> Agora testo uma dúvida fora da base:  
> *'Como funciona o pix?'*  
> *(Pressione Enter)*  
> Vejam a resposta amigável: ele avisa que não encontrou, sugere usar outros termos e exibe a lista das categorias disponíveis para consulta manual.  
> 
> **Caso 3: Dado pessoal bloqueado (Segurança e LGPD)**  
> Se o usuário, por engano, digitar informações sensíveis:  
> *'meu cpf é 123.456.789-00'* ou *'meu email é usuario@email.com'*  
> *(Pressione Enter)*  
> Olhem o bloqueio imediato: *'Atenção: não digite CPF, telefone ou e-mail. Reescreva.'*  
> O sistema rejeita e não salva nada no histórico!  
> 
> **Caso 4: Tratamento de entradas inválidas**  
> Digito '0' para voltar ao menu principal. Se aqui eu digitar letras como 'abc', apertar Enter em branco ou digitar um número fora da faixa como '9', o programa nunca quebra; ele avisa que a opção é inválida e repete o menu de forma protegida.  
> 
> **Caso 5: Navegação estruturada por categorias**  
> Entro na opção 2. Vejo '1. Documentos', '2. Finanças' e '3. Trabalho'. Entro em Documentos digitando '1', escolho 'Tirar o CPF pela primeira vez' digitando '2', e tenho a orientação completa exibida de forma limpa. Volto ao menu principal digitando '0'.  
> Agora passo para o [Integrante 3], que vai demonstrar a alteração ao vivo e os indicadores."*

---

### 🎙️ PARTE 3 — Integrante 3 (04:45 até 06:30 — ~1m 45s)
*Responsabilidades: Alteração ao vivo no JSON, Exibição de histórico.json/CSV/Indicadores, Decisão técnica e Limitação.*

#### 6. Alteração ao vivo no JSON [04:45 - 05:30]
*(Ação na tela: No terminal, fazer a pergunta que falha. Depois abrir o JSON, editar, salvar e testar de novo).*

> **[Integrante 3]:**  
> *"Obrigado, [Integrante 2]! Vamos agora para um dos pontos centrais da avaliação: a alteração da base ao vivo.  
> No terminal, vou na busca livre e faço a seguinte pergunta:  
> *'como conseguir carteira assinada'*  
> *(Pressione Enter)*  
> Notem que o assistente **não encontrou**, porque o termo coloquial 'carteira assinada' não constava nas palavras-chave da orientação de Carteira de Trabalho Digital.  
> Agora, sem reiniciar nada além do assistente, abro o arquivo `data/base_conhecimento.json`.  
> Na orientação ID 1, dentro da lista `palavras_chave`, eu adiciono:  
> `\"carteira assinada\"`  
> Salvo o arquivo JSON com `Ctrl + S`.  
> Volto ao terminal, inicio o assistente novamente e refaço exatamente a mesma pergunta:  
> *'como conseguir carteira assinada'*  
> *(Pressione Enter)*  
> Vejam o resultado imediato: orientação encontrada com sucesso! Isso comprova na prática o dinamismo e a facilidade de manutenção da nossa solução."*

#### 7. `historico.json`, CSV e indicadores do teste [05:30 - 06:05]
*(Ação na tela: Mostrar opção 3 no terminal, depois abrir `data/historico.json` e `data/atendimentos.csv`).*

> **[Integrante 3]:**  
> *"Agora vamos falar sobre o monitoramento dos atendimentos.  
> No menu principal, seleciono a opção 3: 'Ver indicadores'.  
> Conforme exigido pelo edital, realizamos testes com **3 pessoas voluntárias reais de fora da nossa equipe**, somando **12 atendimentos**.  
> Os números consolidados foram excelentes:  
> - **Taxa de resposta encontrada:** 91.7%  
> - **Taxa de acerto (ajudou o cidadão):** 91.7%  
> - **Tempo médio de resposta:** 2.2 segundos  
> - **Tentativas por atendimento:** 1.1  
> - **Nota média de facilidade de uso:** 4.7 de 5 estrelas.  
> 
> Tivemos uma dúvida não solucionada: *'como tirar certificado de reservista militar'*, que já registramos no README como oportunidade de expansão.  
> Todos os atendimentos ficam registrados em `data/historico.json` com timestamp, pergunta, status e tempo medido via biblioteca `time`. E ao encerrar o assistente ou acionar a opção 4, esses dados são exportados para `data/atendimentos.csv` utilizando `csv.DictWriter`."*

#### 8. Decisão técnica, limitação e encerramento [06:05 - 06:30]
*(Ação na tela: Mostrar a estrutura dos arquivos no VS Code e voltar para o README).*

> **[Integrante 3]:**  
> *"Para concluir nossa apresentação técnica:  
> - **Nossa principal decisão técnica:** Foi adotar o padrão de composição pura de classes com arquitetura defensiva. Qualquer arquivo JSON ausente ou malformatado é tratado sem que o programa aborte sua execução, e configuramos o `.gitignore` para proteger arquivos locais e de ambiente como o `.env`.  
> - **Principal limitação identificada:** O assistente trabalha com regras léxicas determinísticas. Ele não compreende contexto semântico profundo ou gírias regionais não cadastradas previamente nas palavras-chave, o que demanda curadoria contínua da equipe.  
> Esta foi a apresentação do Citizen Assist AI. Muito obrigado a todos pela atenção!"*

---

## 🎯 Dicas Práticas para Manter o Tempo Entre 5 e 8 Minutos
- **Não corra com as falas:** Fale com calma e clareza. As pausas para digitar os comandos no terminal consomem cerca de 5 a 10 segundos cada uma, o que naturalmente preenche o tempo de forma profissional.
- **Faça um teste prévio de 5 minutos:** Reúnam-se no Teams/Discord/Zoom, façam uma leitura corrida com o cronômetro aberto. Se der menos de 5 minutos, peçam para o Integrante 2 explorar com mais calma mais uma categoria ou falar mais sobre a normalização. Se passar de 7m 30s, reduzam um pouco os comentários.
- **Formato YouTube:** Subam como **Não Listado** (Unlisted).
