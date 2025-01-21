# 데이터베이스 설정
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 비동기 엔진 생성
# engine: AsyncEngine = create_async_engine(
#     DATABASE_URL,
#     echo=True,
# )

DATABASE_URL = "mysql+asyncmy://root:1234@localhost:3310/stock_db"
engine = create_async_engine(DATABASE_URL, echo=True)

# 세션 팩토리 생성
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# 베이스 클래스 생성
Base = declarative_base()

# DB 세션 의존성
async def get_db():
    async with async_session() as session:
        yield session
