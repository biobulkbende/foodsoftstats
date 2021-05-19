"""Sqlacodegen generated Python bindings for the Foodsoft database schema."""

from sqlalchemy import (
    DECIMAL,
    Column,
    Date,
    DateTime,
    Float,
    Index,
    LargeBinary,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ArticleCategory(Base):
    __tablename__ = "article_categories"

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False, unique=True, server_default=text("''"))
    description = Column(String(255))


class ArticlePrice(Base):
    __tablename__ = "article_prices"

    id = Column(INTEGER(11), primary_key=True)
    article_id = Column(INTEGER(11), index=True)
    price = Column(DECIMAL(8, 2), nullable=False, server_default=text("0.00"))
    tax = Column(DECIMAL(8, 2), nullable=False, server_default=text("0.00"))
    deposit = Column(DECIMAL(8, 2), nullable=False, server_default=text("0.00"))
    unit_quantity = Column(INTEGER(11))
    created_at = Column(DateTime)


class Article(Base):
    __tablename__ = "articles"
    __table_args__ = (
        Index("index_articles_on_name_and_supplier_id", "name", "supplier_id"),
    )

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False, server_default=text("''"))
    supplier_id = Column(
        INTEGER(11), nullable=False, index=True, server_default=text("0")
    )
    article_category_id = Column(
        INTEGER(11), nullable=False, index=True, server_default=text("0")
    )
    unit = Column(String(255), nullable=False, server_default=text("''"))
    note = Column(String(255))
    availability = Column(TINYINT(1), nullable=False, server_default=text("1"))
    manufacturer = Column(String(255))
    origin = Column(String(255))
    shared_updated_on = Column(DateTime)
    price = Column(DECIMAL(8, 2))
    tax = Column(Float)
    deposit = Column(DECIMAL(8, 2), server_default=text("0.00"))
    unit_quantity = Column(INTEGER(11), nullable=False, server_default=text("1"))
    order_number = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    type = Column(String(255), index=True)
    quantity = Column(INTEGER(11), server_default=text("0"))


class Assignment(Base):
    __tablename__ = "assignments"
    __table_args__ = (
        Index(
            "index_assignments_on_user_id_and_task_id",
            "user_id",
            "task_id",
            unique=True,
        ),
    )

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(INTEGER(11), nullable=False, server_default=text("0"))
    task_id = Column(INTEGER(11), nullable=False, server_default=text("0"))
    accepted = Column(TINYINT(1), server_default=text("0"))


class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(INTEGER(11), primary_key=True)
    supplier_id = Column(INTEGER(11), index=True)
    delivered_on = Column(Date)
    created_at = Column(DateTime)
    note = Column(Text)
    invoice_id = Column(INTEGER(11))


class Document(Base):
    __tablename__ = "documents"

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    mime = Column(String(255))
    data = Column(LargeBinary)
    created_by_user_id = Column(INTEGER(11))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class FinancialLink(Base):
    __tablename__ = "financial_link"

    id = Column(INTEGER(11), primary_key=True)
    note = Column(Text)


class FinancialTransaction(Base):
    __tablename__ = "financial_transactions"

    id = Column(INTEGER(11), primary_key=True)
    ordergroup_id = Column(
        INTEGER(11), nullable=False, index=True, server_default=text("0")
    )
    amount = Column(DECIMAL(8, 2), nullable=False, server_default=text("0.00"))
    note = Column(Text, nullable=False)
    user_id = Column(INTEGER(11), nullable=False, server_default=text("0"))
    created_on = Column(DateTime, nullable=False)
    financial_link_id = Column(INTEGER(11))


class GroupOrderArticleQuantity(Base):
    __tablename__ = "group_order_article_quantities"

    id = Column(INTEGER(11), primary_key=True)
    group_order_article_id = Column(
        INTEGER(11), nullable=False, index=True, server_default=text("0")
    )
    quantity = Column(INTEGER(11), server_default=text("0"))
    tolerance = Column(INTEGER(11), server_default=text("0"))
    created_on = Column(DateTime, nullable=False)


class GroupOrderArticle(Base):
    __tablename__ = "group_order_articles"
    __table_args__ = (
        Index("goa_index", "group_order_id", "order_article_id", unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    group_order_id = Column(
        INTEGER(11), nullable=False, index=True, server_default=text("0")
    )
    order_article_id = Column(
        INTEGER(11), nullable=False, index=True, server_default=text("0")
    )
    quantity = Column(INTEGER(11), nullable=False, server_default=text("0"))
    tolerance = Column(INTEGER(11), nullable=False, server_default=text("0"))
    updated_on = Column(DateTime, nullable=False)
    result = Column(DECIMAL(8, 3))
    result_computed = Column(DECIMAL(8, 3))


class GroupOrder(Base):
    __tablename__ = "group_orders"
    __table_args__ = (
        Index(
            "index_group_orders_on_ordergroup_id_and_order_id",
            "ordergroup_id",
            "order_id",
            unique=True,
        ),
    )

    id = Column(INTEGER(11), primary_key=True)
    ordergroup_id = Column(INTEGER(11), index=True)
    order_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("0"))
    price = Column(DECIMAL(8, 2), nullable=False, server_default=text("0.00"))
    lock_version = Column(INTEGER(11), nullable=False, server_default=text("0"))
    updated_on = Column(DateTime, nullable=False)
    updated_by_user_id = Column(INTEGER(11))


class Group(Base):
    __tablename__ = "groups"

    id = Column(INTEGER(11), primary_key=True)
    type = Column(String(255), nullable=False, server_default=text("''"))
    name = Column(String(255), nullable=False, unique=True, server_default=text("''"))
    description = Column(String(255))
    account_balance = Column(
        DECIMAL(12, 2), nullable=False, server_default=text("0.00")
    )
    created_on = Column(DateTime, nullable=False)
    role_admin = Column(TINYINT(1), nullable=False, server_default=text("0"))
    role_suppliers = Column(TINYINT(1), nullable=False, server_default=text("0"))
    role_article_meta = Column(TINYINT(1), nullable=False, server_default=text("0"))
    role_finance = Column(TINYINT(1), nullable=False, server_default=text("0"))
    role_orders = Column(TINYINT(1), nullable=False, server_default=text("0"))
    deleted_at = Column(DateTime)
    contact_person = Column(String(255))
    contact_phone = Column(String(255))
    contact_address = Column(String(255))
    stats = Column(Text)
    next_weekly_tasks_number = Column(INTEGER(11), server_default=text("8"))
    ignore_apple_restriction = Column(TINYINT(1), server_default=text("0"))
    role_invoices = Column(TINYINT(1), nullable=False, server_default=text("0"))
    break_start = Column(Date)
    break_end = Column(Date)


class Invite(Base):
    __tablename__ = "invites"

    id = Column(INTEGER(11), primary_key=True)
    token = Column(String(255), nullable=False, index=True, server_default=text("''"))
    expires_at = Column(DateTime, nullable=False)
    group_id = Column(INTEGER(11), nullable=False, server_default=text("0"))
    user_id = Column(INTEGER(11), nullable=False, server_default=text("0"))
    email = Column(String(255), nullable=False, server_default=text("''"))


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(INTEGER(11), primary_key=True)
    supplier_id = Column(INTEGER(11), index=True)
    number = Column(String(255))
    date = Column(Date)
    paid_on = Column(Date)
    note = Column(Text)
    amount = Column(DECIMAL(8, 2), nullable=False, server_default=text("0.00"))
    deposit = Column(DECIMAL(8, 2), nullable=False, server_default=text("0.00"))
    deposit_credit = Column(DECIMAL(8, 2), nullable=False, server_default=text("0.00"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    created_by_user_id = Column(INTEGER(11))
    attachment_mime = Column(String(255))
    attachment_data = Column(LargeBinary)
    financial_link_id = Column(INTEGER(11))


class MailDeliveryStatu(Base):
    __tablename__ = "mail_delivery_status"

    id = Column(INTEGER(11), primary_key=True)
    created_at = Column(DateTime)
    email = Column(String(255), nullable=False, index=True)
    message = Column(String(255), nullable=False)
    attachment_mime = Column(String(255))
    attachment_data = Column(LargeBinary)


class Membership(Base):
    __tablename__ = "memberships"
    __table_args__ = (
        Index(
            "index_memberships_on_user_id_and_group_id",
            "user_id",
            "group_id",
            unique=True,
        ),
    )

    id = Column(INTEGER(11), primary_key=True)
    group_id = Column(INTEGER(11), nullable=False, server_default=text("0"))
    user_id = Column(INTEGER(11), nullable=False, server_default=text("0"))


class Message(Base):
    __tablename__ = "messages"

    id = Column(INTEGER(11), primary_key=True)
    sender_id = Column(INTEGER(11))
    recipients_ids = Column(Text)
    subject = Column(String(255), nullable=False)
    body = Column(Text)
    email_state = Column(INTEGER(11), nullable=False, server_default=text("0"))
    private = Column(TINYINT(1), server_default=text("0"))
    created_at = Column(DateTime)
    reply_to = Column(INTEGER(11))
    group_id = Column(INTEGER(11))
    salt = Column(String(255))
    received_email = Column(LargeBinary)


class OrderArticle(Base):
    __tablename__ = "order_articles"
    __table_args__ = (
        Index(
            "index_order_articles_on_order_id_and_article_id",
            "order_id",
            "article_id",
            unique=True,
        ),
    )

    id = Column(INTEGER(11), primary_key=True)
    order_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("0"))
    article_id = Column(INTEGER(11), nullable=False, server_default=text("0"))
    quantity = Column(INTEGER(11), nullable=False, server_default=text("0"))
    tolerance = Column(INTEGER(11), nullable=False, server_default=text("0"))
    units_to_order = Column(INTEGER(11), nullable=False, server_default=text("0"))
    lock_version = Column(INTEGER(11), nullable=False, server_default=text("0"))
    article_price_id = Column(INTEGER(11))
    units_billed = Column(INTEGER(11))
    units_received = Column(INTEGER(11))


class OrderComment(Base):
    __tablename__ = "order_comments"

    id = Column(INTEGER(11), primary_key=True)
    order_id = Column(INTEGER(11), index=True)
    user_id = Column(INTEGER(11))
    text = Column(Text)
    created_at = Column(DateTime)


class Order(Base):
    __tablename__ = "orders"

    id = Column(INTEGER(11), primary_key=True)
    supplier_id = Column(INTEGER(11))
    note = Column(Text)
    starts = Column(DateTime)
    ends = Column(DateTime)
    state = Column(String(255), index=True, server_default=text("'open'"))
    lock_version = Column(INTEGER(11), nullable=False, server_default=text("0"))
    updated_by_user_id = Column(INTEGER(11))
    foodcoop_result = Column(DECIMAL(8, 2))
    created_by_user_id = Column(INTEGER(11))
    boxfill = Column(DateTime)
    pickup = Column(Date)
    invoice_id = Column(INTEGER(11))
    last_sent_mail = Column(DateTime)
    end_action = Column(INTEGER(11), nullable=False, server_default=text("0"))


class PageVersion(Base):
    __tablename__ = "page_versions"

    id = Column(INTEGER(11), primary_key=True)
    page_id = Column(INTEGER(11), index=True)
    lock_version = Column(INTEGER(11))
    body = Column(Text)
    updated_by = Column(INTEGER(11))
    redirect = Column(INTEGER(11))
    parent_id = Column(INTEGER(11))
    updated_at = Column(DateTime)


class Page(Base):
    __tablename__ = "pages"

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255), index=True)
    body = Column(Text)
    permalink = Column(String(255), index=True)
    lock_version = Column(INTEGER(11), server_default=text("0"))
    updated_by = Column(INTEGER(11))
    redirect = Column(INTEGER(11))
    parent_id = Column(INTEGER(11))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class PeriodicTaskGroup(Base):
    __tablename__ = "periodic_task_groups"

    id = Column(INTEGER(11), primary_key=True)
    next_task_date = Column(Date)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


t_schema_migrations = Table(
    "schema_migrations",
    metadata,
    Column("version", String(255), nullable=False, unique=True),
)


class Setting(Base):
    __tablename__ = "settings"
    __table_args__ = (
        Index(
            "index_settings_on_thing_type_and_thing_id_and_var",
            "thing_type",
            "thing_id",
            "var",
            unique=True,
        ),
    )

    id = Column(INTEGER(11), primary_key=True)
    var = Column(String(255), nullable=False)
    value = Column(Text)
    thing_id = Column(INTEGER(11))
    thing_type = Column(String(30))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class StockChange(Base):
    __tablename__ = "stock_changes"

    id = Column(INTEGER(11), primary_key=True)
    delivery_id = Column(INTEGER(11), index=True)
    order_id = Column(INTEGER(11))
    stock_article_id = Column(INTEGER(11), index=True)
    quantity = Column(INTEGER(11), server_default=text("0"))
    created_at = Column(DateTime)
    stock_taking_id = Column(INTEGER(11), index=True)


class StockTaking(Base):
    __tablename__ = "stock_takings"

    id = Column(INTEGER(11), primary_key=True)
    date = Column(Date)
    note = Column(Text)
    created_at = Column(DateTime)


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False, unique=True, server_default=text("''"))
    address = Column(String(255), nullable=False, server_default=text("''"))
    phone = Column(String(255), nullable=False, server_default=text("''"))
    phone2 = Column(String(255))
    fax = Column(String(255))
    email = Column(String(255))
    url = Column(String(255))
    contact_person = Column(String(255))
    customer_number = Column(String(255))
    delivery_days = Column(String(255))
    order_howto = Column(String(255))
    note = Column(String(255))
    shared_supplier_id = Column(INTEGER(11))
    min_order_quantity = Column(String(255))
    deleted_at = Column(DateTime)
    shared_sync_method = Column(String(255))
    iban = Column(String(255))


class Task(Base):
    __tablename__ = "tasks"

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False, index=True, server_default=text("''"))
    description = Column(String(255))
    due_date = Column(Date, index=True)
    done = Column(TINYINT(1), server_default=text("0"))
    workgroup_id = Column(INTEGER(11), index=True)
    created_on = Column(DateTime, nullable=False)
    updated_on = Column(DateTime, nullable=False)
    required_users = Column(INTEGER(11), server_default=text("1"))
    duration = Column(INTEGER(11), server_default=text("1"))
    periodic_task_group_id = Column(INTEGER(11))


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER(11), primary_key=True)
    nick = Column(String(255), unique=True)
    password_hash = Column(String(255), nullable=False, server_default=text("''"))
    password_salt = Column(String(255), nullable=False, server_default=text("''"))
    first_name = Column(String(255), nullable=False, server_default=text("''"))
    last_name = Column(String(255), nullable=False, server_default=text("''"))
    email = Column(String(255), nullable=False, unique=True, server_default=text("''"))
    phone = Column(String(255))
    created_on = Column(DateTime, nullable=False)
    reset_password_token = Column(String(255))
    reset_password_expires = Column(DateTime)
    last_login = Column(DateTime)
    last_activity = Column(DateTime)
    deleted_at = Column(DateTime)
    iban = Column(String(255))
