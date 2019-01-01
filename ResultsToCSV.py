import os,JSON2CSV,pprint,time
# import sys
# sys.path.insert(0,r'D:..path2module')
# import module



dir = os.path.dirname(__file__)
pp = pprint.PrettyPrinter(indent=4)


# os.startfile(os.path.join(dir,'getCurrentList.cmd'))
# time.sleep(10)

results = ''
with open(os.path.join(dir,"results.log"),"r") as Rlog:
    results = Rlog.read()

# print(results.split('           '))
# exit()

resultsList0 = results.split('           ')

finalResults = {}
finalResults['items'] = []

recordDateTime = 'unknown'

for i in resultsList0 :

    if len(i) > 0  :
        if "Name:" in i:
            finalResults['items'].append({})
            finalResults['items'][len(finalResults['items'])-1]['DateTime'] = recordDateTime

        if "datetime" in i:
            recordDateTime = i.replace('datetime:  ','').replace('\n','').rstrip().lstrip()
            continue


        i = i.rstrip().lstrip().split(':')

        if len(i) == 3:
            # print(i)
            i[1] = "D:" + i[2]
        
        # print(i[0])
        if "Speed" in i[0]:
            i[1] = i[1].replace(' ','').replace('B/s','').replace('k','000').replace('m','000000')
            # print(i)

        # print(i)

        try:
            finalResults['items'][len(finalResults['items'])-1][i[0]] = i[1].lstrip().rstrip()
        except:
            print(i)



pp.pprint(finalResults)

JSON2CSV.exportCSV('Results.csv',finalResults['items'])
