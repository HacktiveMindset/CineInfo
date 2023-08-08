import requests

def get_movie_info(movie_name, api_key):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        title = data["Title"]
        year = data["Year"]
        plot = data["Plot"]
        rating = data["imdbRating"]
        genre = data["Genre"]
        runtime = data["Runtime"]
        director = data["Director"]
        cast = data["Actors"]
        awards = data["Awards"]
        production = data["Production"]

        print(f"Title: {title}")
        print(f"Year: {year}")
        print(f"Genre: {genre}")
        print(f"IMDb Rating: {rating}")
        print(f"Runtime: {runtime}")
        print(f"Director: {director}")
        print(f"Cast: {cast}")
        print(f"Awards: {awards}")
        print(f"Production: {production}")
        print(f"Plot: {plot}")
    else:
        print(f"Movie '{movie_name}' not found!")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OMDB API key
    api_key = "YOUR_API_KEY"

    movie_name = input("Enter the movie name: ")
    get_movie_info(movie_name, api_key)
