import os
import json

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

from GlobalParameters import global_settings

def initialization_config(args):
    # 配置文件路径
    config_path=os.path.join(global_settings.project_path,'./config.json')
    with open(config_path, 'r', encoding='utf-8') as config_file:
        global_settings.config_data = json.load(config_file)
    system_path=os.path.join(global_settings.project_path,'../system.json')
    with open(system_path, 'r', encoding='utf-8') as system_file:
        global_settings.system_config = json.load(system_file)
    global_settings.webapi_ip=args.ip

    global_settings.webapi_port=args.port

    pass
def initialization_db(mode):
    # 本地模式
    if mode==1:
        global_settings.db_connect_str=global_settings.config_data["db"]["sqlliteConnect"]
    # 互联网模式
    elif mode == 3:
        global_settings.db_connect_str=global_settings.config_data["db"]["mysqlConnect"]

    pass
# 启动参数
if __name__ == '__main__':
    pass
