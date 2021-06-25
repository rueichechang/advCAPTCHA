from threading import Lock
from typing import Dict
from flask import Flask, render_template, session, request, \
    copy_current_request_context, send_from_directory
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from operator import itemgetter 
import time, os, glob, json
import numpy as np
import random
import pymongo
import uuid
import pandas as pd
from threading import Thread
from time import sleep

from dotenv import load_dotenv
load_dotenv()

# Get environment variables from .env
serverIP = os.getenv("SERVER_IP")
mongoURL = os.getenv("MONGO_URL")

# initiate mongodb
my_client = pymongo.MongoClient(mongoURL)

# initialize collection names
mydb                        = my_client["advcaptcha"]
task_data                   = mydb["task"]
demographic_data            = mydb["demographic"]
feedback_collection         = mydb["evaluation_feedback"]
captcha_spots               = mydb["captcha_spots"]
# participant_count           = mydb["participant_count"]

# initialize socket configurations
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

# # route after user submit the post questionaire
# @app.route('/post_question',methods=['POST'])
# def post_question():
#     table_id = request.values['table_id']
#     spot_id = request.values['spot_id']
#     # group = request.values['group']
#     # task_order = request.values['task_order']

#     print("----------------delay checking----------------")
#     late = request.values['late']
#     captcha_spots.update_one({"table_name": 'captcha_spots_table'}, { "$set":{spot_id:'empty'}})
#     if late == 'yes': return render_template('late.html',**locals())
#     print("----------------delay checked-----------------")

#     name = request.values['name']
#     email = request.values['email']
#     final_like_reason = request.values['reasontolove']
#     final_dislike_reason = request.values['reasontohate']

#     answer1 = request.values['answer1']
#     answer2 = request.values['answer2']
#     answer3 = request.values['answer3']
#     answer4 = request.values['answer4']


#     query = { "table_id": table_id }
#     newvalues = { "$set": { "name": name , 
#                             "email": email, 
#                             "final_like_reason": final_like_reason, 
#                             "final_dislike_reason": final_dislike_reason,
#                             "final_preference_order":dict(answer1=answer1,
#                                                         answer2=answer2,
#                                                         answer3=answer3,
#                                                         answer4=answer4,)} }
#     demographic_data.update_one(query, newvalues)
#     captcha_spots.update_one({"table_name": 'captcha_spots_table'}, { "$set":{spot_id:'complete'}})

#     return render_template('thank.html',**locals())


@app.route('/submit',methods=['POST'])
def submit():
    table_id    = request.values['table_id']
    spot_id     = request.values['spot_id']
    group       = request.values['group']
    task_order  = request.values['task_order']

    print("delay checking", spot_id)
    late = request.values['late']
    if late == 'yes': 
        captcha_spots.update_one({"table_name": 'captcha_spots_table'}, { "$set":{spot_id:'empty'}})
        demographic_query = {"spot_id" : spot_id}
        demographic_data.delete_one(demographic_query)
        return render_template('late.html',**locals())

    time_0 = request.values['0']
    time1_1 = request.values['11']
    time1_2 = request.values['12']
    time1_3 = request.values['13']
    time2_1 = request.values['21']
    time2_2 = request.values['22']
    time2_3 = request.values['23']
    time3_1 = request.values['31']
    time3_2 = request.values['32']
    time3_3 = request.values['33']
    time4_1 = request.values['41']
    time4_2 = request.values['42']
    time4_3 = request.values['43']

    count_0 = request.values['c0']
    count1_1 = request.values['c11']
    count1_2 = request.values['c12']
    count1_3 = request.values['c13']
    count2_1 = request.values['c21']
    count2_2 = request.values['c22']
    count2_3 = request.values['c23']
    count3_1 = request.values['c31']
    count3_2 = request.values['c32']
    count3_3 = request.values['c33']
    count4_1 = request.values['c41']
    count4_2 = request.values['c42']
    count4_3 = request.values['c43']

    user_input0 = request.values['pro0']
    user_input1_1 = request.values['pro1_1']
    user_input1_2 = request.values['pro1_2']
    user_input1_3 = request.values['pro1_3']
    user_input2_1 = request.values['pro2_1']
    user_input2_2 = request.values['pro2_2']
    user_input2_3 = request.values['pro2_3']
    user_input3_1 = request.values['pro3_1']
    user_input3_2 = request.values['pro3_2']
    user_input3_3 = request.values['pro3_3']
    user_input4_1 = request.values['pro4_1']
    user_input4_2 = request.values['pro4_2']
    user_input4_3 = request.values['pro4_3']

    ground_truth0 = request.values['ground_truth0']
    ground_truth1_1 = request.values['ground_truth1_1']
    ground_truth1_2 = request.values['ground_truth1_2']
    ground_truth1_3 = request.values['ground_truth1_3']
    ground_truth2_1 = request.values['ground_truth2_1']
    ground_truth2_2 = request.values['ground_truth2_2']
    ground_truth2_3 = request.values['ground_truth2_3']
    ground_truth3_1 = request.values['ground_truth3_1']
    ground_truth3_2 = request.values['ground_truth3_2']
    ground_truth3_3 = request.values['ground_truth3_3']
    ground_truth4_1 = request.values['ground_truth4_1']
    ground_truth4_2 = request.values['ground_truth4_2']
    ground_truth4_3 = request.values['ground_truth4_3']

    captcha_type0 = request.values['captcha_type0']
    captcha_type1_1 = request.values['captcha_type1_1']
    captcha_type1_2 = request.values['captcha_type1_2']
    captcha_type1_3 = request.values['captcha_type1_3']
    captcha_type2_1 = request.values['captcha_type2_1']
    captcha_type2_2 = request.values['captcha_type2_2']
    captcha_type2_3 = request.values['captcha_type2_3']
    captcha_type3_1 = request.values['captcha_type3_1']
    captcha_type3_2 = request.values['captcha_type3_2']
    captcha_type3_3 = request.values['captcha_type3_3']
    captcha_type4_1 = request.values['captcha_type4_1']
    captcha_type4_2 = request.values['captcha_type4_2']
    captcha_type4_3 = request.values['captcha_type4_3']

    file_address0 = request.values['file_address0']
    file_address1_1 = request.values['file_address1_1']
    file_address1_2 = request.values['file_address1_2']
    file_address1_3 = request.values['file_address1_3']
    file_address2_1 = request.values['file_address2_1']
    file_address2_2 = request.values['file_address2_2']
    file_address2_3 = request.values['file_address2_3']
    file_address3_1 = request.values['file_address3_1']
    file_address3_2 = request.values['file_address3_2']
    file_address3_3 = request.values['file_address3_3']
    file_address4_1 = request.values['file_address4_1']
    file_address4_2 = request.values['file_address4_2']
    file_address4_3 = request.values['file_address4_3']

    task_type0 = request.values['task_type0']
    task_type1_1 = request.values['task_type1_1']
    task_type1_2 = request.values['task_type1_2']
    task_type1_3 = request.values['task_type1_3']
    task_type2_1 = request.values['task_type2_1']
    task_type2_2 = request.values['task_type2_2']
    task_type2_3 = request.values['task_type2_3']
    task_type3_1 = request.values['task_type3_1']
    task_type3_2 = request.values['task_type3_2']
    task_type3_3 = request.values['task_type3_3']
    task_type4_1 = request.values['task_type4_1']
    task_type4_2 = request.values['task_type4_2']
    task_type4_3 = request.values['task_type4_3']

    task_time_ground_truth1_1 = request.values['task_time_ground_truth1_1']
    task_time_ground_truth1_2 = request.values['task_time_ground_truth1_2']
    task_time_ground_truth1_3 = request.values['task_time_ground_truth1_3']
    task_time_ground_truth2_1 = request.values['task_time_ground_truth2_1']
    task_time_ground_truth2_2 = request.values['task_time_ground_truth2_2']
    task_time_ground_truth2_3 = request.values['task_time_ground_truth2_3']
    task_time_ground_truth3_1 = request.values['task_time_ground_truth3_1']
    task_time_ground_truth3_2 = request.values['task_time_ground_truth3_2']
    task_time_ground_truth3_3 = request.values['task_time_ground_truth3_3']
    task_time_ground_truth4_1 = request.values['task_time_ground_truth4_1']
    task_time_ground_truth4_2 = request.values['task_time_ground_truth4_2']
    task_time_ground_truth4_3 = request.values['task_time_ground_truth4_3']


    likert_fb1_1 = request.values['likert_fb1_1']
    likert_fb1_2 = request.values['likert_fb1_2']
    # likert_fb1_3 = request.values['likert_fb1_3']
    text_fb1_1 = request.values['text_fb1_1']
    text_fb1_2 = request.values['text_fb1_2']
    text_fb1_3 = request.values['text_fb1_3']

    likert_fb2_1 = request.values['likert_fb2_1']
    likert_fb2_2 = request.values['likert_fb2_2']
    # likert_fb2_3 = request.values['likert_fb2_3']
    text_fb2_1 = request.values['text_fb2_1']
    text_fb2_2 = request.values['text_fb2_2']
    text_fb2_3 = request.values['text_fb2_3']

    likert_fb3_1 = request.values['likert_fb3_1']
    likert_fb3_2 = request.values['likert_fb3_2']
    # likert_fb3_3 = request.values['likert_fb3_3']
    text_fb3_1 = request.values['text_fb3_1']
    text_fb3_2 = request.values['text_fb3_2']
    text_fb3_3 = request.values['text_fb3_3']

    likert_fb4_1 = request.values['likert_fb4_1']
    likert_fb4_2 = request.values['likert_fb4_2']
    # likert_fb4_3 = request.values['likert_fb4_3']
    text_fb4_1 = request.values['text_fb4_1']
    text_fb4_2 = request.values['text_fb4_2']
    text_fb4_3 = request.values['text_fb4_3']

    dataJson = {}
    feedback = {}

    dataJson["practice"]    = dict(iteration=0, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address0,captcha_type=captcha_type0,task_type=task_type0,digit_ground_truth=ground_truth0,user_spent_time=time_0, count=count_0, user_input=user_input0)
    dataJson["instance1_1"] = dict(iteration=1, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address1_1,captcha_type=captcha_type1_1,task_type=task_type1_1,digit_ground_truth=ground_truth1_1, task_time_ground_truth=task_time_ground_truth1_1, user_spent_time=time1_1, count=count1_1, user_input=user_input1_1)
    dataJson["instance1_2"] = dict(iteration=2, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address1_2,captcha_type=captcha_type1_2,task_type=task_type1_2,digit_ground_truth=ground_truth1_2, task_time_ground_truth=task_time_ground_truth1_2, user_spent_time=time1_2, count=count1_2, user_input=user_input1_2)
    dataJson["instance1_3"] = dict(iteration=3, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address1_3,captcha_type=captcha_type1_3,task_type=task_type1_3,digit_ground_truth=ground_truth1_3, task_time_ground_truth=task_time_ground_truth1_3, user_spent_time=time1_3, count=count1_3, user_input=user_input1_3)
    
    dataJson["instance2_1"] = dict(iteration=1, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address2_1,captcha_type=captcha_type2_1,task_type=task_type2_1,digit_ground_truth=ground_truth2_1, task_time_ground_truth=task_time_ground_truth2_1, user_spent_time=time2_1, count=count2_1, user_input=user_input2_1)
    dataJson["instance2_2"] = dict(iteration=2, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address2_2,captcha_type=captcha_type2_2,task_type=task_type2_2,digit_ground_truth=ground_truth2_2, task_time_ground_truth=task_time_ground_truth2_2, user_spent_time=time2_2, count=count2_2, user_input=user_input2_2)
    dataJson["instance2_3"] = dict(iteration=3, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address2_3,captcha_type=captcha_type2_3,task_type=task_type2_3,digit_ground_truth=ground_truth2_3, task_time_ground_truth=task_time_ground_truth2_3, user_spent_time=time2_3, count=count2_3, user_input=user_input2_3)
    
    dataJson["instance3_1"] = dict(iteration=1, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address3_1,captcha_type=captcha_type3_1,task_type=task_type3_1,digit_ground_truth=ground_truth3_1, task_time_ground_truth=task_time_ground_truth3_1, user_spent_time=time3_1, count=count3_1, user_input=user_input3_1)
    dataJson["instance3_2"] = dict(iteration=2, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address3_2,captcha_type=captcha_type3_2,task_type=task_type3_2,digit_ground_truth=ground_truth3_2, task_time_ground_truth=task_time_ground_truth3_2, user_spent_time=time3_2, count=count3_2, user_input=user_input3_2)
    dataJson["instance3_3"] = dict(iteration=3, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address3_3,captcha_type=captcha_type3_3,task_type=task_type3_3,digit_ground_truth=ground_truth3_3, task_time_ground_truth=task_time_ground_truth3_3, user_spent_time=time3_3, count=count3_3, user_input=user_input3_3)
    
    dataJson["instance4_1"] = dict(iteration=1, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address4_1,captcha_type=captcha_type4_1,task_type=task_type4_1,digit_ground_truth=ground_truth4_1, task_time_ground_truth=task_time_ground_truth4_1, user_spent_time=time4_1, count=count4_1, user_input=user_input4_1)
    dataJson["instance4_2"] = dict(iteration=2, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address4_2,captcha_type=captcha_type4_2,task_type=task_type4_2,digit_ground_truth=ground_truth4_2, task_time_ground_truth=task_time_ground_truth4_2, user_spent_time=time4_2, count=count4_2, user_input=user_input4_2)
    dataJson["instance4_3"] = dict(iteration=3, table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,file_address=file_address4_3,captcha_type=captcha_type4_3,task_type=task_type4_3,digit_ground_truth=ground_truth4_3, task_time_ground_truth=task_time_ground_truth4_3, user_spent_time=time4_3, count=count4_3, user_input=user_input4_3)
    
    feedback["feedback1"]   = dict(table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,likert_fb1_1=likert_fb1_1, likert_fb1_2=likert_fb1_2, text_fb1_1=text_fb1_1, text_fb1_2=text_fb1_2, text_fb1_3=text_fb1_3)
    feedback["feedback2"]   = dict(table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,likert_fb2_1=likert_fb2_1, likert_fb2_2=likert_fb2_2, text_fb2_1=text_fb2_1, text_fb2_2=text_fb2_2, text_fb2_3=text_fb2_3)
    feedback["feedback3"]   = dict(table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,likert_fb3_1=likert_fb3_1, likert_fb3_2=likert_fb3_2, text_fb3_1=text_fb3_1, text_fb3_2=text_fb3_2, text_fb3_3=text_fb3_3)
    feedback["feedback4"]   = dict(table_id=table_id,spot_id=spot_id,group=group,task_order=task_order,likert_fb4_1=likert_fb4_1, likert_fb4_2=likert_fb4_2, text_fb4_1=text_fb4_1, text_fb4_2=text_fb4_2, text_fb4_3=text_fb4_3)
    
    task_data.insert_one(dataJson)
    feedback_collection.insert_one(feedback)

    #for submit form
    name = request.values['name']
    email = request.values['email']
    final_like_reason = request.values['reasontolove']
    final_dislike_reason = request.values['reasontohate']
    technical_report = request.values['technical_report']
    end_time = request.values['end_time']

    answer1 = request.values['answer1']
    answer2 = request.values['answer2']
    answer3 = request.values['answer3']
    answer4 = request.values['answer4']

    start_time = captcha_spots.find_one({"table_name" : "captcha_spots_table"})[spot_id]
    try:
        total_spent_time = int(end_time) - int(start_time)
    except:
        total_spent_time = 0
    query = { "table_id": table_id }
    newvalues = { "$set": { "name": name , 
                            "email": email, 
                            "final_like_reason": final_like_reason, 
                            "final_dislike_reason": final_dislike_reason,
                            "technical_report" : technical_report,
                            "total_spent_time" : total_spent_time,
                            "final_preference_order":dict(answer1=answer1,
                                                        answer2=answer2,
                                                        answer3=answer3,
                                                        answer4=answer4,)} }
    demographic_data.update_one(query, newvalues)
    captcha_spots.update_one({"table_name": 'captcha_spots_table'}, { "$set":{spot_id:'complete'}})



    return render_template('thank.html',**locals())

    # return render_template('submit.html', async_mode=socketio.async_mode,
    #                                         table_id = table_id,
    #                                         spot_id = spot_id,
    #                                         group = group,
    #                                         task_order = task_order,
    #                                         file_address1_1 = file_address1_1,
    #                                         file_address2_1 = file_address2_1,
    #                                         file_address3_1 = file_address3_1,
    #                                         file_address4_1 = file_address4_1)


@app.route('/demographic_control',methods=['POST'])
def demographic_control():
    # Retrieve start time
    start_time = request.values['start_time']

    # Retrieve user's input data from the entry survey
    table_id = request.values['table_id']
    age     = request.values['age']
    gender  = request.values['gender']
    familiaritynum = request.values['familiaritynum']
    familiaritycaptcha = request.values['familiaritycaptcha']
    familiarityaudio = request.values['familiarityaudio']
    apparatus = request.values['apparatus']

    # update the input variables that to be added to database
    demographic = {}
    demographic["table_id"]     = table_id
    demographic["age"]          = age
    demographic["gender"]       = gender
    demographic["play_mode"]    = apparatus
    demographic["familiarity_english"]          = familiaritynum
    demographic["familiarity_original_captcha"] = familiaritycaptcha
    demographic["familiarity_audio_captcha"]    = familiarityaudio

    # generate empty variables that user will fill in in the final survey
    demographic['name'] = ''
    demographic['email'] = ''
    demographic['final_like_reason'] = ''
    demographic['final_dislike_reason'] = ''
    demographic['final_preference_order'] = ''
    demographic['total_spent_time'] = ''
    

    # get group
    group = "test group"

    # get participants_num
    # res = participant_count.update_one({"_id": 'participants_num'}, {"$inc": {"count": 1}}, upsert =True)
    # doc  = participant_count.find_one({"_id": 'participants_num'})
    # participants_id = str(doc["count"])

    # generate captcha spots if empty
    spot_limit = 25
    if captcha_spots.count() == 0:
        spots = {"table_name":'captcha_spots_table'}
        for i in range (1,spot_limit):
            name = "spot_" + str(i)
            spots[name] = 'empty'
        captcha_spots.insert(spots)

    # get spots and check if there is empty captcha pack
    spots  = captcha_spots.find_one({"table_name": 'captcha_spots_table'})
    if 'empty' in list(spots.values()):
        empty_spots_index = [i for i, e in enumerate(list(spots.values())) if e == 'empty']
        if len(empty_spots_index) == 1:
            spot_id = list(spots.keys())[empty_spots_index[0]]
        else:
            empty_spots = list(itemgetter(*empty_spots_index)(list(spots.keys())))
            # print('empty_spots', empty_spots)
            spot_id = empty_spots.pop(0)
        captcha_spots.update_one({"table_name": 'captcha_spots_table'}, { "$set":{spot_id : start_time}})
    else: 
        return render_template('full.html',**locals()) 

    spot_tsv_address = 'static/prototypes/'+spot_id[5:]+'/task_info.tsv'
    spot_tsv = pd.read_csv(spot_tsv_address, header=None, sep='\t', dtype = str)

    task_order_file_name = 'participant_task_ordering_2021-06-21-16-49'
    task_order_address = 'static/prototypes/'+task_order_file_name+'.tsv'
    task_order_tsv = pd.read_csv(task_order_address, header=None, sep='\t')
    spot_num = int(spot_id[5:])
    task_order = task_order_tsv.iloc[spot_num,1]

    # update user data to the database
    demographic['task order'] = task_order
    demographic['spot_id'] = spot_id
    demographic_data.insert_one(demographic)

    return render_template('tasks.html', async_mode=socketio.async_mode,
                                        table_id        = table_id,
                                        spot_id         = spot_id,
                                        group           = group,
                                        task_order      = task_order,
                                        
                                        practice       = "prototypes/example/example.wav",
                                        captcha_type0  = "0",
                                        task_type0     = "example",
                                        ground_truth0  = "123456",
                                        

                                        instance1_1         = "prototypes/"+spot_id[5:]+"/task1_1.wav", 
                                        captcha_type1_1     = "0",
                                        task_type1_1        = spot_tsv.iloc[0,1],
                                        ground_truth1_1     = spot_tsv.iloc[0,2],
                                        task_time_ground_truth1_1 = spot_tsv.iloc[0,4],

                                        instance1_2         ="prototypes/"+spot_id[5:]+"/task1_2.wav", 
                                        captcha_type1_2     = "0",
                                        task_type1_2        = spot_tsv.iloc[1,1],
                                        ground_truth1_2     = spot_tsv.iloc[1,2],
                                        task_time_ground_truth1_2 = spot_tsv.iloc[1,4],

                                        instance1_3         ="prototypes/"+spot_id[5:]+"/task1_3.wav", 
                                        captcha_type1_3     = "0",
                                        task_type1_3        = spot_tsv.iloc[2,1],
                                        ground_truth1_3     = spot_tsv.iloc[2,2],
                                        task_time_ground_truth1_3 = spot_tsv.iloc[2,4],

                                        instance2_1         ="prototypes/"+spot_id[5:]+"/task2_1.wav", 
                                        captcha_type2_1     = "0",
                                        task_type2_1        = spot_tsv.iloc[3,1],
                                        ground_truth2_1     = spot_tsv.iloc[3,2],
                                        task_time_ground_truth2_1 = spot_tsv.iloc[3,4],

                                        instance2_2         ="prototypes/"+spot_id[5:]+"/task2_2.wav", 
                                        captcha_type2_2     = "0",
                                        task_type2_2        = spot_tsv.iloc[4,1],
                                        ground_truth2_2     = spot_tsv.iloc[4,2],
                                        task_time_ground_truth2_2 = spot_tsv.iloc[4,4],

                                        instance2_3         ="prototypes/"+spot_id[5:]+"/task2_3.wav", 
                                        captcha_type2_3     = "0",
                                        task_type2_3        = spot_tsv.iloc[5,1],
                                        ground_truth2_3     = spot_tsv.iloc[5,2],
                                        task_time_ground_truth2_3 = spot_tsv.iloc[5,4],

                                        instance3_1         ="prototypes/"+spot_id[5:]+"/task3_1.wav", 
                                        captcha_type3_1     = "0",
                                        task_type3_1        = spot_tsv.iloc[6,1],
                                        ground_truth3_1     = spot_tsv.iloc[6,2],
                                        task_time_ground_truth3_1 = spot_tsv.iloc[6,4],

                                        instance3_2         ="prototypes/"+spot_id[5:]+"/task3_2.wav", 
                                        captcha_type3_2     = "0",
                                        task_type3_2        = spot_tsv.iloc[7,1],
                                        ground_truth3_2     = spot_tsv.iloc[7,2],
                                        task_time_ground_truth3_2 = spot_tsv.iloc[7,4],

                                        instance3_3         ="prototypes/"+spot_id[5:]+"/task3_3.wav", 
                                        captcha_type3_3     = "0",
                                        task_type3_3        = spot_tsv.iloc[8,1],
                                        ground_truth3_3     = spot_tsv.iloc[8,2],
                                        task_time_ground_truth3_3 = spot_tsv.iloc[8,4],

                                        instance4_1         ="prototypes/"+spot_id[5:]+"/task4_1.wav", 
                                        captcha_type4_1     = "0",
                                        task_type4_1        = spot_tsv.iloc[9,1],
                                        ground_truth4_1     = spot_tsv.iloc[9,2],
                                        task_time_ground_truth4_1 = spot_tsv.iloc[9,4],

                                        instance4_2         ="prototypes/"+spot_id[5:]+"/task4_2.wav", 
                                        captcha_type4_2     = "0",
                                        task_type4_2        = spot_tsv.iloc[10,1],
                                        ground_truth4_2     = spot_tsv.iloc[10,2],
                                        task_time_ground_truth4_2 = spot_tsv.iloc[10,4],

                                        instance4_3         ="prototypes/"+spot_id[5:]+"/task4_3.wav",
                                        captcha_type4_3     = "0",
                                        task_type4_3        = spot_tsv.iloc[11,1],
                                        ground_truth4_3     = spot_tsv.iloc[11,2],
                                        task_time_ground_truth4_3 = spot_tsv.iloc[11,4],
)
@app.route('/')
def index():
    table_id = uuid.uuid1()
    return render_template('index.html', async_mode=socketio.async_mode,
                                        table_id=table_id)


@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@socketio.on('for_test', namespace='/test')
def for_test(test):
    print("================================="+test)
    emit('test_response', "Hello I am server" + test)


@socketio.on('connect', namespace='/test')
def test_connect():
    print("connect")
    emit('my_response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)

def timer():
    # time_ref = round(time.time() * 1000)
    time_dur = 1800 #seconds
    while True:
        sleep(time_dur)
        spots = captcha_spots.find_one({"table_name": 'captcha_spots_table'})
        for spot in spots:
            if spot[:5] == "spot_":
                spot_value = spots[spot]
                
                if spot_value != "empty" and spot_value != "complete":
                    current_time = round(time.time() * 1000)
                    interval = current_time - int(spot_value)
                    
                    if interval > (time_dur * 1000):
                        captcha_spots.update_one({"table_name": 'captcha_spots_table'}, { "$set":{spot : 'empty'}})
                        demographic_query = {'spot_id': spot}
                        demographic_data.delete_one(demographic_query)

if __name__ == '__main__':
    t = Thread(target=timer)
    t.start()
    socketio.run(app, debug=False, host='0.0.0.0', port=80)
