import requests

# create your own api key https://v6.exchangerate-api.com

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200 or data['result'] != 'success':
        print("Error fetching exchange rate data")
        return None
    
    rates = data['conversion_rates']
    return rates.get(target_currency, None)

def currency_converter(api_key):
    print("Welcome to the Currency Converter!")
    
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
    
    if exchange_rate is None:
        print(f"Error: Could not find exchange rate for {base_currency} to {target_currency}")
    else:
        converted_amount = amount * exchange_rate
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

def main():
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    currency_converter(api_key)

if __name__ == "__main__":
    main()
