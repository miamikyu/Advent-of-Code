#advent of code day 1
file=open("input","r")

#create empty lists
leftlist=[]
rightlist=[]
#function to read a file a split it in half
def split(file):
    for line in file:
        data=line.split()
        leftlist.append(int(data[0]))
        rightlist.append(int(data[1]))
    return leftlist, rightlist


leftlist,rightlist = split(file)

#sort the lists smallest to largest
sortedleftlist=sorted(leftlist)
sortedrightlist=sorted(rightlist)

#set total distance var
totaldistance=0

#find the difference between each pair in the sorted lists
for x in range (len(sortedleftlist)):
    if sortedleftlist[x]>sortedrightlist[x]:
        totaldistance=totaldistance+(sortedleftlist[x]-sortedrightlist[x])
    elif sortedleftlist[x]<sortedrightlist[x]:
        totaldistance=totaldistance+(sortedrightlist[x]-sortedleftlist[x])

        
#print the answer to the solution - got the correct answer 
print(totaldistance)


#~~~~~~~PART 2~~~~~~~~~#

#create similarity score var
similarityscore=0

#count var
count=0
#find out how many times each number in the left list appears in the right list 
#times the number by the amount of times in the list to get similarity score

for y in range (len(sortedleftlist)):


    if sortedleftlist[y] in sortedrightlist:
        count=sortedrightlist.count(sortedleftlist[y])

        similarityscore+=(sortedleftlist[y]*count)
    count=0
    

#print total similarity score
print(similarityscore)