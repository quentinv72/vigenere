Quick and dirty Vigenere deciphering tool.

Only deciphers English language ciphers with uppercase alphabetical characters.

You can run this to decrypt with known key:

```
python main.py -f filename -k YOUR_KEY
```
You can run this to guess possible keys based on length:
```
python main.py -f filename -l LENGTH
```
You can run this to estimate a key length:
```
python main.py -f FILENAME -u
```
This is a script I used to help me solve some Krypton levels on Overthewire.



