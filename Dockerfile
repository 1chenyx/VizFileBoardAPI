# 使用 Python 官方提供的镜像作为基础镜像
FROM python:3.10

# 将工作目录设置为 /app
WORKDIR /app

# 复制当前目录中的所有文件到容器的 /app 目录中
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 FastAPI 应用程序的端口
EXPOSE 15001

# 启动 FastAPI 应用程序
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15001"]
