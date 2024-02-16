import requests

contract_name = 'dublin'  # 替换为实际的合同名称
api_key = 'c7cf23104c668a36fddf547d1448accb9f36ab94'

# 获取所有站点信息的URL（根据API的设计可能需要调整）
url = f'https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}'

response = requests.get(url)

if response.status_code == 200:
    # 请求成功，解析数据
    stations_data = response.json()
    # 打印所有站点信息或进行其他处理
    for station in stations_data:
        print(station)
else:
    # 处理错误
    print(f"Error: {response.status_code}")
