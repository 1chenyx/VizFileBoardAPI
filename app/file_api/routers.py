import os
import re

from fastapi import APIRouter, File, UploadFile, HTTPException
import uuid
import hashlib

from app.file_api.curd import upload_file,updatefileInfo,deletefileInfo,deletefileInfoTrue
from app.file_api.schemas import UpdateFileInfoModel
from utils.base_model_util import BaseReturnModel

router = APIRouter()


# 新增上传文件
@router.post("/file/upload/" ,response_model=BaseReturnModel, summary="新增上传文件")
async def upload(file: UploadFile = File(...)) ->BaseReturnModel:
    message=await upload_file(file)
    if message=="成功":
        return BaseReturnModel(message=message, code=200)
    # 上传文件
    return BaseReturnModel (message=message, code=-1)

# 修改文件基本信息
@router.post("/file/update/" ,response_model=BaseReturnModel, summary="修改文件信息")
async def update(fromdata:UpdateFileInfoModel) ->BaseReturnModel:
    # 假设update_file_info是正确的函数名，需要根据实际情况修改
    message = await updatefileInfo(fromdata)
    if message == "成功":
        return BaseReturnModel(message=message, code=200)
    # 上传文件
    return BaseReturnModel(message=message, code=-1)

# 删除文件
@router.post("/file/delete/",response_model=BaseReturnModel, summary="删除文件")
async def delete(id:str) ->BaseReturnModel:
    # 假设update_file_info是正确的函数名，需要根据实际情况修改
    message = deletefileInfo(id = id)
    if message == "成功":
        return BaseReturnModel(message=message, code=200)
    return BaseReturnModel(message=message, code=-1)
# 彻底删除文件
@router.post("/file/deleteTrue/",response_model=BaseReturnModel, summary="彻底删除文件")
async def deleteTrue(id:str) ->BaseReturnModel:
    # 假设update_file_info是正确的函数名，需要根据实际情况修改
    message = deletefileInfoTrue(id = id)
    if message == "成功":
        return BaseReturnModel(message=message, code=200)
    return BaseReturnModel(message=message, code=-1)

# 查询文件列表

# 查询文件详细信息
# 恢复文件
