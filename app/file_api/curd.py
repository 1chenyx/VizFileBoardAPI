import os
import uuid
import hashlib

from GlobalParameters import global_settings
from app.file_api.models import FileInfo
from app.file_api.schemas import UpdateFileInfoModel
from utils.db_utils.SqlHelp import get_db
from utils.file_utils.file_handle import calculate_md5
from utils.mapModel import file_type_folder_map, file_type_map
from datetime import datetime


# 上传文件
async def upload_file(file)->str:
    db=get_db()
    # 获取md5值
    md5_value,file_size = await calculate_md5(file)
    old_file_info = db.query(FileInfo).filter(FileInfo.IsDel == False and FileInfo.MD5Value==md5_value).first()
    # 判断是否存在
    if old_file_info:
        return "文件已存在"
    # 获取文件扩展名
    file_extension = os.path.splitext(file.filename)[1].lower()

    # 确定文件夹类型
    folder_type = file_type_folder_map.get(file_extension, "others")  # 默认文件夹为"others"

    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 构建完整的保存路径
    save_path = os.path.join(global_settings.config_data["filepath"],folder_type, current_date)
    os.makedirs(save_path, exist_ok=True)

    file_uuid = uuid.uuid4()
    # 新的文件名
    new_filename = f"{file_uuid}{file_extension}"
    # 相对路径
    relative_path = os.path.join(save_path, new_filename)

    #组织参数
    new_file_info= FileInfo(
        id= uuid.uuid4(),
        Version= global_settings.config_data["Version"],
        FileType=file_type_map.get(file_extension, 0),
        FilePath=relative_path,
        FileExtension=file_extension,
        MD5Value=md5_value,
        file_size=file_size,
        Name=os.path.splitext(file.filename)[0]
    )

    # 插入数据库
    db.add(new_file_info)
    db.commit()
    # db.refresh(new_file_info)
    # 保存文件
    return "成功"

def updateimagesInfo(fromdata:UpdateFileInfoModel):

    db=get_db()
    # 判断是否已存在
    db.query(FileInfo).filter(FileInfo.IsDel == False).filter(FileInfo.id == fromdata.id).update(fromdata)
    db.commit()
    return True


