from threading import Lock
from typing import Dict
from flask import Flask, render_template, session, request, \
    copy_current_request_context, send_from_directory
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import time, os, glob, json
import numpy as np
from itertools import permutations
import random
import pymongo
# 'mongodb+srv://advcaptcha:hankhaopinlee@cluster0.j1zm5.gcp.mongodb.net'
mongo_url = 'mongodb+srv://advcaptcha:hankhaopinlee@cluster0.j1zm5.gcp.mongodb.net'
my_client = pymongo.MongoClient(mongo_url)
mydb = my_client["advcaptcha"]

mycol = mydb["forms"]


groupA_count = {}
groupB_count = {}
groupC_count = {}

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

id_used_record = {"A":[], "B":[], "C":[]}

def join_tuple_string(strings_tuple) -> str:
   return ''.join(strings_tuple)
def initialize_counter():
    # Baseline -> B
    # Kenan -> K
    # Devil -> D
    # Mix (Kenan+Devil)-> M
    permutation = list(permutations("BKDM",4))
    names = map(join_tuple_string, permutation)

    for name in names:
        groupA_count[name] = 0
        groupB_count[name] = 0
        groupC_count[name] = 0

@app.route('/submit',methods=['POST'])
def submit():
    print("======== submit success ============")
    time_0 = request.values['0']
    time_11 = request.values['11']
    time_12 = request.values['12']
    time_13 = request.values['13']
    time_21 = request.values['21']
    time_22 = request.values['22']
    time_23 = request.values['23']
    time_31 = request.values['31']
    time_32 = request.values['32']
    time_33 = request.values['33']
    time_41 = request.values['41']
    time_42 = request.values['42']
    time_43 = request.values['43']

    count_0 = request.values['c0']
    count_11 = request.values['c11']
    count_12 = request.values['c12']
    count_13 = request.values['c13']
    count_21 = request.values['c21']
    count_22 = request.values['c22']
    count_23 = request.values['c23']
    count_31 = request.values['c31']
    count_32 = request.values['c32']
    count_33 = request.values['c33']
    count_41 = request.values['c41']
    count_42 = request.values['c42']
    count_43 = request.values['c43']

    pro0 = request.values['pro0']
    pro1_1 = request.values['pro1_1']
    pro1_2 = request.values['pro1_2']
    pro1_3 = request.values['pro1_3']
    pro2_1 = request.values['pro2_1']
    pro2_2 = request.values['pro2_2']
    pro2_3 = request.values['pro2_3']
    pro3_1 = request.values['pro3_1']
    pro3_2 = request.values['pro3_2']
    pro3_3 = request.values['pro3_3']
    pro4_1 = request.values['pro4_1']
    pro4_2 = request.values['pro4_2']
    pro4_3 = request.values['pro4_3']

    likert_fb1_1 = request.values['likert_fb1_1']
    likert_fb1_2 = request.values['likert_fb1_2']
    likert_fb1_3 = request.values['likert_fb1_3']
    text_fb1_1 = request.values['text_fb1_1']
    text_fb1_2 = request.values['text_fb1_2']

    likert_fb2_1 = request.values['likert_fb2_1']
    likert_fb2_2 = request.values['likert_fb2_2']
    likert_fb2_3 = request.values['likert_fb2_3']
    text_fb2_1 = request.values['text_fb2_1']
    text_fb2_2 = request.values['text_fb2_2']

    likert_fb3_1 = request.values['likert_fb3_1']
    likert_fb3_2 = request.values['likert_fb3_2']
    likert_fb3_3 = request.values['likert_fb3_3']
    text_fb3_1 = request.values['text_fb3_1']
    text_fb3_2 = request.values['text_fb3_2']

    likert_fb4_1 = request.values['likert_fb4_1']
    likert_fb4_2 = request.values['likert_fb4_2']
    likert_fb4_3 = request.values['likert_fb4_3']
    text_fb4_1 = request.values['text_fb4_1']
    text_fb4_2 = request.values['text_fb4_2']

    # fname   = request.values['fname']
    # lname   = request.values['lname']
    # age     = request.values['age']
    # gender  = request.values['gender']
    # email   = request.values['email']
    # group = request.values['group']
    # order = request.values['order']
    # id1 = request.values['id1']
    # id2 = request.values['id2']
    # id3 = request.values['id3']

    # if group == "A": groupA_count[order] +=1
    # elif group == "B": groupB_count[order] +=1
    # elif group == "C": groupC_count[order] +=1
    # id_used_record[group].append(id1)
    # id_used_record[group].append(id2)
    # id_used_record[group].append(id3)
    # print(group, order, id1, id2, id3)
    
    # pack all responses to json
    dataJson = {}
    # dataJson["fname"] = fname
    # dataJson["lname"] = lname
    # dataJson["age"] = age
    # dataJson["gender"] = gender
    # dataJson["email"] = email

    dataJson["practice"] = dict(time=time_0, count=count_0, text=pro0)
    dataJson["instance1_1"] = dict(time=time_11, count=count_11, text=pro1_1)
    dataJson["instance1_2"] = dict(time=time_12, count=count_12, text=pro1_2)
    dataJson["instance1_3"] = dict(time=time_13, count=count_13, text=pro1_3)
    dataJson["feedback1"] = dict(likert_fb1_1=likert_fb1_1, likert_fb1_2=likert_fb1_2, likert_fb1_3=likert_fb1_3, text_fb1_1=text_fb1_1, text_fb1_2=text_fb1_2)
    
    dataJson["instance2_1"] = dict(time=time_21, count=count_21, text=pro2_1)
    dataJson["instance2_2"] = dict(time=time_22, count=count_22, text=pro2_2)
    dataJson["instance2_3"] = dict(time=time_23, count=count_23, text=pro2_3)
    dataJson["feedback2"] = dict(likert_fb2_1=likert_fb2_1, likert_fb2_2=likert_fb2_2, likert_fb2_3=likert_fb2_3, text_fb2_1=text_fb2_1, text_fb2_2=text_fb2_2)
    
    dataJson["instance3_1"] = dict(time=time_31, count=count_31, text=pro3_1)
    dataJson["instance3_2"] = dict(time=time_32, count=count_32, text=pro3_2)
    dataJson["instance3_3"] = dict(time=time_33, count=count_33, text=pro3_3)
    dataJson["feedback3"] = dict(likert_fb3_1=likert_fb3_1, likert_fb3_2=likert_fb3_2, likert_fb3_3=likert_fb3_3, text_fb3_1=text_fb3_1, text_fb3_2=text_fb3_2)
    
    dataJson["instance4_1"] = dict(time=time_41, count=count_41, text=pro4_1)
    dataJson["instance4_2"] = dict(time=time_42, count=count_42, text=pro4_2)
    dataJson["instance4_3"] = dict(time=time_43, count=count_43, text=pro4_3)
    dataJson["feedback4"] = dict(likert_fb4_1=likert_fb4_1, likert_fb4_2=likert_fb4_2, likert_fb4_3=likert_fb4_3, text_fb4_1=text_fb4_1, text_fb4_2=text_fb4_2)
    
    mycol.insert_one(dataJson)

    print(fname, lname, age, gender, email)

    return render_template('submit.html',**locals())


@app.route('/demographic_control',methods=['POST'])
def demographic_control():
    fname   = request.values['fname']
    lname   = request.values['lname']
    age     = request.values['age']
    gender  = request.values['gender']
    email   = request.values['email']

    demographic = {}
    demographic["fname"]    = fname
    demographic["lname"]    = lname
    demographic["age"]      = age
    demographic["gender"]   = gender
    demographic["email"]    = email

    print(fname, lname, age,gender, email)

    return render_template('tasks.html', async_mode=socketio.async_mode)

    # return render_template('tasks.html', group = group,
    #                                     order = order,
    #                                     id1 = str(ids[0]),
    #                                     id2 = str(ids[1]),
    #                                     id3 = str(ids[2]),
    #                                     practice= "prototypes/prototype1/Math_Only_Add.mp3",
    #                                     instance1_1 ="prototypes/group"+group+"/"+instance_1+"/"+str(ids[0]), 
    #                                     instance1_2 ="prototypes/group"+group+"/"+instance_1+"/"+str(ids[1]), 
    #                                     instance1_3 ="prototypes/group"+group+"/"+instance_1+"/"+str(ids[2]), 

    #                                     instance2_1 ="prototypes/group"+group+"/"+instance_2+"/"+str(ids[0]), 
    #                                     instance2_2 ="prototypes/group"+group+"/"+instance_2+"/"+str(ids[1]), 
    #                                     instance2_3 ="prototypes/group"+group+"/"+instance_2+"/"+str(ids[2]), 

    #                                     instance3_1 ="prototypes/group"+group+"/"+instance_3+"/"+str(ids[0]), 
    #                                     instance3_2 ="prototypes/group"+group+"/"+instance_3+"/"+str(ids[1]), 
    #                                     instance3_3 ="prototypes/group"+group+"/"+instance_3+"/"+str(ids[2]), 

    #                                     instance4_1 ="prototypes/group"+group+"/"+instance_4+"/"+str(ids[0]), 
    #                                     instance4_2 ="prototypes/group"+group+"/"+instance_4+"/"+str(ids[1]), 
    #                                     instance4_3 ="prototypes/group"+group+"/"+instance_4+"/"+str(ids[2]), )

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


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
    initialize_counter()
    socketio.run(app, debug=False, host="0.0.0.0", port=5000)
