import os
import uuid
import hashlib

from GlobalParameters import global_settings
from app.file_api.models import FileInfo
from app.file_api.schemas import UpdateFileInfoModel
from utils.db_utils.SqlHelp import get_db
from utils.file_utils.file_handle import calculate_md5
from utils.mapModel import file_type_folder_map, file_type_map
from utils.base_model_util import PageBaseResponseModel, PageBaseReturnModel, BaseReturnModel

from datetime import datetime


# 上传文件
async def upload_file(file)->str:
    db=get_db()
    # 获取md5值
    md5_value,file_size = await calculate_md5(file)
    old_file_info = db.query(FileInfo).filter(FileInfo.IsDelete == False and FileInfo.MD5Value==md5_value).first()
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
        id= str(uuid.uuid4()),
        Version= global_settings.config_data["Version"],
        FileType=file_type_map.get(file_extension, 0),
        FilePath=relative_path,
        FileExtension=file_extension,
        MD5Value=str(md5_value),
        SpaceSize=file_size,
        Name=os.path.splitext(file.filename)[0]
    )

    # 插入数据库
    db.add(new_file_info)
    db.commit()
    # db.refresh(new_file_info)
    # 保存文件
    return "成功"
# 修改文件基本信息
async def updatefileInfo(fromdata:UpdateFileInfoModel):
    # 更新文件基本信息数据
    # 数据库
    db=get_db()
    # 判断是否已存在
    old_file_info = db.query(FileInfo).filter(FileInfo.IsDelete == False and FileInfo.id==fromdata.id).first()
    if not old_file_info:
        return "文件不存在"
    # 如果修改了数据就更新数据否则不更新
    if fromdata.BasicInfo:
        old_file_info.BasicInfo=str(fromdata.BasicInfo)
    if fromdata.Bz:
        old_file_info.Bz=str(fromdata.Bz)
    if fromdata.IsCollect:
        old_file_info.IsCollect=bool(fromdata.IsCollect)
    if fromdata.Tags:
        old_file_info.Tags=str(fromdata.Tags)
    if fromdata.Name:
        old_file_info.Name = str(fromdata.Name)  # 原错误代码是 FileType=str(fromdata.Name)
    # 保存数据
    db.commit()
    return "成功"


# 删除文件基本信息
def deletefileInfo(id:str):
    # 数据库
    db=get_db()
    # 判断是否已存在
    old_file_info = db.query(FileInfo).filter(FileInfo.IsDelete == False, FileInfo.id==id).first()
    if not old_file_info:
        return "文件不存在"
    # 修改数据
    old_file_info.IsDelete = True
    # 保存数据
    db.commit()
    return "成功"
# 彻底删除文件
def deletefileInfoTrue(id:str):
    # 数据库
    db=get_db()
    # 判断是否已存在
    old_file_info = db.query(FileInfo).filter(FileInfo.IsDelete == False, FileInfo.id==id).first()
    if not old_file_info:
        return "文件不存在"
    # 删除文件
    file_path = old_file_info.FilePath
    if os.path.exists(str(file_path)):
        os.remove(str(file_path))
    # 删除数据库数据
    db.delete(old_file_info)
    db.commit()
    return "成功"
# 分页查询文件列表
def getfilePageList(fromdata:PageBaseResponseModel)->PageBaseReturnModel:
    db=get_db()
    # 分页查询数据
    query = db.query(FileInfo)
    # 过滤已删除的数据
    query = query.filter(FileInfo.IsDelete == False)
    # 过滤时间
    if fromdata.sTime and fromdata.eTime:
        query = query.filter(FileInfo.CreateTime >= fromdata.sTime, FileInfo.CreateTime <= fromdata.eTime)
    # 统计总条数
    total_count = query.count()
    # 分页查询数据
    query = query.offset((fromdata.page - 1) * fromdata.per_page).limit(fromdata.per_page)
    # 转换为列表
    data = query.all()
    # 转换为字典列表
    data_list = [item.__dict__ for item in data]
    # 构建返回数据
    return_data = PageBaseReturnModel(
        
    )
    return_data.page = fromdata.page
    return_data.per_page = fromdata.per_page
    return_data.total_count = total_count
    return_data.data = data_list
    return return_data
    pass


