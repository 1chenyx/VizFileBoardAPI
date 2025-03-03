# 接口服务
from fastapi import FastAPI

from app.database import create_all_tables
from app.user_app import routers as user_routers
from app.Cost_app import routers as cost_routers
from app.file_manage import routers as file_routers



app = FastAPI()
# 初始化表
create_all_tables()

# app.include_router(
#     router=user_routers.router, tags=["auth"]
#
# )
# app.include_router(
#     router=cost_routers.router, tags=["cost"]
# )
app.include_router(
    router=file_routers.router, tags=["file"]
)
if __name__ =='__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=15001, reload=True)


