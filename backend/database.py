import motor.motor_asyncio
from model import Todo

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.competition
collection = database.todo

async def fetch_one_todo(nom):
    document = await collection.find_one({"nom": nom})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(nom, Group):
    await collection.update_one({"nom": nom}, {"$set": {"Groupe": Group}})
    document = await collection.find_one({"nom": nom})
    return document

async def remove_todo(nom):
    await collection.delete_one({"nom": nom})
    return True