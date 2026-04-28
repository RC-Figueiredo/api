import requests

headers={
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNCIsImV4cCI6MTc3NzM4NTcxNn0.l3xJKh4vzf2jBA_i98oaJJaiw5RHg-tFvziXbxVk7ao"
}

requisicao= requests.get("http://127.0.0.1:8000/auth/refresh",headers=headers)
print(requisicao)
print(requisicao.json())