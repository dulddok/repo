tupledata = ('dave', 'fun-coding', 'endless')
print(tupledata[1:3])
listdata = list(tupledata)
listdata.append('fun-codingnew')
tupledata = tuple(listdata)
print(tupledata)

tupledata = tuple()
listdata = list()
dictdata = dict()

print(type(tupledata),type(listdata), type(dictdata))

dictdata = {'environment':'환경', 'company':'회사','government':'정치'}
print(dictdata)
for data in dictdata.keys():
    print(data,":", dictdata[data])
dictdata = {'environment':['환경','PO'], 'company':['회사','X'],'governmen':['정치','X']}
for data in dictdata.keys():
    if dictdata[data][1] == 'X':
        print(data)

