# 接口服务
from fastapi import FastAPI

from app.database import create_all_tables



app = FastAPI()
# 初始化表
create_all_tables()

app.include_router(
    router=file_routers.router, tags=["file"]
)
if __name__ =='__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=15001, reload=True)


