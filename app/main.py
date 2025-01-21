from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 주식 매매 요청 데이터 모델
class TradeRequest(BaseModel):
    stock_code: str # 주식 종목 코드 (6자리)
    action: str # buy or sell
    quantity: int
    price: int # 매수가 / 매도가 (1주당 가격)

trades = []

def validate_tick_size(price: int):
    if price < 1000 and price % 1 != 0:
        return False
    elif 1000 <= price < 10000 and price % 5 != 0:
        return False
    elif 10000 <= price < 100000 and price % 10 != 0:
        return False
    elif price >= 100000 and price % 100 != 0:
        return False
    return True

# 주문 등록 API
@app.post("/trade/")
async def place_trade(trade: TradeRequest):
    if trade.action not in {"buy", "sell"}:
        raise HTTPException(status_code=400, detail="Action must be 'buy' or 'sell'")

    if trade.quantity <= 0 or trade.price <= 0:
        raise HTTPException(status_code=400, detail="Quantity and price must be positive")

    if not validate_tick_size(trade.price):
        raise HTTPException(status_code=400, detail="Invalid tick size for the price range")

    trades.append(trade)
    return {
        "message": "Trade executed successfully", 
        "trade_details": trade,
    }

@app.get("/trades/")
async def get_trades():
    return {"total_trades": len(trades), "trades": trades}

@app.get("/")
async def root():
    return {"message": "한국 주식 매매 API가 실행 중입니다!"}