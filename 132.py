s1='HARISH'
s2='KUMAR'
i,j=0,0
output=''
while i<len(s1) and j<len(s2):
    output=output+s1[i]+s2[i]
    i=i+1
    j=j+1
print(output)    



s1=input('enter the str:')
s2=input('enter the str:')
i,j=0,0
output =''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)        