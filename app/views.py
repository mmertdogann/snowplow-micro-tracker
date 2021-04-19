from flask import Blueprint, render_template, request, redirect
from .models import Item
from .config import *

views = Blueprint('views', __name__)


@views.route('/')
def root():
    return "Server is running!"


@views.route("/store", methods=["GET"])
def index():
    ts = datetime.datetime.now().timestamp()
    t.track_page_view("http://127.0.0.1:5000/store", "Store", None, None, ts)

    return render_template("store.html", categories=CATEGORIES)


@views.route("/basket", methods=["GET", "POST"])
def items():
    if request.method == "GET":
        # TODO It needs to be async. Use a broker (RabbitMQ or Kafka) push it to queue then consume.
        ts = datetime.datetime.now().timestamp()
        t.track_page_view("http://127.0.0.1:5000/basket",
                          "Basket", None, None, ts)

        return render_template("basket.html", basket=basket)

    else:
        sku = f"order-{len(basket.items) + 1}"
        name = request.form.get("name")
        price = request.form.get("price")
        quantity = request.form.get("quantity")
        category = request.form.get("category")

        if category not in CATEGORIES:
            ts = datetime.datetime.now().timestamp()
            t.track_page_view("http://127.0.0.1:5000/",
                              "Error", None, None, ts)

            return render_template("error.html", message="Invalid category")

        basket.add_to_basket(
            Item(sku, name, float(price), int(quantity), category))

        ts = datetime.datetime.now().timestamp()

        t.track_add_to_cart(sku, int(quantity), name,
                            category, float(price), "USD", None)

        print()

        if int(quantity) > 5:
            t.track_struct_event(
                category, f"More than 5 {name} added to the basket", None, name, float(price), None, ts)

        return redirect("/store")


@views.route("/purchase", methods=["GET"])
def checkout():
    order_id = uuid.uuid4()
    ts = datetime.datetime.now().timestamp()
    t.track_ecommerce_transaction(
        str(order_id), basket.total, None, None, None, None, None, None, "USD", basket.get_items(), None, ts)

    return redirect("/basket")
