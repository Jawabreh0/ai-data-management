import os

path = "/home/jawabreh/Desktop/self-built-masked-face-recognition-dataset/AFDB_masked_face_dataset/"

def rename_images(path):
    i = 1
    for root, dirs, files in os.walk(path):
        for filename in files:
            src = os.path.join(root, filename)
            dst = os.path.join(root, str(i) + ".jpg")
            os.rename(src, dst)
            i += 1

rename_images(path)
print("done")
