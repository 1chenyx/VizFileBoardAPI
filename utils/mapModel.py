file_type_folder_map = {
    ".mp3": "audios",
    ".wav": "audios",
    ".doc": "docs",
    ".docx": "docs",
    ".pdf": "docs",
    ".jpg": "imgs",
    ".jpeg": "imgs",
    ".png": "imgs",
    ".mp4": "videos",
    ".avi": "videos",
    ".zip": "zips",
    ".rar": "zips",
    # 可以根据需要添加更多文件类型
}
# 0-其他，1-音频，2-文档，3-图片，4-视频,5-压缩包
file_type_map = {
    ".mp3": 1,
    ".wav": 1,
    ".doc": 2,
    ".docx": 2,
    ".pdf": 2,
    ".jpg": 3,
    ".jpeg": 3,
    ".png": 3,
    ".mp4": 4,
    ".avi": 4,
    ".zip": 5,
    ".rar": 5,
    # 可以根据需要添加更多文件类型
}