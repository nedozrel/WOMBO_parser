import time
import requests
from fake_useragent import UserAgent


def get_request_headers() -> dict:
    """Creates and returns a dictionary of request headers"""

    url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw'
    user_agent_fallback = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                          '(KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36'
    user_agent = UserAgent(fallback=user_agent_fallback).random

    headers = {
        'user-agent': user_agent,
    }

    r = requests.post(url, headers=headers, json={'returnSecureToken': True})
    authorization_key = r.json()['idToken']
    headers['authorization'] = f'bearer {authorization_key}'

    return headers


def get_result_url(user_id: str, headers: dict) -> str:
    """Waits until API returns final result and returns URL.

    :param user_id: ID that API gives.
    :param headers: Headers to send in a request.
    :return: A URL to a picture
    """

    result = ''

    while not result:
        req_data = requests.get(f'https://paint.api.wombo.ai/api/tasks/{user_id}', headers=headers).json()

        if req_data['result'] is not None:
            result = req_data['result']['final']

        time.sleep(1)

    return result


def main():
    headers = get_request_headers()

    req_params = {
        'input_spec': {
            'display_freq': 10,
            'prompt': "skull",
            'style': 1
        }}

    for i in range(1, 15):
        req_params['input_spec']['style'] = i
        r = requests.post('https://paint.api.wombo.ai/api/tasks/', headers=headers, json={'premium': 'false'})
        req_data = r.json()
        requests.put(f'https://paint.api.wombo.ai/api/tasks/{req_data["id"]}', headers=headers, json=req_params)
        print(get_result_url(req_data['id'], headers))


if __name__ == '__main__':
    main()
