## Challenge Category:
**IR & Forensic**

## Challenge Name:
**Where Is My Mind?**

## Difficulty Level:
**Moderate**

## Description:
Elliot's mind is fractured, and he's starting to suspect that he's hiding something from himself. Can you help uncover what secrets he's trying to bury deep in his subconscious? Follow the hidden clues to reveal the truth.

**Note:** Ensure that the flag you submit always follows this exact format: `ACVCTF{secret}`.

---

## Solution:

1. We start by examining the file type of `fs0ciety.xyz`:
   
     ```bash
     file fs0ciety.xyz  
     ```
   
     ```plaintext
     fs0ciety.xyz: gzip compressed data, was "fs0ciety.xyz"
     ```
   
   This indicates the file is compressed using gzip.

2. Rename and decompress the file:
   
     ```bash
     mv fs0ciety.xyz fs0ciety.xyz.gz
     gunzip fs0ciety.xyz.gz
     ```
   
   After decompression, we recheck the file type:
   
     ```bash
     file fs0ciety.xyz
     ```
   
     ```plaintext
     fs0ciety.xyz: DOS/MBR boot sector, FAT (32 bit)
     ```
   
   This shows that it’s a FAT32 disk image with a hidden file structure.

3. The disk image can be mounted for easier exploration:
   
     ```bash
     mount fs0ciety.xyz /mnt/toto
     ```

4. Use `photorec` to scan and recover deleted files:
   
     ```bash
     photorec fs0ciety.xyz
     ```
   
   After scanning, we find a `.wav` file: `f0016104.wav`.

5. If you’ve watched *Mr. Robot*, you know that Elliot hides data using DeepSound in music files. Use `deepsound2john.py` to check for embedded data:
   
     ```bash
     deepsound2john.py f0016104.wav > robot.hash
     ```

6. To retrieve the hidden data, we need to crack the password using `john` and the `rockyou` wordlist with rules:
   
     ```bash
     john robot.hash --wordlist=/usr/share/wordlists/rockyou.txt --rules=best64
     ```
   
     ```plaintext
     f0016104.wav:klalderson01
     ```

7. Launch DeepSound with the password `klalderson01` to access the hidden data and retrieve the flag.

   ```plaintext
   Flag Secret: Th1s_1s_h0w_3ll1i0t_H1d3_Fil3s
   Final Flag: ACVCTF{Th1s_1s_h0w_3ll1i0t_H1d3_Fil3s}

---

## Hints:

- **Hint 1:** Remember the song "Where Is My Mind?" from Mr. Robot? The answer isn't where you'd expect—search in the hidden or less obvious places.
- **Hint 2:** What do you know about rules?
