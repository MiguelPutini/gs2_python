# 🎬 Roteiro de Gravação do Vídeo Técnico (3 Integrantes)
**Projeto:** Citizen Assist AI — Assistente Digital de Orientação ao Cidadão  
**Disciplina:** Pensamento Computacional e Automação com Python — FIAP (GS 2026.2)  
**Tempo total estimado:** ~6 minutos e 30 segundos (Regra da FIAP: **entre 5 e 8 minutos** no YouTube como não listado).

---

## 📋 Recomendações Importantes Antes de Gravar
1. **Configuração da Tela:** Deixe aberto o VS Code com fonte legível (Zoom: Ctrl + +) e um terminal limpo ao lado ou embaixo.
2. **Abas abertas no VS Code:** `main.py`, `orientacao.py`, `base_conhecimento.py`, `assistente.py`, `data/base_conhecimento.json`, `data/historico.json` e `data/atendimentos.csv`.
3. **Câmera:** É opcional. O mais importante é o áudio claro e a tela 100% legível.
4. **Regra de ouro:** **Não usar voz sintética ou IA**. Todos os 3 integrantes devem falar individualmente.

---

## ⏱️ Linha do Tempo e Distribuição

| Bloco | Responsável | Tópicos Obrigatórios | Duração |
|---|---|---|---|
| **Parte 1** | **Integrante 1** | 1. Equipe, público e problema escolhido<br>2. JSON, registros, dicionários e tuplas<br>3. Classes: atributos, métodos, `self` e composição | ~2m 00s |
| **Parte 2** | **Integrante 2** | 4. Busca inteligente: `normalizar()` e `pontuar()` com cálculo real<br>5. Execução no terminal: encontrada, não encontrada, inválida, dado pessoal e categorias | ~2m 30s |
| **Parte 3** | **Integrante 3** | 6. Alteração ao vivo no JSON (palavra-chave)<br>7. `historico.json`, CSV e indicadores do teste real<br>8. Decisão técnica e limitação do assistente | ~2m 00s |

---

## 🎭 ROTEIRO DETALHADO FALA POR FALA

---

### 🎙️ PARTE 1 — Integrante 1 (~2 min)
*Foco: Abertura, Contexto, Estruturas de Dados (JSON, Dicionários, Tuplas) e Orientação a Objetos.*

#### 1. Equipe, público e problema escolhido (até 30s)
> **[Integrante 1 falando]:**  
> "Olá a todos! Somos a equipe composta por [Nome 1 - RM], [Nome 2 - RM] e [Nome 3 - RM].  
> Para esta Global Solution de Pensamento Computacional e Automação com Python, desenvolvemos o **Citizen Assist AI**, voltado para **jovens no primeiro emprego, entre 14 e 24 anos**.  
> O problema que atacamos é a desinformação burocrática: quem está ingressando no mercado tem dúvidas críticas sobre emissão da Carteira de Trabalho Digital, regras de Jovem Aprendiz, Lei do Estágio e finanças básicas. Nosso assistente orienta esse público de forma rápida, com fontes oficiais do governo, sem coletar dados pessoais e em linguagem acessível."

#### 2. JSON: Registro explicado, dicionários e tuplas (~45s)
*(Ação na tela: Mostrar o arquivo `data/base_conhecimento.json` aberto no editor).*
> **[Integrante 1 falando]:**  
> "A base de conhecimento fica em `data/base_conhecimento.json`. É uma lista de dicionários em Python, onde cada objeto representa uma orientação oficial completa.  
> Vejam este exemplo do registro 1: temos campos obrigatórios como `id`, `categoria`, `titulo`, a lista de `palavras_chave`, o texto explicativo em `resposta`, a lista de `documentos`, o local de atendimento em `onde`, o link oficial verificado em `fonte` e a data de verificação em `verificado_em`.  
> No Python, usamos **dicionários** pela flexibilidade de mapear chaves e valores, e utilizamos **tuplas** no retorno da nossa busca inteligente, onde cada resultado é uma tupla imutável contendo `(pontos, orientacao)`. A tupla garante integridade para que a nota atribuída e a referência do objeto não sejam alteradas acidentalmente durante a ordenação."

#### 3. Classes: Atributos, métodos, `self` e composição (~45s)
*(Ação na tela: Mostrar os arquivos `orientacao.py`, `base_conhecimento.py` e `assistente.py`).*
> **[Integrante 1 falando]:**  
> "Nosso código é estruturado em três classes bem modularizadas:
> - A classe `Orientacao` guarda os atributos de uma orientação específica e possui o método `exibir()`, que imprime o card formatado no terminal.
> - A classe `BaseConhecimento` recebe o caminho do JSON, faz a leitura tolerante a falhas no método `carregar()`, lista categorias e gerencia o algoritmo de busca.
> - A classe `Assistente` orquestra o diálogo com o cidadão, faz o tratamento de segurança e gera os relatórios.
> O parâmetro `self` é fundamental porque referencia a instância ativa que está executando a operação, permitindo isolar atributos de estado como o histórico e a coleção de orientações.  
> Além disso, aplicamos o conceito de **composição de classes**: o `Assistente` contém uma instância de `BaseConhecimento`, que por sua vez contém uma lista de objetos do tipo `Orientacao`. Isso desacopla as responsabilidades com elegância."

---

### 🎙️ PARTE 2 — Integrante 2 (~2 min 30 s)
*Foco: Algoritmo de Busca por Regras e Demonstração Completa da Execução no Terminal.*

#### 4. Busca: `normalizar()` e `pontuar()` com cálculo real (~50s)
*(Ação na tela: Mostrar a função `normalizar()` e o método `pontuar()` em `base_conhecimento.py`).*
> **[Integrante 2 falando]:**  
> "Agora vou explicar o motor de busca inteligente por regras do assistente.  
> Primeiro, a função `normalizar()` remove qualquer acentuação usando uma tabela de mapeamento, converte tudo para minúsculas e substitui pontuações por espaços, garantindo que 'Título' e 'titulo' sejam equivalentes.  
> Em seguida, o método `pontuar()` aplica as regras do edital:
> - Para cada **palavra-chave** da orientação que aparece na pergunta normalizada, somamos **+3 pontos**.
> - Para cada palavra da pergunta com **4 letras ou mais** que aparece no título da orientação, somamos **+1 ponto**.  
> Vamos ver um exemplo real: se o usuário perguntar:  
> *'Como faço o cartão do sus?'*  
> Ele ganha +3 pela chave 'cartao do sus', +3 pela chave 'sus' e +1 pela palavra 'cartao' que tem mais de 4 letras e está no título, totalizando **7 pontos**. Como 7 é maior ou igual a 6, o assistente classifica com **Confiança ALTA**."

#### 5. Execução ao vivo no terminal (~1m 40s)
*(Ação na tela: Abrir o terminal e executar `python main.py`).*
> **[Integrante 2 falando]:**  
> "Vamos agora para a execução prática no terminal. Rodo `python main.py` e o menu principal é carregado com as 12 orientações oficiais.  
> Vou demonstrar os 5 cenários exigidos:  
> 
> **1º Cenário — Pergunta encontrada:**  
> Digito a opção 1 e faço a pergunta: *'Como tiro a carteira de trabalho digital?'*  
> *(Pressione Enter)*  
> Vejam que o assistente retornou com **Confiança ALTA**, exibiu o título, a resposta simples, os documentos necessários, a fonte oficial `gov.br`, a data em que checamos e o aviso obrigatório de que não somos canal oficial. Respondo 's' para confirmar que atendeu a dúvida.  
> 
> **2º Cenário — Pergunta não encontrada:**  
> Agora digito: *'Como funciona o pix?'*  
> *(Pressione Enter)*  
> Como a pontuação não atinge o limiar mínimo de 3 pontos, o assistente avisa educadamente que não encontrou orientação e sugere reformular a frase ou navegar pelas categorias.  
> 
> **3º Cenário — Dado pessoal bloqueado:**  
> Para proteger a privacidade do cidadão, se alguém digitar acidentalmente: *'meu cpf é 123.456.789-00'* ou um e-mail com *@*, vejam a resposta imediata:  
> *'Atenção: não digite CPF, telefone ou e-mail. Reescreva.'*  
> O sistema bloqueia a entrada e não registra nenhum dado sensível.  
> 
> **4º Cenário — Tratamento de entradas inválidas:**  
> Se eu digitar uma letra no menu, deixar vazio ou colocar uma opção inexistente como '99', o sistema nunca quebra nem encerra; ele informa a entrada inválida e volta a pedir a opção correta.  
> 
> **5º Cenário — Navegação por categorias:**  
> Digito '0' para voltar ao menu e escolho a opção 2, 'Navegar por categorias'. Seleciono '1. Documentos' e vejo todas as opções numeradas. Clico em '2. Tirar o CPF pela primeira vez' e tenho acesso direto e detalhado a todas as instruções, com a opção de retornar pelo '0'."

---

### 🎙️ PARTE 3 — Integrante 3 (~2 min)
*Foco: Alteração ao Vivo no JSON, Histórico, CSV, Indicadores Reais, Decisão Técnica e Limitações.*

#### 6. Alteração ao vivo no JSON (~45s)
*(Ação na tela: Fazer a pergunta no terminal que falha, depois editar o JSON e mostrar o sucesso).*
> **[Integrante 3 falando]:**  
> "Agora vamos demonstrar o ponto 6 do roteiro: a alteração ao vivo na base de conhecimento.  
> No terminal, vou na busca livre e digito: *'como conseguir carteira assinada'*  
> *(Pressione Enter)*  
> Reparem que o assistente **não encontrou**, porque o termo exato 'carteira assinada' ainda não estava cadastrado nas palavras-chave da nossa orientação.  
> Agora, sem fechar o raciocínio, abro o arquivo `data/base_conhecimento.json`, vou na orientação com id 1 (Carteira de Trabalho Digital) e adiciono a palavra-chave:  
> `\"carteira assinada\"` no array de `palavras_chave`.  
> Salvo o arquivo, reinicio o assistente e faço exatamente a mesma pergunta: *'como conseguir carteira assinada'*.  
> *(Pressione Enter)*  
> Perfeito! O assistente agora encontrou imediatamente a orientação com sucesso, comprovando a flexibilidade e o dinamismo da nossa base de conhecimento!"

#### 7. `historico.json`, CSV e indicadores do teste com usuários (~45s)
*(Ação na tela: Mostrar a opção 3 no menu do assistente, depois abrir `data/historico.json` e `data/atendimentos.csv`).*
> **[Integrante 3 falando]:**  
> "Vamos agora analisar a persistência de dados e as métricas.  
> No menu principal, seleciono a opção 3: 'Ver indicadores'.  
> Realizamos um teste de usabilidade com **3 pessoas de fora da equipe**, somando **12 atendimentos reais**.  
> Nossos indicadores consolidados foram:  
> - **Resposta encontrada:** 91.7%  
> - **Taxa de acerto:** 91.7%  
> - **Tempo médio de busca:** 2.2 segundos  
> - **Tentativas por atendimento:** 1.1  
> - **Facilidade de uso média:** 4.7 de 5 estrelas.  
> 
> A única dúvida sem solução foi sobre 'certificado de reservista militar', que serviu de insumo para futuras melhorias.  
> Toda essa trilha é salva automaticamente em `data/historico.json` com data, pergunta, id da resposta, status e tempo. Ao sair do programa ou escolher a opção 4, todos esses registros são exportados para `data/atendimentos.csv` utilizando `csv.DictWriter`, conforme ensinado na aula."

#### 8. Decisão técnica e limitação do assistente (~30s)
> **[Integrante 3 falando]:**  
> "Para finalizar:  
> - **Nossa principal decisão técnica:** Foi adotar uma arquitetura estritamente modular com separação de responsabilidades e tolerância a falhas nos arquivos JSON, garantindo que o programa nunca trave se a base estiver ausente ou corrompida.  
> - **Principal limitação:** A inteligência do assistente é orientada a regras léxicas e palavras-chave. Ele não possui processamento de linguagem natural neural; logo, se o cidadão fizer uma pergunta com gírias ou analogias sem palavras-chave cadastradas, o assistente precisará que a base seja enriquecida manualmente.  
> Muito obrigado pela atenção de todos!"

---

## 💡 Dicas de Sucesso para a Gravação
- **Cronômetro:** Deixem um cronômetro rodando no celular para não ultrapassar 8 minutos e não fazer menos de 5 minutos.
- **Transição de voz:** Façam transições naturais (ex: *"Passo agora a palavra para o [Integrante 2], que vai explicar o algoritmo de busca e rodar o programa"*).
- **Upload:** Ao subir no YouTube, configurem a visibilidade como **Não listado** (Unlisted). Não deixem privado, senão o professor não conseguirá avaliar!
