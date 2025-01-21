# 데이터베이스 모델 정의

from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from app.core.db import Base
import enum
from datetime import datetime

class TradeAction(str, enum.Enum):
    buy = "buy"
    sell = "sell"

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    stock_code = Column(String(6), index=True, nullable=False)
    action = Column(Enum(TradeAction), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.now, nullable=False)