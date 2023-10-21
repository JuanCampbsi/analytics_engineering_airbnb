### Projeto: Engenharia de Dados e Garantia de Qualidade no Conjunto de Dados do Airbnb no Rio de Janeiro

O conjunto de dados "Inside Airbnb", disponível no website "http://insideairbnb.com/", é uma valiosa fonte de informações sobre listagens de hospedagem, avaliações de hóspedes e disponibilidade de calendário em várias cidades ao redor do mundo, incluindo o Rio de Janeiro. Antes de prosseguirmos com a engenharia de dados, é importante entender os principais componentes deste conjunto de dados:

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
