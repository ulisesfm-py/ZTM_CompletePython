import requests
import hashlib
import sys

#SHA1(password123) is cbfdac6008f9cab4083784cbd1874f76618d2a97
# we only pass the first 5 characters, this is called 'key anonymity'

# to avoid sending our complete sha1 password, just to make sure nobody can go looking for sha1s and find our password
# we send query_char, which are the first 5 characters of our requested password hashed into sha1


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    # if the response is 200 it means it went well
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again.')
    return res


def count_password_leaks(hashes, hash_to_check):
    # let's split the hashes by the ':' to get the tail of the hash and the number of times it has been hacked
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # convert password into sha1
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # we split the first 5 characters and the tail
    first5_char, tail = sha1password[:5], sha1password[5:]
    # request api data providing the first 5 char of sha1 password
    response = request_api_data(first5_char)
    print(response)  # if everything is fine it prints Response [200]
    # request_api_data also returns all the sha1 password that start with those 5 char and the times they have been leaked
    # knowing the rest of the sha1 (tail), we can check how many times it has been leaked
    return count_password_leaks(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times. It would be wise to change it.')
        else:
            print('That\'s such a safe password, keep it up man')
    return 'check done!'


if __name__ == '__main__':
    main(sys.argv[1:])
