a=input("Enter the Message")
key=2

enc=''
dec=''
print("Sender Msg is "+a)
print("Text is going to encryptt.....")
for i in a:
	n=ord(i)
	if i!=' ':
		n+=key
	enc+=chr(n)
print("encrypted text is "+enc)

key1=int(input("Enter KEy"))
if key!=key1:
	print("Entered Key is wrongg....")
else:
	print("Received msg is going to  Decrypt ")
	for i in enc:
	    n=ord(i)
	    if i!=' ':
	        n-=key
	    dec+=chr(n)
	print("decrypted text is "+dec)
