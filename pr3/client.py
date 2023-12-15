import requests

url = 'http://localhost:5000/'
s = requests.Session()


def test_authentication(username, password):
    url = 'http://127.0.0.1:5000/'
    params = {
        'username': username,
        'password': password
    }
    response = requests.get(url, params=params)

    if response.status_code == 1000:
        return "1"
    else:
        return response.json()['message']


def test(log, password):
    result = test_authentication(log, password)
    if result == "1":
        print('Password: ' + password)
    else:
        print(result)


test('admin', 'asdasdas')
test('admin', 'dfgdfgdf')
test('admin', 'cvbcvbcv')
test('admin', 'password')