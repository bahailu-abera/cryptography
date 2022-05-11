def maper(text,change=False):
 value=str()
 trans=dict()
 trans={'a':'10','b':'11','c':'12','d':'13','e':'14','f':'15','g':'16','h':'17','i':'18','j':'19','k':'20','l':'21','m':'22','n':'23','o':'24','p':'25','q':'26','r':'27','s':'28','t':'29','u':'30','v':'31','w':'32','x':'33','y':'34','z':'35',' ':'36'}
 if not change:
  for letter in text:
   value+=trans[letter]
  return value
 else:
  temp=dict()
  for k,v in trans.items():
   temp[v]=k
  for num in text:
   if num in temp:
    lett=temp[num]
    value+=lett
  return value
 
def mod(m,e,n):
 if e==0:
  return 1
 ans=mod(m,e//2,n)
 ans=(ans*ans)%n
 if e%2==1:
  ans=(ans*m)%n
 return ans

def multInverse(e=13,p=4176):
 r1=e
 r2=p
 if(r1<r2):
  (r1,r2)=(r2,r1)
 t1=0
 t2=1
 while(r1>1):
  r=r1%r2
  q=r1//r2
  r1=r2
  r2=r
  t=t1-(q*t2)
  t1=t2
  t2=t
 if t1<0:
  t1+=p
 
 return t1
 
def createBlock(newtext,temp=[ ] ):
 length=len(newtext)
 if length==2:
  
  temp.append(newtext)
  return temp
 if length==0:
  return temp
 else:
  block=newtext[:2]
  temp.append(block)
   
  return createBlock(newtext[2:],temp)
  
def encrypt(lst,e=13,n=4307):
 
 str1=[]
 for num in lst:
    
    encry=mod(int(num),e,n)
    str1.append(encry)
    
 
 return str1
 
def decrption(enc,d,n=4307):

 temp=[ ]
 
 for num in enc:
  modulo=mod(num,d,n)
  temp.append(modulo)
  
 return temp
def unblock(blockes):
 string=str()
 for block in blockes:
  string+=str(block)
 i=0
 temp=[ ]
 while i<len(string):
  temp.append(string[i:i+2])
  i+=2
 v=maper(temp,True)
 
 return v
 
def isPrime(p,q):
    count=2
    while count<=p**0.5:
        if p%count==0:
            return False
        count+=1
    count=2
    while count<=q**0.5:
        if q%count==0:
            return False
        count+=1
    return True

def isRelativePrime(e,t):
    if t==0:
        if e==1:
            return True
        return False
    return isRelativePrime(t,e%t)
    
    

  
  
 
  
message=input("enter the message\n")
message=message.lower()
print("if you want to choose the key press yes else press n")

option=input()
if option=="yes":
    p=int(input("enter the first prime number \n"))
    q=int(input("enter the next prime number \n"))
    e=int(input("enter the the public key\n"))
    n=p*q
    t=(p-1)*(q-1)
    while not isPrime(p,q) or not isRelativePrime(e,t):
        cond=input("enter yes  to exit else no to try for the correct prime numbers\n")
        if cond=="yes":
            print("you exit from the ")
            exit()
        else:
            p=int(input("enter the first prime number \n"))
            q=int(input("enter the next prime number \n"))
            e=int(input("enter the the public key\n"))
            n=p*q
            t=(p-1)*(q-1)
    res=maper(message)
    d=multInverse(e,t)
    x=createBlock(res)
    enc=encrypt(x,e,n)
    value=decrption(enc,d,n)
    changed=unblock(value)

else:
    res=maper(message)
    x=createBlock(res)
    enc=encrypt(x)
    d=multInverse()
    value=decrption(enc,d)
    changed=unblock(value)

newValue=str()
for lst in value:
 newValue+=str(lst)
 
newEnc=str( )
for lst in enc:
 newEnc+=str(lst)
 


print("the plaintext in number format:\n",res)

print("the plaintext after encryption in number format is:\n",newEnc)

print("the plaintext after decryption in number format is:\n",newValue)

print("the actual text is:",changed)
