# Teste de Automacao - API e Web

Projeto de automacao de testes com duas suites no mesmo repositorio:

- Testes de API na Swagger Petstore.
- Teste E2E Web no SauceDemo.

O objetivo e validar fluxos principais de API e um fluxo funcional de compra no site, usando boas praticas como Page Objects, separacao de responsabilidades, assercoes claras e execucao automatica em pipeline.

## Tecnologias Utilizadas

- Python
- Pytest
- Requests
- Selenium WebDriver
- Google Chrome
- GitHub Actions

## Estrutura do Projeto

```text
api_tests/
  services/      Cliente da API Petstore
  tests/         Testes dos recursos User, Pet e Store
  utils/         Geracao de dados dinamicos

web_tests/
  pages/         Page Objects do SauceDemo
  tests/         Teste E2E de checkout
  drivers/       Dependencias da automacao web

.github/
  workflows/     Pipeline de CI
```

## Pre-requisitos

Antes de rodar o projeto, instale:

- Python 3.11 ou superior
- Google Chrome
- Git

O ChromeDriver e gerenciado automaticamente pelo Selenium. Caso o Selenium nao consiga localizar ou baixar o driver, rode novamente com internet ativa.

## Instalacao

Clone o repositorio:

```bash
git clone https://github.com/eduardoesn/teste_automacao.git
cd teste_automacao
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Tambem e possivel instalar as dependencias separadamente:

```bash
pip install -r api_tests/requirements.txt
pip install -r web_tests/drivers/requirements.txt
```

## Como Rodar os Testes

Rodar todos os testes:

```bash
pytest api_tests web_tests
```

Rodar apenas os testes de API:

```bash
pytest api_tests
```

Rodar apenas o teste Web:

```bash
pytest web_tests
```

Para executar o teste Web com o navegador visivel:

```bash
$env:HEADLESS="false"
pytest web_tests
```

Se tiver definido um caminho incorreto para `CHROME_DRIVER_PATH`, limpe a variavel antes de rodar:

```bash
Remove-Item Env:CHROME_DRIVER_PATH
pytest web_tests
```

## Cenarios Automatizados

### API - Swagger Petstore

Base URL:

```text
https://petstore.swagger.io/v2
```

Cenarios cobertos:

- Criar, consultar, atualizar e excluir usuario.
- Criar, consultar, atualizar e excluir pet.
- Buscar pets por status.
- Criar, consultar e excluir pedido.
- Consultar inventario da loja.

### Web - SauceDemo

URL:

```text
https://www.saucedemo.com/
```

Fluxo coberto:

- Acessar o site.
- Realizar login com usuario valido.
- Adicionar dois produtos ao carrinho.
- Validar os itens adicionados.
- Preencher dados do checkout.
- Finalizar a compra.
- Validar mensagem de sucesso.

## Evidencias

O teste Web salva screenshot ao final do fluxo em:

```text
artifacts/screenshots/checkout-completo.png
```

## Pipeline CI

A pipeline esta configurada em:

```text
.github/workflows/pipeline.yml
```

Ela roda automaticamente em `push`, `pull_request` e tambem pode ser executada manualmente pelo GitHub Actions.

Jobs configurados:

- `api-tests`: instala dependencias da API e executa `pytest api_tests -v`.
- `web-tests`: instala dependencias Web, prepara o Chrome e executa `pytest web_tests -v`.

## Observacoes

- O teste Web usa Page Objects para organizar as interacoes com as paginas.
- Os dados da API sao gerados dinamicamente para evitar conflito entre execucoes.
- O Chrome e configurado para nao exibir alertas de senha durante a automacao.
