import sys
import os

# Добавляем корень проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.config.db import Base, engine
from app.models.term import Term
from app.models.pricing import Pricing
from app.models.shared_bid import SharedBid
from app.models.ready_event import ReadyEvent

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

print("✅ DB initialized.")