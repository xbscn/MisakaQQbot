import requests
s=requests.session()
s.get("https://music.163.com/api/login/cellphone?phone=xxx&password=yyy")
r=s.get("http://music.163.com/api/search/pc/?type=1&s=water&limit=3")
print(r.text)