# foodsoftstats

More insight into the Foodsoft database.

## Hacking

Setup:

```
$ python3 -m venv .venv && source .venv/bin/activate
$ pip install -U pip setuptools -r requirements.txt
```

Import (ask on the chat for the database dump):

```
$ mysql foodsoft < 2021-05-19-foodsoft.sql
```

Run:

```
$ export DB_PASSWORD=mypassword
$ python stats.py
```

## Generate bindings

You need to have access to a database which has the Foodsoft schema loaded.

```
$ sqlacodegen "mysql+pymysql://<user>:<password>@<host>/<name>" > bindings.py
```
