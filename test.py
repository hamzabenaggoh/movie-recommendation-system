import requests


def get_recommendations(movie_title):

    # Make a request
    URL = "http://localhost:8012/recommend"
    params = {'movie_title': movie_title}
    response = requests.get(URL, params=params)

    # Get the response
    if response.status_code == 200:
        data = response.json()
        recommendations = data["recommendations"]
        
        for rec in recommendations:
            print(rec)
    else:
        print("Error: ", response.status_code)

def main():
    print("Testing Movie Recommendation Microservice")
    movie_title = input("Enter a movie title: ")
    get_recommendations(movie_title)

if __name__ == "__main__":
    main()