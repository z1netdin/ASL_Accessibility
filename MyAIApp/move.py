import os
import shutil

base = "datasets/asl_alphabet"

# Move train
shutil.move(os.path.join(base, "images", "train"), os.path.join(base, "train"))

# Move val
shutil.move(os.path.join(base, "images", "val"), os.path.join(base, "val"))

# Remove the empty 'images' directory
os.rmdir(os.path.join(base, "images"))

print(" Moved train/ and val/ up one level.")
