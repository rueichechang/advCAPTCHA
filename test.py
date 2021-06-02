# import pymongo, os

# from dotenv import load_dotenv
# load_dotenv()

# serverIP = os.getenv("SERVER_IP")
# mongoURL = os.getenv("MONGO_URL")

# print('////')
# print(mongoURL)
# my_client = pymongo.MongoClient(mongoURL)



# mydb = my_client["advcaptcha"]
# task_data = mydb["task"]
# demographic_data = mydb["demographic"]
# post_question_collection = mydb["post_question_collection"]
# preference_data = mydb["preference"]
# feedback_collection = mydb["evaluation_feedback"]


# myquery = { "name": "dsfsd" }
# newvalues = { "$set": { "reasontolove": "123", "reasontohate":"456" } }

# post_question_collection.update_one(myquery, newvalues)

import pandas as pd
# spot_tsv_address = 'static/prototypes/'+str(7)+'/task_info.tsv'
# spot_tsv = pd.read_csv(spot_tsv_address, header=None,sep='\t')
# print(spot_tsv.iloc[0,3])
task_order_address = 'static/prototypes/participant_task_ordering_2021-05-25-01-18.tsv'
task_order_tsv = pd.read_csv(task_order_address, header=None, sep='\t')
print(task_order_tsv.iloc[0,1])

