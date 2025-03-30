import requests

def convert_currency(amount, from_currency, to_currency):
    api_key = "YOUR_API_KEY"  # Get your free API key from exchangerate-api.com
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    
    response = requests.get(url).json()
    
    if response["result"] == "success":
        exchange_rate = response["conversion_rates"][to_currency]
        converted_amount = amount * exchange_rate
        return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    else:
        return "Invalid Currency Code or API Key!"

# Example Usage
print(convert_currency(100, "USD", "INR"))  # Convert 100 USD to INR
