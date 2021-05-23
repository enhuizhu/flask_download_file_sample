from os import listdir
from os.path import isfile, join

def get_files_from_dir(path):
  files = [f for f in listdir(path) if isfile(join(path, f))]
  return files

