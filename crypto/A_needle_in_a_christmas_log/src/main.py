#!/bin/python3
import base64 as b64
import random as rd
from string import ascii_letters, digits
import os
import re
import time

COMPLIANT_STRING_REGEX = re.compile(r"^\[.*\]\[\d+\]$")
FLAG_REGEX = re.compile(r"flag\{.*\}")


def encode(flag, layers, min_arr_len, max_arr_len):
    init_string = flag
    for layer in range(layers):
        random_arr_len = rd.randint(min_arr_len, max_arr_len)
        random_inserting_index = rd.randint(0, random_arr_len-1)
        arr = list()
        for j in range(random_arr_len):
            encoder = rd.choice([b64.b16encode, b64.b32encode, b64.b64encode, b64.b85encode])
            if j == random_inserting_index:
                arr.append(encoder(init_string.encode()).decode())
            else:
                # Lenght of generated string was initially the same size as init_string but it turned out to inflate the 
                # encoded flag too much with so little rounds so I set it to a small fixed size 
                arr.append(encoder((''.join(rd.choice(ascii_letters+digits) for _ in range(3)).encode())).decode())
        init_string = f"{arr}[{random_inserting_index}]"
    return init_string

def decode(encoded_string):
    possible_encodings = {
        "Base16": lambda s: b64.b16decode(s),
        "Base32": lambda s: b64.b32decode(s),
        "Base64": lambda s: b64.b64decode(s),
        "Base85": lambda s: b64.b85decode(s),
    }
    subencoded_string = eval(encoded_string)
    while True:
        for func_name, decode_func in possible_encodings.items():
            try:
                subencoded_string = decode_func(subencoded_string).decode()
                if FLAG_REGEX.match(subencoded_string):
                    return subencoded_string
                elif not COMPLIANT_STRING_REGEX.match(subencoded_string):
                    break
                else:
                    subencoded_string = eval(subencoded_string)
            except Exception:
                continue
    return "Wrong Format"


# def main():
#     curr_path = os.path.dirname(os.path.realpath(__file__))
#     with open(os.path.join(curr_path, "../christmas_log.txt"), "r") as content_to_code:
#         flag = content_to_code.readlines()[0]
#     start_encoding = time.time()
#     mychall = encode(flag,7,2,10)
#     print(f"encoding took {time.time()-start_encoding}")
#     with open(os.path.join(curr_path, "../output.txt"), "w") as file:
#         file.write(mychall)
#     start_decoding = time.time()
#     print(decode(mychall))
#     print(f"decoding took {time.time()-start_decoding}")

# main()    
    
