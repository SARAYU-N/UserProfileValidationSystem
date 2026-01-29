print("Kindly enter following details!")
FullName=input("your full name:")
EmailId=input("your email ID:")
Num=input("your mobile number:")
age=int(input("your age:"))

flen=len(FullName)
mlen=len(Num)

mdigits=Num.count('0')+Num.count('1')+Num.count('2')+Num.count('3')+Num.count('4')+Num.count('5')+Num.count('6')+Num.count('7')+Num.count('8')+Num.count('9')
if(FullName.count(" ")==0):
    print("User profile is INVALID")
elif(FullName[0]==' ' or FullName[mlen-1]==' '):
    print("User profile is INVALID")
elif(EmailId.count('@')==0 or EmailId.count('.')==0 or EmailId[0]=='@'):
    print("User profile is INVALID")
elif(mlen!=10 or mdigits!=10 or Num[0]==0):
    print("User profile is INVALID")
elif(age>60 or age<18):
    print("User profile is INVALID")
else:
    print("User profile is VALID")