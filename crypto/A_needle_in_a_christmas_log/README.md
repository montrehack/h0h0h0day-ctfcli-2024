# A needle in a christmas log

## Concept
The flag is encoded in a random base (16,32,64 or 85) and is then put in an array of random strings encoded with the same base, at a random position forming a "layer" of encoding. Then this array is stringified to be reencoded in another random base and put in a random index among random strings encoded with the same base (another layer), and so on.. 

There is an encoded flag example file but if you want to run another one you can just skip to "Encoding the flag", the example went through 30 rounds of various encoding with a total size of 23Mb (uncompressed). Thus, decoding it manually (figure out which of the 4 encoding will works+decoding) will really be time consuming, you can automate it (with a couple lines of Python such as shown in the src directory) and hopefully, after the 5 first layers, the players will start to loose hope doing that not knowing how many layers there are. 

## Schema
```
Step 1
                              flag 
                                |
                                V
[random_string1,random_string2,    ,random_string3,random_string4]
Step 2
baserandom = base16 or base32 or base64 or base85
[baserandom(random_string1),baserandom(random_string2),baserandom(flag),baserandom(random_string3),baserandom(random_string4)]
step 3
2 being the index of the flag in the array
encoding layer = "[baserandom(random_string1),baserandom(random_string2),baserandom(flag),baserandom(random_string3),baserandom(random_string4)][2]"
Step 4
Return to step 1 and consider "encoding layer" as your new "flag", repeat the process as much as possible. 
```

## Requirements 

None, this is litterally made out of builtin code, was built with Python 3.12. Should be fine as long as it is Python 3 

## Encoding the flag
Start a Python interpreter in the src folder
```Python
from main import encode
with open("../encoded_flag.txt", "w") as file:
    # Number of layers 20
    # Minimum length of a generated array 2
    # Maximum length of a generated array 10
    file.write(encode("\\INSERT FLAG HERE\\", 20,2,10))
``` 

## Decoding the flag
Start a Python interpreter in the src folder
```Python
from main import decode
with open("../encoded_flag.txt", "r") as file:
    encoded_flag = file.read()

with open("../decoded_flag.txt", "w") as file:
    # The decoder is bruteforcing any encoding, breaking 
    # through unlimited number of layers until it find the flag 
    # thanks to regex 
    file.write(decode(encoded_flag))
``` 

## Perfomances concerns 
~~Please consider before going on more than 8 encryption layers, the produced size of the encoded flag is exponential as well as the time of the encoding process. Encoding 7 layers take 1mn on a decent computer with an output file of 280mb, decoding took 5sec. Encoding 8 layers take 4mn on the same computer, decoding took 19sec and I did not even checked the size of the output file.  ~~ Was with same lenght on random strings, can now run fine.  
