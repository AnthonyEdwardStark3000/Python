import requests
import hashlib


# password = 'D56D985300D4B52EB6E189BE006F44F8D23C5EC9'
# password = 'D56D9'
# url = 'https://api.pwnedpasswords.com/range/'+ password
# res = requests.get(url)
# print(res)

def request_api(query_character):
    url = 'https://api.pwnedpasswords.com/range/' + query_character
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error occured {res.status_code}, check the API and try again .')
    return res.status_code


def pawned_api(password):
    sha_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # print(f'The encrypted password is {sha_password}')
    return sha_password

password_global = 'D56D9'
pawned_api(password_global)
request_api(password_global)
