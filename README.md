# API-PythonFlask-Sample
Creating an API using Python and Flask as a sample

## Assumptions
- The countries do not have any distance between them, so we calculate the shortest path by going through the least amount of countries. 

- You always start in the United States.

- The driver only has deliveries to the destination. There may be a situation where a driver may need to go to a nearby country before his final delivery for other deliveries. 

- The only information you need about the countries is the country code and neighboring countries (for database).


## Planning
    ### User stories:
    - User can start with a list of possible options to enter at first endpoint.
    - User inputs country code and gets a list of countries a driver must drive through.
    - User enters the USA as a destination and gets a list containing a single item country (USA).
    - User enters "BLZ" as a destination and gets a list containing ["USA","MEX", "BLZ"].

Dataset includes a list of 3-letter country codes and neighboring countries that a driver must drive through.

## Requirement Analysis
- Build a web api.
- Create an endpoint where we can send a country code and see the list of countries
- Setting up a server to host the API.
- Choose a backend framework.
- Store data in a database or file
- Create a method for calculating what countries a driver must go through to reach destination.


## Design
- Build web API using a popular framework. In this case I went with Python/Flask. This framework allows for a pleasant experience and is useful when building small projects. This combo allows for any changes and updates to development without much of a hassle. I did not use Django since the project is not very complex. 
- I considered using C# and .NET core but I felt that it would take too much time to understand the details of C# and the best coding practices. However, if the project required enterprise level support this would be the best option.
- Given that the dataset is not extensive I used a JSON file to store the country codes, and the neighbors of that country. If there was more data then there would have been a need to use a proper databse such as an SQL database.
- To ensure that the API returns the correct solution I implemented a shortest path algorithm to calculate the shortest path from the start to the destination. This allows for a more robust API that could handle more data if needed.
- The JSON file is loaded as a dictionary in python to run the shortest path algorithm.
- It is possible to test with all endpoints specified in the requirements.
-Server will be hosted on pythonanywhere.com.

## Testing
- I went through all the endpoints when testing the server locally to make sure that the desired output was returned.
- If the user enters an incorrect input then a "None" is returned.
- I tested the dataset loader to make sure that all countries and their neighbors were imported correctly.
- I tested the list of countries returned when entering a country code for all the countries.
- 

## Improvements
- If this were a more complex project there would need to be some improvements.
- With a larger dataset I would need to use a database. Flask has good options for managing a databse such as using a PostgreSQL.
- With a larger dataset there would also need to be more endpoints.
- If the data is complex enough it might be best to employ a machine learning approach instead of a traditional shortest path algorithm.
- It is important to consider the longevity of the project. If this were an API that were used at CH Robinson then it would need to be implemented in C# and .NET core to better connect with the current codebase.
- Flask is not able to handle requests associated with multiprocessing therefore it is important to either switch to a different framework or set up a Web Server Gateway Interface with the Web server. This would be important for when there are multiple calls being made to this API.
- 
 

