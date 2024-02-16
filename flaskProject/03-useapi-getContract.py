import requests

api_key = 'c7cf23104c668a36fddf547d1448accb9f36ab94'  # 替换成您的实际API密钥

# 请求所有合同的URL
url = 'https://api.jcdecaux.com/vls/v1/contracts?apiKey=' + api_key

response = requests.get(url)

if response.status_code == 200:
    contracts = response.json()
    for contract in contracts:
        print(f"Name: {contract['name']}, City: {contract['commercial_name']}")
else:
    print(f"Error: {response.status_code}")
'''
Name: rouen, City: cy'clic
Name: jcdecauxbike, City: None
Name: toulouse, City: Vélô
Name: luxembourg, City: Veloh
Name: dublin, City: dublinbikes
Name: valence, City: None
Name: stockholm, City: Cyclocity
Name: santander, City: Tusbic
Name: lund, City: Lundahoj
Name: maribor, City: None
Name: bruxelles, City: villo
Name: lyon, City: Vélo'V
Name: amiens, City: Velam
Name: mulhouse, City: VéloCité
Name: lillestrom, City: Bysykkel
Name: ljubljana, City: Bicikelj 
Name: seville, City: None
Name: nancy, City: vélOstan'lib
Name: namur, City: Li bia velo
Name: creteil, City: Cristolib
Name: cergy-pontoise, City: Velo2
Name: vilnius, City: Cyclocity
Name: toyama, City: cyclocity
Name: marseille, City: Le vélo
Name: nantes, City: Bicloo
Name: brisbane, City: CityCycle
Name: besancon, City: None
'''