from database import SessionLocal
from models import Movie,Rating,Tag,Link

db=SessionLocal()
#tester la recuperation de quelques films

movies=db.query(Movie).limit(10).all()
movies
for movie in movies:
    print(f"id:{movie.movieId},titre:{movie.title},genres:{movie.genres}")
else:
    print("no module found")
# recupere les films du genre Action
actions_movies=db.query(Movie).filter(Movie.genres.like("%Action%")).limit(5).all()
for movie in actions_movies:
    print(f"id:{movie.movieId},titre:{movie.title},genres:{movie.genres}")
else:
    print("no action movie found")


ratings=db.query(Rating).limit(10).all()
for rating in ratings:
    print(f"user id:{rating.userId},movie id:{rating.movieId},rating:{rating.rating},timestamp:{rating.timestamp}")

hight_rated_movies=(
    db.query(Movie.title,Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4, Movie.movieId == Rating.movieId)
    .limit(5)
    .all()
)
print(hight_rated_movies)

for title, rating in hight_rated_movies:
    print(f"Movie:{title},rating:{rating}")

# Recuperation des tags associes aux films
tags=db.query(Tag).limit(10).all()
for tag in tags:
    print(f"user id:{tag.userId},movie id:{tag.movieId},tag:{tag.tag},timestamp:{tag.timestamp}")

links=db.query(Link).limit(10).all()

for link in links:
    print(f"movie id:{link.movieId},imdb id:{link.imdbId},tmdb id:{link.tmdbId}")

#fermer la session
db.close()