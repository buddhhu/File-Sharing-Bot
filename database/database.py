# (©)CodeXBotz


from motor.motor_asyncio import AsyncIOMotorClient

from config import DB_NAME, DB_URI

dbclient = AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database["users"]


async def present_user(user_id: int):
    return bool(await user_data.find_one({"_id": user_id}))


async def add_user(user_id: int):
    await user_data.insert_one({"_id": user_id})


async def full_userbase():
    user_docs = await user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc["_id"])

    return user_ids


async def del_user(user_id: int):
    await user_data.delete_one({"_id": user_id})
