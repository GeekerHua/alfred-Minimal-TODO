# coding=utf-8
import sys
query = sys.argv[1].strip()
path = sys.argv[2]
hasQuery = (len(query[3:]) > 0)


def writeFile(txt):
    newFile = open(path, 'w+')
    newFile.write(txt)
    newFile.close()


def handleTodo(func):
    def wrappendfunc():
        global query
        oldfile = open(path, 'r+')
        txt = ''
        query = query[3:]
        for item in oldfile.readlines():
            txt = func(item, txt)
        oldfile.close()
        writeFile(txt)
    return wrappendfunc

#  complete


@handleTodo
def complete(item, txt):
    if (item.strip() == query and not item.strip().startswith('-')):
        txt += ("-" + item)
    else:
        txt += item
    return txt


@handleTodo
def reset(item, txt):
    if (item.strip() == query and item.strip().startswith('-')):
        txt += item[1:]
    else:
        txt += item
    return txt


@handleTodo
def delete(item, txt):
    if item.strip() != query:
        txt += item
    return txt


@handleTodo
def resetAll(item, txt):
    txt += item.lstrip().replace('-', '')
    return txt


@handleTodo
def clearDone(item, txt):
    if not item.strip().startswith('-'):
        txt += item
    return txt


# 命令操作
# resetAll
if query.startswith('[r]'):
    resetAll()

# clearDone
if query.startswith('[c]'):
    clearDone()


# 单一操作
if not hasQuery:
    exit()

#  add todo
if query.startswith('[+]'):
    newFile = open(path, 'a')
    querys = query[3:].split('\ ')
    for query in querys:
        if len(query) > 0:
            newFile.write(query + '\n')
    newFile.close()

if query.startswith('[x]'):
    complete()

# reset
if query.startswith('[@]'):
    reset()

# delete
if query.startswith('[-]'):
    delete()
