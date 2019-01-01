import os

dir = os.path.dirname(__file__)

def exportCSV(CSVname,JsonList):
    CSV = open(os.path.join(dir,CSVname),'w')

    i = 0 
    header = ''
    while i < len(JsonList):
        for key, value in JsonList[i].items():
            if key not in header:
                header = header + key + ','
        i += 1

    CSV.write(header[:-1]+'\n')

    colList =  header.split(',')

    i = 0 
    while i < len(JsonList):
        line = ''
        for c in colList:
            thisValue = ''
            for key, value in JsonList[i].items():
                if c == key:
                    thisValue = '\"' + str(value) + '\"'
            line = line + thisValue + ','

        CSV.write(line + '\n')
        i += 1

    CSV.close()


#unit test
if __name__ == '__main__':
    thisJSON = {}
    thisJSON['items'] = []

    thisJSON['items'].append(
        {
        'ID': 1    
        }
    )

    thisJSON['items'].append(
        {
        'ID': 1,    
        'Path': 'D:thisthis',
        'List': [1,2,3]
        }
    )

    thisJSON['items'].append(
        {
        'ID': 1,    
        'List': [1,2,3]
        }
    )
    

    thisJSON['items'].append(
        {
        'ID': 1,    
        'num': 100
        }
    )

    exportCSV("test.csv",thisJSON['items'])
    
