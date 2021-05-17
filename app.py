from threading import Lock
from typing import Dict
from flask import Flask, render_template, session, request, \
    copy_current_request_context, send_from_directory
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import time, os, glob, json
import numpy as np
import random
import pymongo
import uuid

from dotenv import load_dotenv
load_dotenv()

serverIP = os.getenv("SERVER_IP")
mongoURL = os.getenv("MONGO_URL")

print('////')
print(mongoURL)
# 'mongodb+srv://advcaptcha:hankhaopinlee@cluster0.j1zm5.gcp.mongodb.net'
# mongo_url = mongoURL
my_client = pymongo.MongoClient(mongoURL)


mydb = my_client["advcaptcha"]
task_data = mydb["task"]
demographic_data = mydb["demographic"]
post_question_collection = mydb["post_question_collection"]
preference_data = mydb["preference"]


async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/post_question',methods=['POST'])
def post_question():
    name = request.values['name']
    email = request.values['email']
    reasontolove = request.values['reasontolove']
    reasontohate = request.values['reasontohate']

    answer1 = request.values['answer1']
    answer2 = request.values['answer2']
    answer3 = request.values['answer3']
    answer4 = request.values['answer4']

    result = {}
    result['name'] = name
    result['email'] = email
    result['reasontolove'] = reasontolove
    result['reasontohate'] = reasontohate
    result['preference'] = dict(answer1=answer1,
                                answer2=answer2,
                                answer3=answer3,
                                answer4=answer4,
                                )

    post_question_collection.insert_one(result)

    print("had got in here")
    return render_template('thank.html',**locals())
@app.route('/submit',methods=['POST'])
def submit():
    print("======== submit success ============")
    
    table_id = request.values['table_id']
    participant_id = request.values['participant_id']
    group = request.values['group']
    task_order = request.values['task_order']

    print("======== 1 ============")
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
    print("======== 2 ============")

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
    print("======== 3 ============")

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
    print("======== 4 ============")

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
    print("======== 5 ============")

    captcha_id0 = request.values['captcha_id0']
    captcha_id1_1 = request.values['captcha_id1_1']
    captcha_id1_2 = request.values['captcha_id1_2']
    captcha_id1_3 = request.values['captcha_id1_3']
    captcha_id2_1 = request.values['captcha_id2_1']
    captcha_id2_2 = request.values['captcha_id2_2']
    captcha_id2_3 = request.values['captcha_id2_3']
    captcha_id3_1 = request.values['captcha_id3_1']
    captcha_id3_2 = request.values['captcha_id3_2']
    captcha_id3_3 = request.values['captcha_id3_3']
    captcha_id4_1 = request.values['captcha_id4_1']
    captcha_id4_2 = request.values['captcha_id4_2']
    captcha_id4_3 = request.values['captcha_id4_3']
    print("======== 6 ============")

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
    print("======== 7 ============")

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
    print("======== 8 ============")


    likert_fb1_1 = request.values['likert_fb1_1']
    likert_fb1_2 = request.values['likert_fb1_2']
    # likert_fb1_3 = request.values['likert_fb1_3']
    text_fb1_1 = request.values['text_fb1_1']
    text_fb1_2 = request.values['text_fb1_2']
    text_fb1_3 = request.values['text_fb1_3']
    print("======== 9 ============")

    likert_fb2_1 = request.values['likert_fb2_1']
    likert_fb2_2 = request.values['likert_fb2_2']
    # likert_fb2_3 = request.values['likert_fb2_3']
    text_fb2_1 = request.values['text_fb2_1']
    text_fb2_2 = request.values['text_fb2_2']
    text_fb2_3 = request.values['text_fb2_3']
    print("======== 10 ============")

    likert_fb3_1 = request.values['likert_fb3_1']
    likert_fb3_2 = request.values['likert_fb3_2']
    # likert_fb3_3 = request.values['likert_fb3_3']
    text_fb3_1 = request.values['text_fb3_1']
    text_fb3_2 = request.values['text_fb3_2']
    text_fb3_3 = request.values['text_fb3_3']
    print("======== 11 ============")

    likert_fb4_1 = request.values['likert_fb4_1']
    likert_fb4_2 = request.values['likert_fb4_2']
    # likert_fb4_3 = request.values['likert_fb4_3']
    text_fb4_1 = request.values['text_fb4_1']
    text_fb4_2 = request.values['text_fb4_2']
    text_fb4_3 = request.values['text_fb4_3']

    print("======== 12 ============")

    dataJson = {}

    dataJson["practice"]    = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address0,captcha_id=captcha_id0,task_type=task_type0,ground_truth=ground_truth0,time=time_0, count=count_0, user_input=user_input0)
    dataJson["instance1_1"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address1_1,captcha_id=captcha_id1_1,task_type=task_type1_1,ground_truth=ground_truth1_1,time=time1_1, count=count1_1, user_input=user_input1_1)
    dataJson["instance1_2"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address1_2,captcha_id=captcha_id1_2,task_type=task_type1_2,ground_truth=ground_truth1_2,time=time1_2, count=count1_2, user_input=user_input1_2)
    dataJson["instance1_3"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address1_3,captcha_id=captcha_id1_3,task_type=task_type1_3,ground_truth=ground_truth1_3,time=time1_3, count=count1_3, user_input=user_input1_3)
    dataJson["feedback1"]   = dict(likert_fb1_1=likert_fb1_1, likert_fb1_2=likert_fb1_2, text_fb1_1=text_fb1_1, text_fb1_2=text_fb1_2, text_fb1_3=text_fb1_3)
    
    dataJson["instance2_1"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address2_1,captcha_id=captcha_id2_1,task_type=task_type2_1,ground_truth=ground_truth2_1,time=time2_1, count=count2_1, user_input=user_input2_1)
    dataJson["instance2_2"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address2_2,captcha_id=captcha_id2_2,task_type=task_type2_2,ground_truth=ground_truth2_2,time=time2_2, count=count2_2, user_input=user_input2_2)
    dataJson["instance2_3"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address2_3,captcha_id=captcha_id2_3,task_type=task_type2_3,ground_truth=ground_truth2_3,time=time2_3, count=count2_3, user_input=user_input2_3)
    dataJson["feedback2"]   = dict(likert_fb2_1=likert_fb2_1, likert_fb2_2=likert_fb2_2, text_fb2_1=text_fb2_1, text_fb2_2=text_fb2_2, text_fb2_3=text_fb2_3)
    
    dataJson["instance3_1"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address3_1,captcha_id=captcha_id3_1,task_type=task_type3_1,ground_truth=ground_truth3_1,time=time3_1, count=count3_1, user_input=user_input3_1)
    dataJson["instance3_2"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address3_2,captcha_id=captcha_id3_2,task_type=task_type3_2,ground_truth=ground_truth3_2,time=time3_2, count=count3_2, user_input=user_input3_2)
    dataJson["instance3_3"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address3_3,captcha_id=captcha_id3_3,task_type=task_type3_3,ground_truth=ground_truth3_3,time=time3_3, count=count3_3, user_input=user_input3_3)
    dataJson["feedback3"]   = dict(likert_fb3_1=likert_fb3_1, likert_fb3_2=likert_fb3_2, text_fb3_1=text_fb3_1, text_fb3_2=text_fb3_2, text_fb3_3=text_fb3_3)
    
    dataJson["instance4_1"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address4_1,captcha_id=captcha_id4_1,task_type=task_type4_1,ground_truth=ground_truth4_1,time=time4_1, count=count4_1, user_input=user_input4_1)
    dataJson["instance4_2"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address4_2,captcha_id=captcha_id4_2,task_type=task_type4_2,ground_truth=ground_truth4_2,time=time4_2, count=count4_2, user_input=user_input4_2)
    dataJson["instance4_3"] = dict(table_id=table_id,participant_id=participant_id,group=group,task_order=task_order,file_address=file_address4_3,captcha_id=captcha_id4_3,task_type=task_type4_3,ground_truth=ground_truth4_3,time=time4_3, count=count4_3, user_input=user_input4_3)
    dataJson["feedback4"]   = dict(likert_fb4_1=likert_fb4_1, likert_fb4_2=likert_fb4_2, text_fb4_1=text_fb4_1, text_fb4_2=text_fb4_2, text_fb4_3=text_fb4_3)
    
    task_data.insert_one(dataJson)

    # print(fname, lname, age, gender, email)

    return render_template('submit.html', async_mode=socketio.async_mode,
                                            table_id = table_id,
                                            participant_id = participant_id,
                                            group = group,
                                            task_order = task_order,
                                            file_address1_1 = file_address1_1,
                                            file_address2_1 = file_address2_1,
                                            file_address3_1 = file_address3_1,
                                            file_address4_1 = file_address4_1)


@app.route('/demographic_control',methods=['POST'])
def demographic_control():
    
    # fname   = request.values['fname']
    # lname   = request.values['lname']
    table_id = request.values['table_id']
    age     = request.values['age']
    gender  = request.values['gender']
    familiaritynum = request.values['familiaritynum']
    familiaritycaptcha = request.values['familiaritycaptcha']
    familiarityaudio = request.values['familiarityaudio']
    apparatus = request.values['apparatus']
    # email   = request.values['email']

    demographic = {}
    # demographic["fname"]    = fname
    # demographic["lname"]    = lname
    demographic["table_id"]    = table_id
    demographic["age"]      = age
    demographic["gender"]   = gender
    demographic["familiaritynum"]   = familiaritynum
    demographic["familiaritycaptcha"]   = familiaritycaptcha
    demographic["familiarityaudio"]   = familiarityaudio
    demographic["apparatus"]   = apparatus

    # demographic["email"]    = email
    demographic_data.insert_one(demographic)

    # get group, task order
    group = "test group"
    task_order = " test task order"
    
    # get participants_num
    res = preference_data.update_one({"_id": 'participants_num'}, {"$inc": {"count": 1}}, upsert =True)
    print(res.raw_result)
    doc  = preference_data.find_one({"_id": 'participants_num'})
    participants_num = doc["count"]

    participants_id = str(participants_num)


    # return render_template('tasks.html', async_mode=socketio.async_mode)

    return render_template('tasks.html', async_mode=socketio.async_mode,
                                        table_id        = table_id,
                                        participants_id = participants_id,
                                        group           = group,
                                        task_order      = task_order,
                                        
                                        practice       = "prototypes/practice.mp3",
                                        catpcha_id0    = "0",
                                        task_type0     = "N",
                                        ground_truth0  = "000000",

                                        instance1_1         = "prototypes/"+participants_id+"/", 
                                        catpcha_id1_1       = "0",
                                        task_type1_1        = "N",
                                        ground_truth1_1     = "000000",

                                        instance1_2 ="prototypes/"+participants_id+"/", 
                                        catpcha_id1_2       = "0",
                                        task_type1_2        = "N",
                                        ground_truth1_2     = "000000",

                                        instance1_3 ="prototypes/"+participants_id+"/", 
                                        catpcha_id1_3       = "0",
                                        task_type1_3        = "N",
                                        ground_truth1_3     = "000000",

                                        instance2_1 ="prototypes/"+participants_id+"/", 
                                        catpcha_id2_1       = "0",
                                        task_type2_1        = "N",
                                        ground_truth2_1     = "000000",

                                        instance2_2 ="prototypes/"+participants_id+"/", 
                                        catpcha_id2_2       = "0",
                                        task_type2_2        = "N",
                                        ground_truth2_2     = "000000",

                                        instance2_3 ="prototypes/"+participants_id+"/", 
                                        catpcha_id2_3       = "0",
                                        task_type2_3        = "N",
                                        ground_truth2_3     = "000000",

                                        instance3_1 ="prototypes/"+participants_id+"/", 
                                        catpcha_id3_1       = "0",
                                        task_type3_1        = "N",
                                        ground_truth3_1     = "000000",

                                        instance3_2 ="prototypes/"+participants_id+"/", 
                                        catpcha_id3_2       = "0",
                                        task_type3_2        = "N",
                                        ground_truth3_2     = "000000",

                                        instance3_3 ="prototypes/"+participants_id+"/", 
                                        catpcha_id3_3       = "0",
                                        task_type3_3        = "N",
                                        ground_truth3_3     = "000000",

                                        instance4_1 ="prototypes/"+participants_id+"/", 
                                        catpcha_id4_1       = "0",
                                        task_type4_1        = "N",
                                        ground_truth4_1     = "000000",

                                        instance4_2 ="prototypes/"+participants_id+"/", 
                                        catpcha_id4_2       = "0",
                                        task_type4_2        = "N",
                                        ground_truth4_2     = "000000",

                                        instance4_3         ="prototypes/"+participants_id+"/",
                                        catpcha_id4_3       = "0",
                                        task_type4_3        = "N",
                                        ground_truth4_3     = "000000")

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

if __name__ == '__main__':
    # initialize_counter()
    socketio.run(app, debug=False, host='0.0.0.0', port=5000)
