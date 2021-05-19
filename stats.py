from os import environ
from sys import exit

from bindings import Article, GroupOrder, Order, OrderArticle, Supplier
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def never_ordered(session):
    """List all articles never ordered by supplier."""

    suppliers = session.query(Supplier)
    order_articles = session.query(OrderArticle)
    articles = session.query(Article)

    ordered_articles = []

    for order in session.query(Order).all():
        supplier = suppliers.filter(Supplier.id == order.supplier_id).first()

        if not supplier:
            continue

        all_order_articles = order_articles.filter(
            OrderArticle.order_id == order.id
        ).all()

        for order_article in all_order_articles:
            if not order_article.units_received:
                continue

            if order_article.article_id not in ordered_articles:
                ordered_articles.append(order_article.article_id)

    never_ordered = articles.filter(Article.id.notin_(ordered_articles)).all()

    suppliers_articles = {}
    for article in never_ordered:
        supplier = suppliers.filter(Supplier.id == article.supplier_id).first()

        if supplier.name not in suppliers_articles:
            suppliers_articles[supplier.name] = []

        suppliers_articles[supplier.name].append(article)

    for supplier in suppliers_articles:
        articles = suppliers_articles[supplier]
        articles.sort(key=lambda a: a.created_at, reverse=True)

        if not articles:
            continue

        print(f"Supplier: {supplier}, # articles never ordered: {len(articles)}")

        for artc in articles:
            print(f"Article: {artc.name}, Added {artc.created_at}")

        print("")


DB_USER = environ.get("DB_USER", "root")
DB_PASSWORD = environ.get("DB_PASSWORD")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = environ.get("DB_NAME", "foodsoft")

if not DB_PASSWORD:
    exit("Please set a DB_PASSWORD env var")

connection = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
session = Session(create_engine(connection))

never_ordered(session)
