# Cookiecutter Django Base Template

This is a base template for Django projects. It includes some common configurations and tools to help you get started quickly.

This template is based on a lot of good ideas and layout from the [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) project, but stripped down to the bare essentials and simplified to use as a base for any Django project.

## !!! IMPORTANT !!!

This template is designed to be used as a base for new Django projects. It does not include all the batteries! If you are looking for a full-fledged Django project template, you should consider using the [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) template instead.

## Features

- For Django >= 5.0
- Works with Python >= 3.13
- [12-Factor](https://12factor.net) based settings via [django-environ](https://github.com/joke2k/django-environ)
- Optional basic ASGI setup for Websockets
- Send emails via [Anymail](https://github.com/anymail/django-anymail) (using [Mailgun](http://www.mailgun.com/) by default or Amazon SES if AWS is selected cloud provider, but switchable)
- Media storage using Amazon S3, Google Cloud Storage, Azure Storage or nginx
- Docker support
- Run tests with unittest or pytest
- Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review
- Configuration for [Celery](https://docs.celeryq.dev) and [Flower](https://github.com/mher/flower)
- Integration with [Mailpit](https://github.com/axllent/mailpit/) for local email testing
- Integration with [Sentry](https://sentry.io/welcome/) for error logging
- Additional security configuration such as Content Security Policy (CSP) settings
- Prometheus metrics in production

## Constraints

- Uses PostgreSQL everywhere: 16+
- Only maintained 3rd party libraries are used.
- Environment variables for configuration

## Usage

First, get Cookiecutter.

```shell
pip install "cookiecutter>=1.7.0"
# If you have pipx (which is awesome) you can use:
# pipx install cookiecutter
```

Now run it against this repo:

```shell
cookiecutter https://github.com/voidrot/cookiecutter-django-base
```

You'll be prompted for some values. Provide them, then a Django project will be created for you.

Enter the project and take a look around:

```shell
cd your_project_name
ls -lah
```

Create a git repo and push it there:

```shell
git init
git add .
git commit -m "first awesome commit"
git remote add origin git@github.com:your_username/your-awesome-project.git
git push -u origin master
```

## Not Exactly What You Want?

This is what I want. _It might not be what you want._ Don't worry, you have options:

### Fork This

If you have differences in your preferred setup, I encourage you to fork this to create your own version.

### Submit a Pull Request

We accept pull requests if they're small, atomic, and make our own project development
experience better.


