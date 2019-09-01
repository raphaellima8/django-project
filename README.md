# Eventex

Sistema de Eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/raphaellima8/django-project.svg?branch=develop)](https://travis-ci.org/raphaellima8/django-project)
[![Maintainability](https://api.codeclimate.com/v1/badges/11f55debfb7a35c6fd05/maintainability)](https://codeclimate.com/github/raphaellima8/django-project/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/11f55debfb7a35c6fd05/test_coverage)](https://codeclimate.com/github/raphaellima8/django-project/test_coverage)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.7.4
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:raphaellima8/django-project.git django-project
cd django-project
python -m venv .django-app
source .django-app/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```


## Como fazer o deploy?

1. Crie um instância no heroku.
2. Envie as configuraçōes para o heroku.
3. Define una SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku develop --force
```