# movie-recommendation-system
 
# How to Request movie recommendations from the service

To request data make an HTTP GET request to the endpoint that the microservice is listening on.
Specifically you want to include a query parameter in the GET request that corresponds to a movie title.
In the example below the microservice is listening on port 8012:


URL = "http://localhost:8012/recommend"
params = {'movie_title': movie_title}
response = requests.get(URL, params=params)


The url this corresponds to assuming Batman is the movie_title: http://localhost:8012/recommend?movie_title=Batman

# How to receive movie recommendations from the service

When you send a request the microservice processes the request and calculates three recommended movies based on the movie
you passed in the get request. Since the microservice is listening to your request on the /recommend endpoint,
as soon as it receives a request it sends a json response back containing the 3 movie recommendations. In order to receive the 
data you must parse the JSON response like so:

if response.status_code == 200:
        data = response.json()
        recommendations = data["recommendations"]
    else:
        print("Error: ", response.status_code)


UML Sequence Diagram<br>


<img width="331" alt="Screenshot 2024-02-26 at 7 08 11 PM" src="https://github.com/hamzabenaggoh/movie-recommendation-system/assets/54951481/ad0a721f-04a0-4ec3-864a-3a89fd5d24d2">

