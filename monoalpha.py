l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("---Sender---")
msg=input("enter message to send:")
key=int(input("enter cipher key number:"))
print("--Encrypting and sending---")
enc=''
dec=''
for i in msg.lower():
	if i==' ':
		enc+=' '
		continue
	elif i.isdigit():
		enc+=str(int(i)+key)
		continue
	enc+=l[((l.index(i)%26)+key)%26]
print("cipher text as:"+enc)

print("---Reciever---")
key2=int(input("enter key to decrypt:"))
if key!=key2:
	print("Sorry...wrong key")
else:
	for i in enc:
		if i==' ':
			dec+=' '
			continue
		elif i.isdigit():
			dec+=str(int(i)-key)
			continue
		dec+=l[((l.index(i)%26)-key)%26]
		print("Tes :"dec())
	print("The plain text is:"+dec.upper())

		
