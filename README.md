# foodsoftstats

More insight into the Foodsoft database. The approach here is (because we're not Ruby programmers) that we're doing a MySQL database dump of the Foodsoft database (live @ [foodsoft.biobulkbende.org](https://foodsoft.biobulkbende.org)) and then loading that dump locally. Then, using [sqlacodegen](https://github.com/agronholm/sqlacodegen) to generate Python-based API bindings so we can write scripts to learn more about what is happening in the database (e.g. what products from which suppliers were never ordered?).

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
