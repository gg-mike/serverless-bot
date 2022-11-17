from glob import glob
from shutil import move

directories = glob("../.aws-sam/build/*/", recursive = True)
length = len(directories)
length_str_size = len(str(length))

print("Cleaning build folder")
for i, directory in enumerate(directories):
    print(f"[{i+1: <{length_str_size}}/{length}]: {directory[:-1].split('/')[-1]}")
    for package in glob(directory + "*/", recursive=True):
        move(package, directory + "packages/" + package[:-1].split("/")[-1])



