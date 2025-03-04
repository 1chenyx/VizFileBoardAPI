from src.utils.database.SqlHelp import Base

from sqlalchemy import Boolean, Column, Integer, String, DateTime, Numeric, func


# 文件项目表
class FileProjectInfo(Base):
    __tablename__ = "FileProjectInfo"

    id: Column[int] = Column(Integer, primary_key=True, autoincrement=True,comment="主键")
    Creation_Time: Column[datetime.datetime] = Column(DateTime, default=func.now(), nullable=False, comment="创建时间")
    # 数据类型
    DataType: Column[int] = Column(Integer, default=1,nullable=False,comment="数据类型（1-文件，2-项目)")
    # 版本号
    Version: Column[int] = Column(Integer, default=0,nullable=False,comment="版本号")
    # 文件类型
    FileType: Column[int] = Column(Integer,nullable=True,default=1,comment="文件类型（图片、视频、、、)")
    # 是否收藏
    IsCollect: Column[bool] = Column(Boolean,nullable=False,default=False,comment="是否收藏")
    # 文件地址
    FilePath: Column[str] = Column(String(200),nullable=False,comment="文件地址（相对地址）")
    # 标签信息
    # [{"name":"标签名字","id":"标签id"}]
    Labels: Column[str] = Column(String(500),nullable=False,default="[]",comment="标签信息")
    # 配置信息
    # {"bz":"备注","imgsize":"图片尺寸","source":"来源","projectInfo":[{"name":"项目名字","id":"项目id"}]}
    ConfigJson: Column[str] = Column(String(1000),nullable=False,default="{}",comment="配置信息")

    # 搜索内容
    # ["内容1","内容2"]
    SearchInfo: Column[str] = Column(String(1000),nullable=False,comment="搜索内容")
    # 文件后缀
    FileExtension: Column[str] = Column(String(50),nullable=False,comment="文件后缀")
    # MD5值
    MD5Value: Column[str] = Column(String(1),nullable=True,comment="文件后缀")
    # 名字
    Name: Column[str] = Column(String(100),nullable=False,comment="名字")

    # 空间大小
    SpaceSize: Column[int] = Column(Integer,nullable=True,comment="空间大小")
    # 是否已删除
    IsDelete: Column[bool] = Column(Boolean,nullable=False,default=False,comment="是否已删除")





# 文件标签关联表
class FileProjectTagInfo(Base):
    __tablename__ = "FileProjectTagInfo"

    id  : Column[int] = Column(Integer, primary_key=True, autoincrement=True,comment="主键")
    Creation_Time: Column[datetime.datetime] = Column(DateTime, default=func.now(), nullable=False, comment="创建时间")
    # 文件节点Id
    FileNodeId: Column[int] = Column(Integer, default=0,nullable=True,comment="文件节点Id")
    # 标签Id
    LabelId: Column[int] = Column(Integer, default=0,nullable=True,comment="标签Id")
class TagInfo(Base):
    __tablename__ = "TagInfo"

    id = Column(Integer, primary_key=True, autoincrement=True,comment="主键")
    Creation_Time = Column(DateTime, default=func.now(), nullable=False, comment="创建时间")

    TagName = Column(String(20), unique=True,  comment="标签名字")