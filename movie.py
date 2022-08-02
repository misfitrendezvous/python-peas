current_movies = {'Movie 1':'None',
                  'Movie 2':"10:00am",
                  'Movie 3': '9:00am'}

print("We're currently showing for the following movies:")
for key in current_movies:
    print(key)

preferred_movie = input('What movie do you reuqest the showtime for?')

showtime_of_preferred_movie = current_movies.get(preferred_movie)
if showtime_of_preferred_movie == None:
    print('No')
else:
    print(preferred_movie, 'is playing at', showtime_of_preferred_movie)