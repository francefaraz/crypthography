import random
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("---Sender---")
msg=input("enter message to send:")
print("--Encrypting and sending---")
enc=''
dec=''
key1=len(msg)
key=[]
for i in range(key1):
    key.append(random.randint(0,25))
j=0;
for i in msg.lower():

    if i==' ':
        enc+=' '
        j=j+1
        continue
    elif i.isdigit():
        enc+=str(int(i))
        j=j+1
        continue
    enc+=l[((l.index(i)%26)+key[j])%26]
    j=j+1
print("cipher text as:"+enc)

print("---Reciever---")
j=0
for i in enc:
    if i==' ':
        dec+=' '
        j=j+1
        continue
    elif i.isdigit():
        dec+=str(int(i))
        j=j+1
        continue
    dec+=l[((l.index(i)%26)-key[j])%26]
    j=j+1
    print("The plain text is:"+dec.upper())
