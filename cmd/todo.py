# coding=utf-8
import sys
import json
import copy


def operate_todo(operate, txt):
    with open(path) as f:
        todo_list = json.load(f)
    if originQuery.startswith('[+]'):
        todo_list.append({
            'status': 'wait',
            'title': txt
        })
    elif originQuery.startswith('[x]'):
        for item in todo_list:
            if item['title'] == txt:
                item['status'] = 'done'
                break
    elif originQuery.startswith('[@]'):
        for item in todo_list:
            if item['title'] == txt:
                item['status'] = 'wait'
                break
    elif originQuery.startswith('[-]'):
        index = None
        for i, item in enumerate(todo_list):
            if item['title'] == txt:
                index = i
                break
        del todo_list[index]
    elif originQuery.startswith('[r]'):
        for item in todo_list:
            item['status'] = 'wait'
    elif originQuery.startswith('[c]'):
        todo_list = [todo for todo in todo_list if todo['status'] != 'done']
    else:
        return
    with open(path, 'w') as f:
        json.dump(todo_list, f)


if __name__ == '__main__':
    originQuery = sys.argv[1].strip()
    path = sys.argv[2]
    query = originQuery[3:].strip()
    operate = originQuery[:3]
    operate_todo(operate, query)
