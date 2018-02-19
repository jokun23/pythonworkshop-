DNA= open("DNA.txt").read()
count=0
count1=0
y=len(DNA)
for x in range (y-1,0,-1):
    if (DNA[x]=='C'):
        count=count+1

    elif (DNA[x]=='G'):
        count1=count1+1

h=count+count1
k=(float(h)/float(y))*100
print "The percentage of C+G is ",k,"%."


