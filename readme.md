# Motor de Insights de Produto via Análise de Reviews

## 📜 Descrição do Projeto

Este projeto consiste no desenvolvimento de um produto de dados completo com o objetivo de coletar, processar e analisar automaticamente milhares de reviews de clientes sobre um produto fictício (ou um produto real específico). A partir dessa análise, o sistema gera insights valiosos sobre o sentimento dos clientes, identifica as principais queixas e aponta sugestões de melhoria, auxiliando na tomada de decisão estratégica para o produto.

Foi implementado um pipeline de dados que abrange desde a ingestão e tratamento dos dados até seu armazenamento e visualização, aplicando conceitos de arquitetura de dados para facilitar a análise exploratória e a extração de conhecimento.

## ✨ Objetivos Principais

* Coletar reviews de produtos de fontes online (via web scraping ou datasets públicos).
* Realizar o pré-processamento e limpeza dos textos dos reviews utilizando técnicas de Processamento de Linguagem Natural (NLP).
* Analisar o sentimento expresso em cada review (positivo, negativo, neutro).
* Identificar os tópicos mais frequentes, principais queixas e sugestões de melhoria mencionadas pelos clientes.
* Estruturar um pipeline de dados para a ingestão, tratamento e armazenamento dos dados e insights gerados.
* Visualizar os insights de forma clara e acionável.

## 🛠️ Tecnologias Utilizadas

* **Linguagem de Programação:** Python
* **Coleta de Dados:** `Requests`, `Beautiful Soup 4` (ou `Scrapy`, `Selenium`)
* **Manipulação e Análise de Dados:** `Pandas`, `NumPy`
* **Processamento de Linguagem Natural (NLP):** `NLTK` e/ou `spaCy`
    * Para tarefas como: tokenização, remoção de stopwords, lematização/stemming, análise de sentimento, extração de entidades, etc.
* **Armazenamento de Dados:** `SQLServer`
* **Visualização de Dados:** `Matplotlib`, `Seaborn`, e `Power BI`

## 📊 Pipeline de Dados e Metodologia

1.  **Coleta de Dados:**
    * Os reviews foram coletados do site X utilizando a biblioteca `Beautiful Soup` para parsing HTML e `Requests` para requisições HTTP.
2.  **Pré-processamento e Limpeza de Dados:**
    * Remoção de caracteres especiais, links, e informações irrelevantes.
    * Conversão para minúsculas.
    * Tokenização dos textos.
    * Remoção de stopwords (palavras comuns como "o", "a", "de").
    * Lematização ou Stemming para reduzir palavras à sua forma raiz.
3.  **Análise de Sentimento:**
    * Utilização de bibliotecas como NLTK Vader ou um modelo treinado para classificar o sentimento de cada review como positivo, negativo ou neutro.
4.  **Extração de Tópicos e Queixas Principais:**
    * Aplicação de técnicas como TF-IDF para identificar palavras-chave importantes, e/ou modelagem de tópicos (LDA) para agrupar reviews por assuntos. ou Extração de substantivos e adjetivos frequentes associados a sentimentos negativos para identificar queixas.
5.  **Armazenamento de Dados:**
    * Os dados processados e os insights gerados foram armazenados em arquivos CSV e/ou em um banco de dados SQLServer simulando um ambiente de produção.
6.  **Visualização e Geração de Insights:**
    * Criação de gráficos e dashboards utilizando Matplotlib/Seaborn (ou Power BI) para apresentar a distribuição de sentimentos, os tópicos mais discutidos, as principais queixas e sugestões de melhoria de forma visual e compreensível.

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://docs.github.com/articles/referencing-and-citing-content](https://docs.github.com/articles/referencing-and-citing-content)
    cd [nome-do-repositorio]
    ```
2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Baixe os recursos do NLTK/spaCy (se necessário):**
    ```python
    # Exemplo para NLTK:
    # import nltk
    # nltk.download('stopwords')
    # nltk.download('punkt')
    # nltk.download('wordnet')
    # nltk.download('vader_lexicon')

    # Exemplo para spaCy (após instalar o spaCy):
    # python -m spacy download en_core_web_sm  (ou pt_core_news_sm para português)
    ```
    (Adicione instruções específicas aqui conforme as bibliotecas que usar)

5.  **Execute os notebooks ou scripts principais:**
    * [Ex: "Abra e execute os Jupyter Notebooks na pasta `notebooks/` na ordem numérica." ou "Execute o script principal: `python src/main.py`"]

## 🎯 Resultados e Insights Gerados (Exemplos)

* Distribuição geral do sentimento dos clientes (e.g., 60% Positivo, 30% Negativo, 10% Neutro).
* Principais termos/tópicos associados a reviews negativos (e.g., "bateria fraca", "tela arranhada", "atendimento ruim").
* Sugestões de melhoria mais frequentes extraídas dos reviews (e.g., "aumentar duração da bateria", "melhorar embalagem").
* Comparação de sentimento ou tópicos ao longo do tempo (se houver dados de data).

_(Adicione aqui alguns exemplos dos insights que seu projeto conseguiu gerar. Se puder, inclua pequenas imagens de gráficos)_

## 🔮 Próximos Passos e Melhorias Futuras

* Implementar um dashboard interativo com `Streamlit`.
* Treinar um modelo de classificação de sentimento customizado para o domínio específico do produto.
* Aplicar técnicas mais avançadas de modelagem de tópicos (e.g., BERTopic).
* Automatizar o pipeline de coleta e análise para rodar periodicamente.
* Expandir a análise para incluir a identificação de *aspectos* do produto e o sentimento associado a cada aspecto (Aspect-Based Sentiment Analysis).

## ✍️ Autor

* **Matheus Vieira**
* **LinkedIn:** [linkedin.com/in/mathsv]
* **GitHub:** [github.com/mathsv]

## 📄 Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo `LICENSE.md` para detalhes (opcional, mas bom para projetos públicos).