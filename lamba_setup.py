from glob import glob
from os import makedirs, path
from shutil import copy, rmtree


def clean():
  rmtree('gen', ignore_errors=True)


def generate_lambda_src():
  for filepath in glob(f"src/lambda/*.py"):
    print(filepath)
    file = filepath.split("\\")[1]
    new_dir = path.join("gen", *file.split(".")[:-1])
    makedirs(new_dir)
    copy(filepath, f"{new_dir}/index.py")
    copy("requirements.txt", f"{new_dir}/requirements.txt")
    for common_filepath in glob("src/common/*.py"):
      common_file = common_filepath.split("\\")[1]
      copy(common_filepath, f"{new_dir}/{common_file}")


def main():
  clean()
  generate_lambda_src()


if __name__ == "__main__":
  main()