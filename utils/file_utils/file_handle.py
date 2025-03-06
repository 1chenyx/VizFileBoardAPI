import hashlib

from fastapi import UploadFile


async def calculate_md5(file: UploadFile):
    """
    计算上传文件的 MD5 值。

    参数:
    file (UploadFile): 上传的文件对象。

    返回:
    str: 文件的 MD5 值。
    """
    file.seek(0)  # 将文件指针移到开头
    md5_hash = hashlib.md5()
    total_read = 0
    while True:
        chunk = await file.read(8192)
        if not chunk:
            break
        md5_hash.update(chunk)
        total_read += len(chunk)
    await file.close()
    return md5_hash.hexdigest(),total_read
