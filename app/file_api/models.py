

from sqlalchemy import Boolean, Column, Integer, String, DateTime, func

from pydantic import BaseModel
from datetime import datetime

# 文件项目表
class FileInfo(BaseModel):
    __tablename__ = "FileInfo"

    id: Column[str] = Column(String(50), primary_key=True, comment="主键")
    Creation_Time: Column[datetime] = Column(DateTime, default=func.now(), nullable=False, comment="创建时间")
    # 修改时间
    Modify_Time: Column[datetime] = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False, comment="修改时间")
    # 版本号
    Version: Column[int] = Column(Integer, default=0,nullable=False,comment="版本号")
    # 文件类型
    FileType: Column[int] = Column(Integer,nullable=True,default=1,comment="文件类型（# 0-其他，1-音频，2-文档，3-图片，4-视频,5-压缩包)")
    # 是否收藏
    IsCollect: Column[bool] = Column(Boolean,nullable=False,default=False,comment="是否收藏")
    # 文件地址
    FilePath: Column[str] = Column(String(200),nullable=False,comment="文件地址（相对地址）")
    # 标签信息
    # [{"name":"标签名字","id":"标签id"}]
    Tags: Column[str] = Column(String(500),nullable=False,default="[]",comment="标签信息")
    # 基本信息（一个json用来动态添加基本信息）
    # {"imgsize":"图片尺寸","source":"来源","projectInfo":[{"name":"项目名字","id":"项目id"}]}
    BasicInfo: Column[str] = Column(String(1000),nullable=False,default="{}",comment="基本信息")
    # 备注
    Bz: Column[str] = Column(String(1000),nullable=False,default="",comment="备注")
    # 文件后缀
    FileExtension: Column[str] = Column(String(50),nullable=False,comment="文件后缀")
    # MD5值
    MD5Value: Column[str] = Column(String(1),nullable=True,comment="MD5值")
    # 名字
    Name: Column[str] = Column(String(100),nullable=False,comment="名字")
    # 空间大小
    SpaceSize: Column[int] = Column(Integer,nullable=True,comment="空间大小")
    # 是否已删除
    IsDelete: Column[bool] = Column(Boolean,nullable=False,default=False,comment="是否已删除")






class TagInfo(BaseModel):
    __tablename__ = "TagInfo"

    id = Column(Integer, primary_key=True, autoincrement=True,comment="主键")
    Creation_Time = Column(DateTime, default=func.now(), nullable=False, comment="创建时间")

    TagName = Column(String(20), unique=True,  comment="标签名字")