import os
import shutil

source_dir = "/home/jawabreh/Desktop/test/self-built-masked-face-recognition-dataset/AFDB_masked_face_dataset"
dest_dir = "/home/jawabreh/Desktop/test/data"

# Iterate over subdirectories
for subdir in os.listdir(source_dir):
    subdir_path = os.path.join(source_dir, subdir)
    if os.path.isdir(subdir_path):
        # Iterate over image files in subdirectory
        for file in os.listdir(subdir_path):
            if file.endswith(".jpg") or file.endswith(".png"):
                # Construct source and destination paths
                src_path = os.path.join(subdir_path, file)
                dest_path = os.path.join(dest_dir, file)
                # Copy file to destination directory
                shutil.copy(src_path, dest_path)
