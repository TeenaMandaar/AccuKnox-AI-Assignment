import requests 
response = requests.get("https://openlibrary.org/subjects/science_fiction.json?limit=5")
if response.status_code == 200:
    data = response.json()
    print("Success! I got the data.")
    print(data.keys()) 
else:
    print("Something went wrong.")