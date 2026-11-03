s1=float(input('Score1 '))
s2=float(input('Score2 '))
s3=float(input('Score3 '))
s4=float(input('Score4 '))
if(s1<s2 and s1<s3 and s1<s4):
    print('min. ',s1)
elif(s2<s1 and s2<s3 and s2<s4):
    print('min. ',s2)
elif(s3<s1 and s3<s2 and s3<s4):
    print('min. ',s3)
elif(s4<s1 and s4<s3 and s4<s1):
    print('min. ',s4)

