# 데이터베이스 초기화

# app/core/init_db.py

import sys
import os

# 루트 디렉터리를 모듈 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import asyncio

async def init_models():
    from app.core.db import engine, Base
    from app.model import __all__

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_models())
    print("Database tables created successfully.")

