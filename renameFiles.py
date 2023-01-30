import os

path = "/home/jawabreh/Desktop/Temp/GunDataset/Images/"

def rename_images(path):
    i = 3001
    for filename in os.listdir(path):
        src = path + filename
        dst = path + str(i) + ".jpeg"
        os.rename(src, dst)
        i += 1

rename_images(path)
print("done")
