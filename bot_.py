import requests

request_data = {
    'method': 'POST',
    'url': 'https://tres-bien.com/checkout/cart/add/uenc/aHR0cHM6Ly90cmVzLWJpZW4uY29tL25pa2Utbm9jdGEtYWlyLXpvb20tZHJpdmUtc3Atd2hpdGU%2C/product/123554/',
    'headers': {
        'Host': 'tres-bien.com',
        'Cookie': 'PHPSESSID=5381f088e986c594d89463e91f8d39bf; ...',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Origin': 'https://tres-bien.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://tres-bien.com/nike-dunk-low-qs-varsity-red-silver-fq6965-600',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Priority': 'u=1, i'
    },
    'data': {
        'product': '123554',
        'related_product': '',
        'form_key': 'anr9aUHsGcK7XSV5',
        'super_attribute[135]': '16'
    }
}

try:
    response = requests.post(request_data['url'], headers=request_data['headers'], data=request_data['data'])

    if response.status_code == 200:
        cart_response = requests.get('https://tres-bien.com/customer/section/load', headers=request_data['headers'])
        if cart_response.status_code == 200:
            print('ok')
            with open('requests.txt', 'w') as file:
                file.write('')
            with open('requests.txt', 'a') as file:
                file.write(str(cart_response.json()) + '\n')  
        else:
            print('Erreur', cart_response.status_code)
    else:
        print('Error', response.text)
except requests.exceptions.RequestException as e:
    print('Error', e)

