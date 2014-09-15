import Image,csv
img = Image.new( 'RGB', (503,122), "black")
pixels = img.load()
f=open('flag.txt','r')
reader = csv.reader(f, delimiter=',')
mycsv = list(reader)
k=0
for i in range(img.size[0]): # for every pixel:
 for j in range(img.size[1]):
 pixels[i,j] = (int(mycsv[k][0]), int(mycsv[k][1]), int(mycsv[k][2]))
 k=k+1
img.show()
