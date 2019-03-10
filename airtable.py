import requests
from secret import AIRTABLE_TOKEN

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + AIRTABLE_TOKEN
}

url = "https://api.airtable.com/v0/appG4BDgaJRGJLvOF/Parsed"

def fetch_from_airtable():
    # Will get the words already ankid, backlogged and blacklisted
    # Should expand words and get rid of pronouns (l'air -> l'/ air and l',le,la,les,un,une,des)
    # Add words to already seen words!
    continue

def send_to_airtable(data):
    response = requests.request(
        method="POST",
        url=url,
        json=data,
        headers=headers
    )

    if response.ok:
        print("OK")
    else:
        print("ERROR")
