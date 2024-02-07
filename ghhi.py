import requests

# url = "https://api.themoviedb.org/3/movie/550?language=en-US"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
MOVIE_DB_API_KEY = "54d500dd4de124397b444be95dd81500"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
movie_api_id = 550
movie_title = "fight club"
# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGQ1MDBkZDRkZTEyNDM5N2I0NDRiZTk1ZGQ4MTUwMCIsInN1YiI6IjY1YzM2MzRlOGUyZTAwMDE2MmE1OGNkZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wov2CbgdToGiL-PqrcgpPRFSjn6o-e0sMgfke91_Qlw"
# }
#
# response = requests.get(url, headers=headers)

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGQ1MDBkZDRkZTEyNDM5N2I0NDRiZTk1ZGQ4MTUwMCIsInN1YiI6IjY1YzM2MzRlOGUyZTAwMDE2MmE1OGNkZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wov2CbgdToGiL-PqrcgpPRFSjn6o-e0sMgfke91_Qlw"
# }
#
# response = requests.get(MOVIE_DB_SEARCH_URL, headers=headers)
#
# print(response.text)

movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience
        #e.g. Hindi speakers then you might choose "hi-IN"
# response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
# data = response.json()

# response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
# data = response.json()["results"]
# # print(response.text)
# print(data)

response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
data = response.json()["results"]
# print(data)
print(response.text)
