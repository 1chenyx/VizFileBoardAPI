import os


class GlobalSettings:
    # 项目绝对地址
    project_path = os.path.abspath('.')
    # 系统设置
    system_config = {}
    # 配置数据
    config_data = {}
    # 数据库连接字符串
    db_connect_str = ""

    # webapi ip地址
    webapi_ip = ""
    # webapi port端口
    webapi_port = 15674
# 全局参数
global_settings =GlobalSettings()
