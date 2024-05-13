import requests
import os
import tempfile

# Define the base URL and headers
base_url = 'https://tres-bien.com'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Origin': base_url,
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Priority': 'u=1, i'
}

# Define the product data
product_data = {
    'product': '123554',
    'related_product': '',
    'form_key': 'anr9aUHsGcK7XSV5',
    'super_attribute[135]': '16'
}

# Create a requests Session object
session = requests.Session()

# Create a new cookie jar file on each script launch
with tempfile.NamedTemporaryFile(delete=False) as tmp:
    jar = requests.cookies.RequestsCookieJar()
    session.cookies = jar

    # Add a new cookie to the jar
    jar.set_cookie(requests.cookies.create_cookie('PHPSESSID', value=os.urandom(24).hex()))

try:
    # Make the POST request to add the product to the cart
    response = session.post(f'{base_url}/checkout/cart/add/uenc/aHR0cHM6Ly90cmVzLWJpZW4uY29tL25pa2Utbm9jdGEtYWlyLXpvb20tZHJpdmUtc3Atd2hpdGU%2C/product/123554/', headers=headers, data=product_data)

    if response.status_code == 200:
        # Make the GET request to load the cart section
        cart_response = session.get(f'{base_url}/customer/section/load', headers=headers)
        if cart_response.status_code == 200:
            print('ok')
            # Make the GET request to load the checkout page
            checkout_response = session.get(f'{base_url}/checkout/', headers=headers)
            if checkout_response.status_code == 200:
                print('Contenu de la page Checkout:', checkout_response.text)
            else:
                print('Erreur lors de l\'accès à la page Checkout:', checkout_response.status_code)
        else:
            print('Erreur', cart_response.status_code)
    else:
        print('Error', response.text)
except requests.exceptions.RequestException as e:
    print('Error', e)