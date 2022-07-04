#!/usr/bin/env python3

import pandas as pd

from links import *
from fetch import fetch

title_basics_file_path = fetch(Links.title_basics)
title_ratings_file_path = fetch(Links.title_ratings)

title_basics_frame = pd.read_csv(title_basics_file_path, sep='\t')
title_ratings_frame = pd.read_csv(title_ratings_file_path, sep='\t')
print(title_basics_frame)
print(title_ratings_frame)
