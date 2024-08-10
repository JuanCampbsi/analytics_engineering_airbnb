### Data Engineering and Quality Assurance on the Airbnb Dataset in Rio de Janeiro

This project leverages advanced tools such as dbt, Great Expectations, Python, and Pandas to explore, transform, and validate the "Inside Airbnb" dataset. The dataset, extracted from "http://insideairbnb.com/", provides rich information on accommodation listings, guest reviews, and calendar availability in several global cities, including Rio de Janeiro.

The central goal of this project is to transform and model this data for deeper analysis, ensuring its quality and integrity. With the help of dbt, we perform data transformations and modeling, making it ready for analysis and reporting. Pandas and Python are used for preliminary manipulation and cleaning.

To ensure data quality, we have integrated Great Expectations, which allows you to create and run data quality tests. This set of tools ensures that the information is consistent, reliable, and ready for valuable insights into the accommodation market in the featured cities.

### Postgres

Installation

```bash
%sh
Download https://www.docker.com/get-started/
```

To start the container, you need to have the file, `docker-compose.yml`.

```bash
%sh
docker compose up
```

After that, you need to create a `.ENV` file in the root of the project, and put your keys for the container to work correctly.
NOTE: There is an example file called `EXAMPLE_ENV`, just rename the file to its proper `.ENV` format.

```bash
%sh
DATABASE_USER=YOUR_DATABASE_USER
DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD
POSTGRES_USER=YOUR_POSTGRES_USER
POSTGRES_PASSWORD=YOUR_POSTGRES_PASSWORD
POSTGRES_DB=YOUR_POSTGRES_DB

```

<summary><h2>Creating environment variables - ENV</h3></summary>

Using .env files in Python is a common practice to store sensitive information or settings that should not be hard-coded into your source code. In this project we are using the python-dotenv library to load environment variables from a .env file.

```bash
API_KEY= YOUR_API_KEY_HERE

```

<summary><h2>Execution with Virtual Environment</h2></summary>

<details>
<summary><h3>Linux and MacOs</h3></summary>

## Install virtualenv

To install `virtualenv`, open the terminal and run the following command:

```bash
pip install virtualenv
```

## Creating and Activating a Virtual Environment

Open the terminal and navigate to the root directory of the project, there create the environment with the following command:

```bash
virtualenv venv
```

Now activate your virtual environment:

```bash
source venv/bin/activate
```

## Installing the necessary tools:

Now you can, still in the root folder, install the necessary tools to run the application using the file requirements.txt:

```bash
pip install -r requirements.txt
```

## Deactivating the virtual environment:

To deactivate your virtual environment, simply run the following command:

```bash
deactivate
```

</details>

<details>
<summary><h3>Windows</h3></summary>

## Install virtualenv

To install `virtualenv`, open the Command Prompt or PowerShell as administrator and run the following command:

```bash
pip install virtualenv
```

## Creating and Activating a Virtual Environment

Open the Command Prompt or PowerShell and navigate to the root directory of the project, there create the environment with the following command:

```bash
virtualenv venv
```

Now activate your virtual environment:

```bash
venv/bin/activate
```

## Installing the tools required:

Now you can, still in the root folder, install the tools required to run the application using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Deactivating the virtual environment:

To deactivate your virtual environment, simply run the following command:

```bash
deactivate
