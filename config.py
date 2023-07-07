import motor.motor_asyncio
from dotenv import load_dotenv
import os
load_dotenv('.env')
username: str = os.getenv('USERNAME')
password: str = os.getenv('PASSWORD')

MONGODB_URL = "mongodb+srv://{username}:{password}@fastapi.oqzzohy.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)


#connect to database
database = client.python_db