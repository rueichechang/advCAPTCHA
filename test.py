import pymongo, os

from dotenv import load_dotenv
load_dotenv()

serverIP = os.getenv("SERVER_IP")
mongoURL = os.getenv("MONGO_URL")

print('////')
print(mongoURL)
my_client = pymongo.MongoClient(mongoURL)



mydb = my_client["advcaptcha"]
task_data = mydb["task"]
demographic_data = mydb["demographic"]
post_question_collection = mydb["post_question_collection"]
preference_data = mydb["preference"]
feedback_collection = mydb["evaluation_feedback"]


myquery = { "name": "dsfsd" }
newvalues = { "$set": { "reasontolove": "123", "reasontohate":"456" } }

post_question_collection.update_one(myquery, newvalues)
