from PIL import Image
im = Image.open("stg300.png","r")
pixels = im.load()
width, height = im.size
binary_ans, binary_byte, secret = '','',''
print width,height
for y in range(height): # For every row: Visualize, height is vertical.
    for x in range(width): # For every column in height. Visualize, width is horizontal
#        print pixels[x,y] #This will print every pixel's RGB value.
        blue_pix = pixels[x,y][2] # (r is 0, 1 is g, 2 is b)
        lsb = bin(blue_pix)[-1] # Convert a pixel's blue value to binary and store the least significant bit in lsb
        binary_ans+=lsb # Store blue's every lsb in binary_ans

for i in binary_ans:
    if len(binary_byte) == 8: # Bytes are in count of 8 bits
        secret+=chr(int(binary_byte,2)) # Convert the binaries to int and then  to character and stores in secret as a string
        binary_byte = ''
    binary_byte+=i
print secret
