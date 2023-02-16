from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()


@user.get('/')
async def find_all_users():
    users = usersEntity(conn.local.user.find())
    print(users)
    return users


@user.post('/')
async def create_user(u: User):
    conn.local.user.insert_one(dict(u))
    return usersEntity(conn.local.user.find())
