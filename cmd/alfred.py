# coding=utf-8

import json
import sys


def searchList(todo_list, q):
    tmpList = []
    for i, todo_item in enumerate(todo_list, 1):
        if q not in todo_item['title']:
            continue
        status = todo_item['status']
        title = todo_item['title'].strip()
        icon = './icon/check.png' if status == 'done' else './icon/uncheck.png'
        tmpList.append({
            "valid": True,
            "title": '{}. {}'.format(i, title),
            "subtitle": "enter --> 完成任务, cmd --> 删除任务 ctrl --> 恢复任务",
            "icon": {"path": icon},
            "arg": '[x]' + title,
            "mods": {
                "ctrl": {
                    "valid": True,
                    "arg": '[@]' + title,
                    "subtitle": "reset"
                },
                "cmd": {
                    "valid": True,
                    "arg": '[-]' + title,
                    "subtitle": "delete"
                },
            },
        })
    return tmpList


def appendAdd(item):
    res.append({
        "title": "-a  new todo",
        "subtitle": "add new todo '" + item + "'",
        "autocomplete": "-a ",
        "icon": {"path": "./icon/add.png"},
        "arg": "[+]" + item.strip()
    })


def resetAll(item):
    res.append({
        "title": "-r  reset all",
        "subtitle": "reset all todo",
        "autocomplete": "-r",
        "icon": {"path": "./icon/reset.png"},
        "arg": "[r]"})


def clearAll(item):
    res.append({
        "title": "-c  clear all done",
        "subtitle": "clear all done",
        "autocomplete": "-c",
        "icon": {"path": "./icon/delete.png"},
        "arg": "[c]"})


res = []

if __name__ == '__main__':

    query = sys.argv[1]
    path = sys.argv[2]
    actionList = {
        '-a': appendAdd,
        '-r': resetAll,
        '-c': clearAll,
    }
    querys = query.strip().strip()
    # print querys
    # info = querys
    info = querys[3:]
    if query.startswith('-'):
        action = query.split('\ ')[0]
        for key, func in actionList.items():
            if key.startswith(action):
                func(info.strip())
                break
    else:
        with open(path, 'r') as f:
            todo_list = json.load(f)
            resultList = searchList(todo_list, query)
            if resultList:
                res.extend(resultList)
            else:
                appendAdd(querys)
    print(json.dumps({"items": res}))
