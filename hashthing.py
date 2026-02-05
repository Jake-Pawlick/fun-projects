#A program that takes input for a md5 hash, and looks to match the first part of the hash with a user input
import hashlib
text = input("hi, welcome to the hash md5 pattern finder. What would you like to be the main text to be hashed?: ")
numb = input("What would you like the hashed text to start with?: ")
length = len(numb)
i=0
while True:
    string = text + str(i)
    data = string.encode()
    res = hashlib.md5(data)
    res = res.hexdigest()
    if res[0:length] == numb:
        print(string,i,res)
        break
    i+=1
