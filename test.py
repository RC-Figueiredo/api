import requests

headers={
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNCIsImV4cCI6MTc3ODA2OTg2Nn0.W0A_cYCuQUc0wuMDkl7ahm5kapSF-VylqO3HZU9hZw4"
}

requisicao= requests.get("http://127.0.0.1:8000/auth/refresh",headers=headers)
print(requisicao)
print(requisicao.json()).