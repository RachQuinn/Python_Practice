#treets = ["Lake", "Hennepin", "Lyndale"]
#streets[1] = "Portland"
#for street in streets:
 #   print(street)

# movies = ["Fargo", "Up", "Rocky", "Jaws"]
# movies.sort()
# movies.reverse()
 #     for movie in movies:
# movies.append("Nightmare Before Christmas")
# movies.pop()
# movies.remove("Rocky")
# print(movies)   

import random
movies = ["The Godfather", "Spiderman", "Star Wars", "Finding Nemo"]
random.shuffle(movies)
# for movie in movies:
for index, movie in enumerate(movies):
    print(f"{index + 1}: {movie}")
    print("Index is: " + str(index) + " and value is: ", movie)
    

