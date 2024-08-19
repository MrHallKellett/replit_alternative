with open("tests.py", encoding="utf-8") as f:
    code = f.read()
    
NULL_BYTE_BUFFER=99

#convert each char in code to 2 hex digits
code_hex=[hex(ord(i))[2:].zfill(2) for i in code]

# concat hex string 
hex_2_string = "".join(code_hex)

# convert each 5 hex chars into unicode
unicode = [chr(int(hex_2_string[j:j+5],16)+NULL_BYTE_BUFFER) for j in range(0,len(hex_2_string),5)]


# unicode back into hex
unicode_2_hex = "".join([hex(ord(i))[2:].zfill(5) for i in unicode])

# unicode hex back to 2-digit hex codes
s=[unicode_2_hex[i:i+2].zfill(2) for i in range(0, len(unicode_2_hex), 2)]

with open("deobfuscator.py") as f:
    template = f.read()
    
with open("tests_obfuscated.py", "w", encoding="utf-8") as f:
    f.write(template.replace("UNICODE_STR_HERE", "".join(unicode)))

