from fastapi import APIRouter, Depends, HTTPException, status, Security
router = APIRouter()
# //登录（微信登录）获取token
@router.get("/test/test",  summary="测试接口")
async def wechat_login_token(
    form_data: str) :
    return "test"
