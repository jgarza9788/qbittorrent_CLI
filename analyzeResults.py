import os

dir = os.path.dirname(__file__)

results = ''
with open(os.path.join(dir,"results.log"),"r") as Rlog:
    results = Rlog.read()

print(results.split('           '))
exit()

# # results = results.replace('Ã','')
# # results = results.replace('Ä','')
# # results = results.replace('Å','')
# # results = results.replace('Í','')
# # results = results.replace('Ø','')
# # results = results.replace('Õ','')
# # results = results.replace('Ñ','')
# # results = results.replace('Æµ','')
# # results = results.replace('³','   ')

# # print(results)
# # exit()

# # resultLines = results.split('³')
# resultLines = results.split('Ä´³')

# # print(resultLines)
# # exit()

# statuses = ['SU',' U','FU']

# thisJson = {}
# thisJson["torrents"] = []

# status = ''
# name = ''
# DL = ''
# UL = ''

# r = 0 
# i = 0 
# for l in resultLines:
#     # if 'Ä' not in l:
#     items = l.split('³')

#     status = items[0].replace(' ','')
#     name = items[1].replace(' ','')
#     DL = items[3].replace(' ','').replace('k','000').replace('m','000000').replace('B/s','')
#     UL = items[4].replace(' ','').replace('k','000').replace('m','000000').replace('B/s','')

#     # print(items[0] + ',' + items[1] + ',' + items[3] + ',' + items[4] + '\n')
#     print(status + ',' + name + ',' + DL + ',' + UL + '')

#     # print(str(i)+':')
#     # print(items)
#     # else:
        
#     # print(str(i) + ': ' + l)
#     # r += 1
#     i += 1