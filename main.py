import json

movies = []

# read movies file into variable
with open('movies.json', 'r') as openfile:
    # Reading from json file
    movies = json.load(openfile)

while True:
    print("\nMovie Tracker Menu:")
    print("1. Pievienot filmu")
    print("2. Rādīt visas pievienotas filmas sakartotas pēc reitinga")
    print("3. Rādīt vēl neskatītās filmas")
    print("4. Atzimēt filmu kā skatītu")
    print("5. Dzēst filmu no saraksta")
    print("6. Exit")
    choice = input("Enter your choice: ")
    movies_file = open('movies.json') # opening JSON file
    movies = json.load(movies_file) # returns JSON object as a dictionary
    movies_file.close()
    if choice == "1":
        # https://www.w3schools.com/python/python_dictionaries.asp
        # https://www.w3schools.com/python/python_lists_add.asp
        
        Film_title = input("Enter movie title: ")
        film_rating = int(input("Enter movie rating: "))
        watch = input("Had you watched this movie?(f = false, t = true): ")
        if watch == "f":
            watch = False
        elif watch == "t":
            watch = True



        thisdict = {
            "title": Film_title,
            "rating": film_rating,
            "watched": watch
            }
        movies.append(thisdict)
        print(movies)
        with open("movies.json", "w") as outfile:
            json.dump(movies, outfile)
        pass
    elif choice == "2":
        # https://www.w3schools.com/python/python_lists_sort.asp
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        def sort_rating(movies):
            return int(movies["rating"])
        movies.sort(key = sort_rating, reverse = False)
        print(movies[:11])
        pass
    elif choice == "3":
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        for movie in movies:
             if movie["watched"] == False:
                print(movie)
        pass
    elif choice == "4":
        # https://www.w3schools.com/python/python_lists_change.asp
        # https://www.w3schools.com/python/python_dictionaries_change.asp
        id = int(input("Enter the index of the movie to mark: "))
    elif choice == "5":
        # https://www.w3schools.com/python/python_lists_remove.asp
        id = int(input("Enter the index of the movie to remove: "))
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

# writing movies to file
with open("movies.json", "w") as movies_file:
    json.dump(movies, movies_file)