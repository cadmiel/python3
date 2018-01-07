import requests

file = open('resultGitHubRep.txt','a')

api = requests.get('https://api.github.com/repositories')

for item in api.json():
    file.write(item['name']+'\n')
    print(item['name'])

file.close()



