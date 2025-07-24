from database import SessionLocal
from query_helpers import *


db=SessionLocal()

# movie=get_movie(db,movie_id=1)
# print(movie.title,movie.genres)

# movies=get_movies(db,limit=5,title="Inception",genre="Sci-Fi")
# for film in movies:
#     print(f"id:{film.movieId},titre:{film.title},genres:{film.genres}")

# rating=get_rating(db,user_id=1,movie_id=1)
# print(f"Rating for user {rating.userId} on movie {rating.movieId}: {rating.rating}")

# ratings=get_ratings(db,limit=5,min_rating=4.0,user_id=1)
# for rating in ratings:
#     print(f"User id: {rating.userId} ,Note: {rating.rating}")

# tag=get_tag(db,user_id=2,movie_id=60756,tag_text="funny")
# print(f"Tag found: {tag.userId} ,movie id: {tag.movieId}, user id: {tag.userId}")

n_movies=get_tag_count(db)
print(f"Total number of movies: {n_movies}")

db.close()