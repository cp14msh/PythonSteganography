from PIL import Image
im = Image.open("IMAGE ADDRESS")

def return_num():
    secret=[]
    for I in ("YOYR_SECRET_CODE"):
        secret.append(ord(I))
    
    while True:
        for _ in range(len(secret)):
            yield secret[_]

counter = return_num()

for dot_j in range(20,im.size[1],20):
    for dot_i in range(20,im.size[0],20):
        im.putpixel((dot_i,dot_j),(next(counter),next(counter),next(counter)))


im.show()
im.save("IMAGE ADDRESS YOU WANT TO SAVE")
