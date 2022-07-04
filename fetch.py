import numpy as np
import os
import requests
import hashlib 
import gzip

def fetch(url):
  file_path = os.path.join("/tmp", hashlib.md5(url.encode('utf-8')).hexdigest())
  if os.path.isfile(file_path):
    with open(file_path, "rb") as file:
      print(f"Reading file from temporary storage {file_path}")
      data = file.read()
  else:
    with open(file_path, "wb") as file:
      print(f"Downloading from {url}")
      data = requests.get(url).content
      file.write(gzip.decompress(data))
  return file_path


if __name__ == "__main__":
  test_file = fetch("https://datasets.imdbws.com/title.basics.tsv.gz")
  print(open(test_file).read())
 

