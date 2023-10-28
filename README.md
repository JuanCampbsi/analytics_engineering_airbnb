
### Engenharia de Dados e Garantia de Qualidade no Conjunto de Dados do Airbnb no Rio de Janeiro
Integrantes:
Juan Campos,
Rafael Gomes,
Marcelo Dias,
Jonatha Leôncio.

Este projeto faz uso de ferramentas avançadas como dbt, Great Expectations, Python e Pandas para explorar, transformar e validar o conjunto de dados "Inside Airbnb". O dataset, extraído de "http://insideairbnb.com/", fornece informações ricas sobre listagens de hospedagens, avaliações de hóspedes e disponibilidades de calendário em diversas cidades globais, incluindo o Rio de Janeiro.

O objetivo central deste projeto é transformar e modelar esses dados para análises mais profundas, garantindo sua qualidade e integridade. Com a ajuda do dbt, realizamos transformações e modelagens de dados, tornando-os prontos para análises e relatórios. Pandas e Python são utilizados para manipulação e limpeza preliminares.

Para assegurar a qualidade dos dados, integramos o Great Expectations, que permite criar e executar testes de qualidade de dados. Este conjunto de ferramentas garante que as informações são consistentes, confiáveis e prontas para insights valiosos sobre o mercado de hospedagem nas cidades em destaque.


### Postgres 

Instalação

```bash
    %sh 
    Download https://www.docker.com/get-started/
```


Para subir o contêiner é preciso ter o arquivo, `docker-compose.yml`.

```bash
    %sh 
    docker compose up
```

Após isso, é preciso criar um arquivo `.ENV` na raiz do projeto, e colocar suas chaves para o correto funcionamento do contêiner.
OBS: Existe um arquivo de exemplo chamado `EXAMPLE_ENV`, basta renomear o arquivo para o seu devido formato `.ENV`.

```bash
    %sh 
    DATABASE_USER=YOUR_DATABASE_USER
    DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD
    POSTGRES_USER=YOUR_POSTGRES_USER
    POSTGRES_PASSWORD=YOUR_POSTGRES_PASSWORD
    POSTGRES_DB=YOUR_POSTGRES_DB

```

<summary><h2>Criando váriaveis de ambiente - ENV</h3></summary>

Usar arquivos .env em Python é uma prática comum para armazenar informações sensíveis ou configurações que não devem ser codificadas diretamente em seu código fonte. Nesse projeto estamos usando biblioteca python-dotenv para carregar variáveis de ambiente de um arquivo .env.

```bash
API_KEY= SUA_CHAVE_DE_API_AQUI

```

<summary><h2>Execução com Ambiente Virtual</h2></summary>

<details>
<summary><h3>Linux e MacOs</h3></summary>

## Instale o virtualenv

Para instalar o `virtualenv`, abra o terminal e execute o seguinte comando:

```bash
pip install virtualenv
```

## Criação e Ativação de um Ambiente Virtual

Abra o terminal e navegue até o diretório raiz do projeto, lá crie o ambiente com o seguinte comando:

```bash
virtualenv venv
```

Agora ative seu ambiente virtual:

```bash
source venv/bin/activate
```

## Instlação das ferraments necessárias:

Agora você pode, ainda na pasta raiz, instalar as ferramentas necessárias para rodar a aplicação usando o arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

## Desativação do ambiente virtual:

Para desativar seu ambiente virtual, basta executar o seguinte comando:

```bash
deactivate
```

</details>

<details>
<summary><h3>Windows</h3></summary>

## Instale o virtualenv

Para instalar o `virtualenv`, abra o Prompt de Comando ou PowerShell como administrador e execute o seguinte comando:

```bash
pip install virtualenv
```

## Criação e Ativação de um Ambiente Virtual

Abra o Prompt de Comando ou PowerShell e navegue até o diretório raiz do projeto, lá crie o ambiente com o seguinte comando:

```bash
virtualenv venv
```

Agora ative seu ambiente virtual:

```bash
venv/bin/activate
```

## Instlação das ferraments necessárias:

Agora você pode, ainda na pasta raiz, instalar as ferramentas necessárias para rodar a aplicação usando o arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

## Desativação do ambiente virtual:

Para desativar seu ambiente virtual, basta executar o seguinte comando:

```bash
deactivate
