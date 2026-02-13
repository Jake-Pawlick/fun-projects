#A program that takes input for a md5 hash, and looks to match the first part of the hash with a user input
import hashlib
import keyboard
import time
text = input("hi, welcome to the hash md5 pattern finder. What would you like to be the main text to be hashed?: ")
numb = input("What would you like the hashed text to start with?: ")
length = len(numb)
i=0
print("beginning hash search in 3 seconds... press escape at anytime to stop")
time.sleep(3)
start_time = time.perf_counter()
while True:
    if keyboard.is_pressed('esc'):
        print("ESC pressed, stopping.")
        break
    string = text + str(i)
    data = string.encode()
    res = hashlib.md5(data)
    res = res.hexdigest()
    if res[0:length] == numb:
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(string,i,res,"-"*10,f"Took {elapsed_time:.4f} seconds to find!")
        break
    print (i)
    i+=1