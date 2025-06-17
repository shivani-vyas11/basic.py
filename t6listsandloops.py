# list of 5 favourite movies
favourite_movies = ["Inception", "The Matrix", "Interstellar", "The Shawshank Redemption", "Pulp Fiction"]
# print the list of favourite movies with numbering
print("My 5 favourite movies are:")
for i in range(len(favourite_movies)):
    print(f"{i + 1}. {favourite_movies[i]}")
    