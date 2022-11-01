import requests
import hashlib
import sys


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching : {res.status_code}, check the api and try again .')
    return res


def get_password_leaks(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(f'Your password {h} has been leaked {count} times')
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_character, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_character)
    # print(response)
    return get_password_leaks(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'The password {password} you have entered is pawned {count} number of times')

    return "Done with the checking and you are not hacked ."


if __name__ == '__main__':
    sys.exit(print(main(sys.argv[1:])))
