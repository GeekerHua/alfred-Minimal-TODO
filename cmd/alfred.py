# coding=utf-8

import os
import json
import sys

query = sys.argv[1]
path = sys.argv[2]


file = open(path, 'r')
res = []

querys = query.strip().replace("\ ", "  ").strip()


def searchList():
    tmpList = []
    i = 0
    for item in file.readlines():
        if item.replace('-', '').find(query) >= 0 and item != "\n":
            icon = './icon/uncheck.jpg'
            i += 1
            if item.startswith('-'):
                icon = './icon/check.jpg'
            tmpList.append({
                "valid": True,
                "title": str(i) + '.' + item,
                "subtitle": "enter --> 完成任务, cmd --> 删除任务 ctrl --> 恢复任务",
                "icon": {"path": icon},
                "arg": '[x]' + item,
                "mods": {
                    "ctrl": {
                        "valid": True,
                        "arg": '[@]' + item,
                        "subtitle": "reset"
                    },
                    "cmd": {
                        "valid": True,
                        "arg": '[-]' + item,
                        "subtitle": "delete"
                    },
                },
            })
    return tmpList


def appendAdd(info):
    res.append({
        "title": "-a  new todo",
        "subtitle": "add new todo '" + info + "'",
        "autocomplete": "-a ",
        "icon":{"path": "./icon/add.jpg"},
        "arg": "[+]" + info
    })


def resetAll(info):
    res.append({
        "title": "-r  reset all", 
        "subtitle": "reset all todo",
        "autocomplete": "-r",
        "icon": {"path": "./icon/reset.jpg"}, 
        "arg": "[r]"})


def clearAll(info):
    res.append({
        "title": "-c  clear all done", 
        "subtitle": "clear all done", 
        "autocomplete": "-c",
        "icon": {"path": "./icon/delete.png"}, 
        "arg": "[c]"})


actionList = [
    {"name": '-a',
     "function": appendAdd},
    {"name": '-r',
     "function": resetAll},
    {"name": '-c',
     "function": clearAll},
]

info = querys[3:]
if query.startswith('-'):  # 命令操作
    action = query.split('\ ')[0]
    for item in actionList:
        if item['name'].startswith(action):
            item['function'](info.strip())

else:
    resultList = searchList()
    if len(resultList) == 0:
        appendAdd(querys)
    else:
        res.extend(resultList)


file.close()
ret = json.dumps({"items": res})

print(ret)
