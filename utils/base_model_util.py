from pydantic import BaseModel

from typing import Union
from fastapi import Body
from datetime import datetime
# 返回数据基类
class BaseReturnModel(BaseModel):
    code: int = Body( default=200,description="状态码")
    message: str = Body(default="成功", description="消息")
    data: Union[list, dict, str, int, float, bool, None] = Body(default=None, description="数据")



class PageBaseReturnModel(BaseModel):
    page : int = Body( description="页码")
    per_page : int = Body( description="页大小")
    total_count : int = Body( description="总大小")
    data : list = Body( description="数据")

class PageBaseResponseModel(BaseModel):
    page : int = Body( description="页码")
    per_page : int = Body( description="页大小")
    sTime:Union[datetime, None]  = Body(default=None,description="开始时间")
    eTime: Union[datetime, None] = Body(default=None,description="结束时间")