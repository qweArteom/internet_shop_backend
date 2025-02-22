from sqlalchemy import Table, ForeignKey, Column

from src.database.base import Base


rev_prod_assoc = Table(
    "rev_prod_assoc",
    Base.metadata,
    Column("review_id", ForeignKey("reviews.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)


usre_prod_cart_assoc = Table(
    "user_prod_cart_assoc",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("products_id", ForeignKey("products.id"), primary_key=True)
)


user_shop_list_assoc = Table(
    "user_shop_list_asooc",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("shop_list_id", ForeignKey("shop_list.id"), primary_key=True)
)


shop_list_prod_assoc = Table(
    "shop_list_prod_assoc",
    Base.metadata,
    Column("shop_list_id", ForeignKey("shop_list.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)