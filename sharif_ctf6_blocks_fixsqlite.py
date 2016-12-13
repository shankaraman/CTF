missing_bytes = "53 51 4C 69  74 65 20 66  6F 72 6D 61  74"
clean_hex = (missing_bytes.replace("  "," ")).replace(" ","")

#sqlite_header = [0x53,0x51,0x4C,0x69,0x74,0x65,0x20,0x66,0x6F,0x72,0x6D,0x61,0x74]

sqlite_header = clean_hex.decode("hex")
reconstruct = sqlite_header
fd1 = open('./blocks-data.sqlite','rb')
data = fd1.read()
for i in data:
    reconstruct += i
with open('reconstructed.sqlite','wb') as fd2:
    fd2.write(reconstruct)
fd1.close()
fd2.close()
