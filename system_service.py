"""The module returns the time, the ram information and the hdd infomation of the computer"""
import time
import json
from flask import Flask, Response
import psutil

APP = Flask(__name__)

@APP.route('/time')
def get_time():
    """The function is used to get time information of the computer"""
    time_int = {}
    time_int['time'] = int(time.time())
    response = Response(json.dumps(time_int))
    response.headers["Content-Type"] = "application/json"
    return response

@APP.route('/ram')
def get_ram():
    """The function is used to get RAM information of the computer"""
    mem = psutil.virtual_memory()
    mem_str = {}
    mem_str['total'] = int(mem.total/1024/1024)
    mem_str['used'] = int(mem.used/1024/1024)
    response = Response(json.dumps(mem_str))
    response.headers["Content-Type"] = "application/json"
    return response

@APP.route('/hdd')
def get_hdd():
    """The function is used to get HDD information of the computer"""
    hdd = psutil.disk_usage('/')
    hdd_str = {}
    hdd_str['total'] = int(hdd.total/1024/1024)
    hdd_str['used'] = int(hdd.used/1024/1024)
    response = Response(json.dumps(hdd_str))
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    APP.run()
