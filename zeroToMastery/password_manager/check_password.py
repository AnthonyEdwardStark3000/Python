import requests
import hashlib


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching : {res.status_code}, check the api and try again .')
    return res


def get_password_leaks(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        print(f'Your password {h} has been leaked {count} times')


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_character, tail = sha1password[:5], sha1password[5:]
    # print(f'first 5 characters: {first5_character}, remaining : {tail}')
    response = request_api_data(first5_character)
    print(response)
    return get_password_leaks(response, tail)


pwned_api_check('password123')
