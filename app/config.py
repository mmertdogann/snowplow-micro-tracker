"""Snowplow tracker configuration."""
import datetime
import uuid

from .models import Basket
from snowplow_tracker import Subject, Tracker, Emitter

e = Emitter("localhost:9090")
t = Tracker(e)
s = Subject()

s.set_lang('en')

"""App configuration."""
CATEGORIES = [
    "Electronics",
    "Clothes",
    "Shoes",
    "House",
    "Arts",
]

basket = Basket()
