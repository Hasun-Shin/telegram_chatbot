import tmdbsimple as tmdb
tmdb.API_KEY = 'b25f90dff294de0f547a2e5dda41f3e4'

movie = tmdb.Movies(603)
response = movie.info()
# movie.title
# 'The Matrix'
# movie.budget
# 63000000
# response = movie.releases()
# for c in movie.countries:
#     if c['iso_3166_1'] == 'US':
#          print(c['certification'])

# #'R'