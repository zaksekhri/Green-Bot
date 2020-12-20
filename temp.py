import requests



url = "https://api.warframestat.us/pc/invasions"
ret = requests.get(url).json()
print(ret)

