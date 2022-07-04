#!/usr/bin/env python3

import pandas as pd
import pathlib
from typing import List 

from links import *
from fetch import fetch


def merge(frames: List[pd.DataFrame]) -> pd.DataFrame:
  '''
  Saves merged frames to ./output/{output_file}
  '''

  return pd.concat(frames, axis=1, join='inner') 

def save_frame(file_name: str, frame: pd.DataFrame) -> None:
  pathlib.Path("./output/").mkdir(parents=True, exist_ok=True)
  frame.to_csv(f"./output/{file_name}", sep='\t')

def main() -> None:
  title_basics_file_path = fetch(Links.title_basics)
  title_ratings_file_path = fetch(Links.title_ratings)

  title_basics_frame = pd.read_csv(title_basics_file_path, sep='\t')
  title_ratings_frame = pd.read_csv(title_ratings_file_path, sep='\t')

  all_frames = [title_basics_frame.set_index('tconst'), title_ratings_frame.set_index('tconst')]

  all_videos_frame = merge(all_frames)
  save_frame('all_videos.tsv', all_videos_frame)

if __name__ == "__main__":
  main()
