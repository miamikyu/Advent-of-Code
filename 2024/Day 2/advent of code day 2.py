#advent of code day 2
#~~~~PART 1~~~~~#

'''

Check whether each row in the input file is safe.
There are 2 conditions:
1. Each row has to be all increasing or all decreasing
2. Each item in the row has to be within 1 or >=3 or the previous item

'''

file=open("testdata","r")

#function to split the file.
def splitfile(file):
    intdata=[]
    for line in file:
        data=line.split()
        intdata.append([int(x) for x in line.split()])
    return intdata
intdata=splitfile(file)
#testing clauses
print(intdata)


def condition1(intdata):
    saferow=True
    safedata=[]
    unsafedata=[]
    for row in intdata:
        for x in range(len(row)-1):
            if row[x]<row[x+1] or row[x]>row[x+1]:
                saferow=True
            else:
                saferow=False
        if saferow==True:
            safedata.append(row)
            print("safe",row)
        else:
            unsafedata.append(row)
            print("unsafe",row)
    return safedata, unsafedata

safedata, unsafedata=condition1(intdata)


def condition2(safedata,unsafedata):
    fullysaferow=True
    fullysafedata=[]
    diff=(1,2,3)
    for row in safedata:
        for x in range(len(row)-1):
            if abs(row[x]-row[x+1]) in diff:
                fullysaferow=True
            else:
                fullysaferow=False
        if fullysaferow==True:
            fullysafedata.append(row)
        else:
            unsafedata.append(row)
    return fullysafedata, unsafedata

fullysafedata, unsafedata=condition2(safedata,unsafedata)

file.close()


print(len(fullysafedata))
        
                
    



    



