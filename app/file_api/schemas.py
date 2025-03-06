from pydantic import BaseModel
from datetime import datetime
from typing import Union

from fastapi.params import Body
from pydantic import BaseModel

from utils.base_model_util import PageBaseResponseModel, PageBaseReturnModel, BaseReturnModel
from fastapi import Body

class UpdateFileInfoModel(BaseModel):
    id: str = Body(..., description="主键")  # 文件标题
    Tags: Union[str, None] = Body(default=None, description="标签信息")
    BasicInfo: Union[str, None] = Body(default=None, description="基本信息")
    Bz: Union[str, None] = Body(default=None, description="备注")
    Name: Union[str, None] = Body(default=None, description="文件名")
    IsCollect: Union[bool, None] = Body(default=None, description="是否收藏")

