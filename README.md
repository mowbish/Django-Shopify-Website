# onlineshop

The Onlineshop is a virtual store on the Internet where customers can browse the catalog and select products of
interest. The selected items may be collected in a shopping cart. At checkout time, the items in the shopping cart will
be presented as an order. At that time, more information will be needed to complete the transaction.

[![Python Version](https://img.shields.io/badge/python-3.9.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2.7-brightgreen.svg)](https://djangoproject.com)


# Purpose of system

The Onlineshop is a virtual store on the Internet where customers can browse the catalog and select products of
interest. The selected items may be collected in a shopping cart. At checkout time, the items in the shopping cart will
be presented as an order. At that time, more information will be needed to complete the transaction. Usually, the
customer will be asked to fill or select a billing address, a shipping address, a shipping option, and payment
information such as a credit card number.

The Onlineshop is expanded permanently through new products and services to offer a product portfolio corresponding to
the market. Private customers and business customers can order the selected products of the Online service online
quickly and comfortably.

# Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/mowbish/shopify.git
```

Install the requirements:

```bash
pip install -r requirements.txt --user
```

Create the database:

```bash
python manage.py makemigrations
```

Transfer rows and columns to database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at [**localhost:8000**](127.0.0.1:8000).

# Hint
you can create superuser and do some works with it:
```bash
python manage.py createsuperuser
```

fill needed data and the go to the:
```bash
localhost:8000/admin
```
well down you are now in superuser panel

#if some errors in linux
if you got an error on "psycopg2" installing in debian base distros
 you should enter in terminal:

```commandline
sudo apt-get install libpq-dev
```

and then
```commandline
pip install psycopg2
```