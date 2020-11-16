# Python Developer / Data Engineer Intern recruitment test
This is test recruitment task for intern candidate for Python Developer or Data Engineer position.

0. Fork this repository.

1. Download from https://www.imdb.com/interfaces/ files:
- `title.basics.tsv.gz`
- `title.ratings.tsv.gz`

2. Implement Python script which merges data about videos from those files using *tconst* column and save it into `all_videos.tsv` file. New file should contain columns from `title.basics.tsv.gz` and `title.ratings.tsv.gz`

3. Implement Python script which extracts from `all_videos.tsv` only these videos with *titleType* "movie" and save them into `movies.tsv` file

4. Implement Python script which calculates average rating for each *genre* save them into `movie_rating_by_genres.tsv` file

5. Repeat point 4. for average rating per *startYear* column and save them into `movie_rating_by_year.tsv` file

6. All scripts and `movie_rating_by_genres.tsv`, `movie_rating_by_year.tsv` files upload to your repository. Separate commits for points 2-5.

7. Optional - visualize on chart `movie_rating_by_genres.tsv` and `movie_rating_by_year.tsv` files using any Python library and upload script and png files to your repository.
