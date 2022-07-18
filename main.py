#!/usr/bin/env python3

import pandas as pd
import pathlib
from typing import List 
from collections import OrderedDict

from links import *
from fetch import fetch


def merge(frames: List[pd.DataFrame]) -> pd.DataFrame:
  '''
  Saves merged frames to ./output/{output_file}
  '''

  return pd.concat(frames, axis=1, join='inner') 

def save_frame(file_name: str, frame: pd.DataFrame, **kwargs) -> None:
  pathlib.Path("./output/").mkdir(parents=True, exist_ok=True)
  frame.to_csv(f"./output/{file_name}", sep='\t', **kwargs)

def extract(source_frame: pd.DataFrame, column: str, col_type: str) -> pd.DataFrame:
  return source_frame[source_frame[column] == col_type]

def average_rating_type(source_frame: pd.DataFrame, column: str, sort=False) -> pd.DataFrame:
  d = {}

  filter_values = zip(source_frame[column].to_list(), source_frame['averageRating'].to_list())
  for genres, rating in filter_values:
    if pd.notnull(genres) and genres != '\\N':
      for genre in genres.split(","):
        if genre not in d:
          d[f"{genre}"] = []
        d[f"{genre}"].append(rating)
    
  ret = {}
  for genre, ratings in d.items():
    ret[genre] = round(sum(ratings)/len(ratings), 2)


  if sort:
    full_dict = OrderedDict(sorted(ret.items()))
  else:
    full_dict = {column: list(ret.keys()), 'average rating': list(ret.values())}

  print(full_dict)

  return pd.DataFrame(full_dict)


def main() -> None:
  title_basics_file_path = fetch(Links.title_basics)
  title_ratings_file_path = fetch(Links.title_ratings)

  title_basics_frame = pd.read_csv(title_basics_file_path, sep='\t', low_memory=False)
  title_ratings_frame = pd.read_csv(title_ratings_file_path, sep='\t', low_memory=False)

  all_frames = [title_basics_frame.set_index('tconst'), title_ratings_frame.set_index('tconst')]

  all_videos_frame = merge(all_frames)
  save_frame('all_videos.tsv', all_videos_frame)

  only_movies_frame = extract(all_videos_frame, 'titleType', 'movie')
  save_frame('movies.tsv', only_movies_frame)

  average_rating_genre_table = average_rating_type(all_videos_frame, 'genres')
  save_frame('movie_rating_by_genres.tsv', average_rating_genre_table, index_label=None)

  average_rating_year_table = average_rating_type(all_videos_frame, 'startYear')
  save_frame('movie_rating_by_year.tsv', average_rating_year_table, index_label=None)
  
if __name__ == "__main__":
  main()
