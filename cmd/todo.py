# coding=utf-8
import sys


def dealTodo(func):
    with open(path, 'r+') as oldFile:
        txt = ''
        for oldLine in oldFile.readlines():
            txt = func(oldLine.strip(), txt) + '\n'
        with open(path, 'w+') as newFile:
            newFile.write(txt)


def complete(item, txt):
    if item == query and not item.startswith('-'):
        txt += ("-" + item)
    else:
        txt += item
    return txt


def reset(item, txt):
    if item == query and item.startswith('-'):
        txt += item[1:]
    else:
        txt += item
    return txt


def delete(item, txt):
    if item != query:
        txt += item
    return txt


def resetAll(item, txt):
    txt += item.replace('-', '')
    return txt


def clearDone(item, txt):
    if not item.startswith('-'):
        txt += item
    return txt


if __name__ == '__main__':
    originQuery = sys.argv[1].strip()
    path = sys.argv[2]
    query = originQuery[3:]
    hasQuery = (len(query) > 0)

    if hasQuery:
        if originQuery.startswith('[+]'):
            with open(path, 'a') as f:
                queryList = query.split('\ ')
                for line in queryList:  # 多行添加
                    if len(line) > 0:
                        f.write(line + '\n')
        elif originQuery.startswith('[x]'):
            dealTodo(complete)
        elif originQuery.startswith('[@]'):
            dealTodo(reset)
        elif originQuery.startswith('[-]'):
            dealTodo(delete)
    else:
        if originQuery.startswith('[r]'):
            dealTodo(resetAll)
        elif originQuery.startswith('[c]'):
            dealTodo(clearDone)
