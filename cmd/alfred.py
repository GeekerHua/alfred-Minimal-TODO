# coding=utf-8

import json
import sys


def searchList(fs, q):
    tmpList = []
    i = 0
    for item in fs.readlines():
        if q in item:
            i += 1
            icon = './icon/check.png' if item.startswith('-') else './icon/uncheck.png'
            tmpList.append({
                "valid": True,
                "title": str(i) + '.' + item,
                "subtitle": "enter --> 完成任务, cmd --> 删除任务 ctrl --> 恢复任务",
                "icon": {"path": icon},
                "arg": '[x]' + item,
                "mods": {
                    "ctrl": {
                        "valid": True,
                        "arg": '[@]' + item.strip(),
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

    with open(path, 'r') as f:
        querys = query.strip().replace("\ ", "  ").strip()
        info = querys[3:]
        if query.startswith('-'):
            action = query.split('\ ')[0]
            for key, func in actionList.items():
                if key.startswith(action):
                    func(info.strip())
        else:
            resultList = searchList(f, query)
            if len(resultList) == 0:
                appendAdd(querys)
            else:
                res.extend(resultList)

        print json.dumps({"items": res})
