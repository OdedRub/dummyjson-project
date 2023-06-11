import requests  # imports requests library for making API requests

endpoints = {  # defines a dictionary for the different options
    "products": "https://dummyjson.com/products",
    "carts": "https://dummyjson.com/carts",
    "users": "https://dummyjson.com/users"
}
valid_options = set(endpoints.keys())  # defines a set for the available endpoints' keys

json_type = input("Enter data type (products/carts/users): ")  # asks user for input

if json_type in valid_options:  # checks if the input is one of the valid endpoints
    data_id = input("Enter an ID (1-100 for products or users, 1-20 for carts) or press 0 to get all of them: ")
    url = endpoints[json_type]  # sets 'url' to requested option

    if data_id == "0":  # checks if ID input is 0
        response = requests.get(url)  # sends GET request to requested endpoint
        data = response.json()  # parses retrieved data to json
        print(data)  # prints json
    else:
        response = requests.get(f"{url}/{data_id}")  # sends GET request to requested endpoint with id
        data = response.json()  # parses retrieved data to json
        print(data)  # prints json
else:
    print("Invalid input.")  # in case a different input was typed by user
