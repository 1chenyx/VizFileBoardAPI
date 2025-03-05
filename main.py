# 接口服务
from fastapi import FastAPI
import argparse

import uvicorn

from GlobalParameters import global_settings
from initialization import initialization_config, initialization_db
from app.file_api.routers import router as file_router

# from app.database import create_all_tables

app = FastAPI()

app.include_router(router=file_router, tags=["file"])
def start_main():
    parser = argparse.ArgumentParser(description="启动接口")

    # 启动模式
    parser.add_argument("-m", "--mode", type=int, default="1", help="启动模式（1-本地，2-局域网，3-互联网云端）")
    # 启动接口的ip端口
    parser.add_argument("-p", "--port", type=int, default="15674", help="本地接口端口")
    # 启动接口的ip端口
    parser.add_argument("-i", "--ip", type=str, default="localhost", help="Ip地址")
    # 解析参数
    args = parser.parse_args()
    print(f"接口地址：{args.ip}:{args.port}")
    # 初始化参数
    initialization_config(args)
    # 初始化数据库
    initialization_db(args.mode)
    # 初始化表
    # create_all_tables()

    pass

if __name__ =='__main__':
    start_main()
    # 启动接口服务

    uvicorn.run('main:app', host=global_settings.webapi_ip, port=global_settings.webapi_port, reload=True)



