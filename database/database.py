# (©)CodeXBotz


from motor.motor_asyncio import AsyncIOMotorClient

from config import DB_NAME, DB_URI

dbclient = AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database["users"]


_cache = []

async def cache():
    global _cache
    _cache = await full_userbase()

async def present_user(user_id: int):
    return user_id in _cache


async def add_user(user_id: int):
    if user_id not in _cache:
        _cache.append(user_id)
    await user_data.insert_one({"_id": user_id})


async def full_userbase():
    if _cache:
        return _cache
    user_docs = await user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc["_id"])

    return user_ids


async def del_user(user_id: int):
    if user_id in _cache:
        _cache.remove(user_id)
    await user_data.delete_one({"_id": user_id})
