import requests
adress = 'https://discord.com/api/webhooks/1361603827085737994/-GzaWlGSZNZeGSNsIvdWpAl1WabMmIDjkHL9zdpE34T8UfMfS4RYbwfTP7AeT74oTJmT'

text = {
    "content": "Ahoj z programu python"
}

response = requests.post(adress, json=text)
