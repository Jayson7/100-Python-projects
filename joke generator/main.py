import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Failed to retrieve a joke."

if __name__ == "__main__":
    joke = get_joke()
    print(joke)
