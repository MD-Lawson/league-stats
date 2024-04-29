import requests

def get_data_from_api(api_url, api_key):
    headers = {
        'Content-Type': 'application/json',
        'X-Riot-Token': api_key
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse JSON response
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error accessing API: {e}")
        return None

# Example usage
api_url = 'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/vsovari/noob'
api_key = 'RGAPI-9a2816dc-ddd3-4982-b2ab-eee80e4e601d'

data = get_data_from_api(api_url, api_key)
if data:
    print("Received data from API:")
    print(data)
else:
    print("Failed to fetch data from API.")