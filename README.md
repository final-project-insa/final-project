# KiFiSo

final project

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### How to start

-   Start locally:
        $ docker compose -f ./local.yml up

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy knl2

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
We deployed this web with WSGI (python anywhere) and another technology is AWS

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Some images of website

I have encountered a deployment issue with my website, therefore I am sharing some images with you to showcase the conception and design of this project. I will share the website link with you soon!!!

![1  Page d'accueil](https://user-images.githubusercontent.com/91082621/236629949-076579ed-28b1-419a-9c12-9d0933b39edc.png)
![2  Page about us](https://user-images.githubusercontent.com/91082621/236629970-e6547a2c-419c-4b6c-8ac2-039902c03ad1.png)
![3  Page skills](https://user-images.githubusercontent.com/91082621/236629983-b0004f8b-b85d-470f-93f2-fa8659a32c1f.png)
![4  Page our team](https://user-images.githubusercontent.com/91082621/236630039-bb3a2b23-5119-4d74-b9ba-876b238fb186.png)
![5  Page basic plan](https://user-images.githubusercontent.com/91082621/236630043-c90d7fa1-827a-4b6c-bc5d-945f59472630.png)
![6  Page company plan](https://user-images.githubusercontent.com/91082621/236630051-e4f9abec-bb02-47bb-aacc-773c980fd2f1.png)
![7  Page developer plan](https://user-images.githubusercontent.com/91082621/236630054-93d6dee9-ae2b-4f36-8177-9cb37f52fb91.png)
![8  Page details porfolio](https://user-images.githubusercontent.com/91082621/236630058-d470e403-0591-4241-84de-620896c61eaf.png)
![9  Page of payment](https://user-images.githubusercontent.com/91082621/236630062-4b18716a-ec02-4cae-a598-c0fd2a85764b.png)
![10  Sign in](https://user-images.githubusercontent.com/91082621/236630067-c86c028c-678f-4e38-aa76-75f5bd489f4d.png)
![11  Sign up](https://user-images.githubusercontent.com/91082621/236630071-72345315-3d0e-4b7c-9944-e6f70ee5f9b9.png)
![12  Page user profile](https://user-images.githubusercontent.com/91082621/236630075-423de62f-1254-40d0-a2b8-8fb178ee27f3.png)
![13  Page change user's informations](https://user-images.githubusercontent.com/91082621/236630080-8e27f383-33ef-4c83-a0cf-cbdbaf36ca08.png)
![14  Page user's email](https://user-images.githubusercontent.com/91082621/236630099-3e30724c-f870-4efb-866c-6f8baa330d63.png)
