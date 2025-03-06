import os

from fastapi import APIRouter, File, UploadFile, HTTPException
import uuid
import hashlib

from app.file_api.curd import upload_file
from app.file_api.schemas import UpdateFileInfoModel
from utils.base_model_util import BaseReturnModel

router = APIRouter()


# 新增上传文件
@router.post("/file/upload/" ,response_model=BaseReturnModel, summary="新增上传文件")
async def upload(file: UploadFile = File(...)) ->BaseReturnModel:
    message=upload_file(file)
    if message=="成功":
        return BaseReturnModel(message=message, code=200, data=None)
    # 上传文件
    return BaseReturnModel (message=message, code=-1, data=None)

# 修改文件基本信息
@router.post("/file/update/" ,response_model=BaseReturnModel, summary="修改文件信息")
async def upload(fromdata:UpdateFileInfoModel) ->BaseReturnModel:

    message=""
    if message=="成功":
        return BaseReturnModel(message=message, code=200, data=None)
    # 上传文件
    return BaseReturnModel (message=message, code=-1, data=None)


# 查询文件列表
# 查询文件详细信息
# 删除文件
# 彻底删除文件
# 恢复文件
