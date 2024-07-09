import requests

res = requests.get('http://localhost:5000', headers={"uuid":"1c8bdbac-a252-4518-8a53-052b6ea6bc61"})
print(res.headers)

