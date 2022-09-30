import requests

password = 'D56D985300D4B52EB6E189BE006F44F8D23C5EC9'
url = 'https://api.pwnedpasswords.com/range/'+ password
res = requests.get(url)
print(res)