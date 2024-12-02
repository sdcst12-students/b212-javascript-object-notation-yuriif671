#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

#print(data)
# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains
response = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
data = response.json()
#print(data)

print("\n\n             SDSS MENU")
for item in data['menu']:
    print("=" * 40)
    print(f"{item['dayname']} ({item['date']})")
    print(f"Soup: {item['soup']}")
    print(f"Short Order: {item['shortorder']}")
    print(f"Entree: {item['entree']}")
    print(f"Notes: {item['notes']}")

print("=" * 40)
print('\n\n')