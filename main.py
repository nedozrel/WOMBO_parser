import requests
import json
import time


def get_result_url(id, headers):
    res = ''
    while not res:
        r = requests.get(f'https://paint.api.wombo.ai/api/tasks/{id}', headers=headers)
        data = r.json()
        time.sleep(1)
        if data['result'] is not None:
            res = r.json()['result']['final']
    return res


r = requests.get(
    'https://firebase.googleapis.com/v1alpha/projects/-/apps/1:181681569359:web:277133b57fecf57af0f43a/webConfig',
    headers={'x-goog-api-key': 'AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw'})
print(r.headers)
print(r.json())
r = requests.post(
    'https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw')
print(r.headers)
print(r.json())

data = {
    'premium': 'false'
}

headers = {'authorization': 'bearer DE5NDQ4NiwidXNlcl9peyJhbGciOiJSUzI1NiIsImtpZCI6IjcxMTQzNzFiMmU4NmY4MGM1YzYxNThmNDUzYzk0NTEyNmZlNzM5Y2MiLCJ0eXAiOiJKV1QifQ.eyJwcm92aWRlcl9pZCI6ImFub255bW91cyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9wYWludC1wcm9kIiwiYXVkIjoicGFpbnQtcHJvZCIsImF1dGhfdGltZSI6MTY0MZCI6ImVYMTNTdnlLZ0JVZlBISklaOXh4ZGJ5bXRxcTIiLCJzdWIiOiJlWDEzU3Z5S2dCVWZQSEpJWjl4eGRieW10cXEyIiwiaWF0IjoxNjQwMTk0NDg2LCJleHAiOjE2NDAxOTgwODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiYW5vbnltb3VzIn19.kEa1GSfYpFWr6qa9F4yW_sKkY8gSgAewjDfxWRRHRulSfjZ96kBpvvd_y-kblSlFG9lni-JHNZHNjjv_Qayu2FpGsy4pHtb3nQQmPsYzT3WyN9myaNmSeRxgmSHRHf-6RDsVwO8wSvYzhkl7UXeKzibTiaDuYpHYZ7OlTnXjwkzjxhaWkVVvDf_9Cb4CMKOibD-8WP9Ii1mA0ejymJ9ayrrsHts0VJBLzjSk-SCAc3pj0oufK-a9SlmiB_MFDZCU0RsvhN9zwG5chTq8MHHiWP5SRq0OeZnxTE-0ItkakVM6gNJ1h6QFUWu-Wgt7ojYrA-oOSft2LvcJU9dKRpEfiw',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/94.0.4606.85 YaBrowser/21.11.3.927 Yowser/2.5 Safari/537.36'
}

input_spec = {
    'input_spec': {
        'display_freq': 10,
        'prompt': "a cat ate a dog",
        'style': 1
    }
}

r = requests.post('https://paint.api.wombo.ai/api/tasks/', headers=headers, json=data)
data = r.json()
print(data)
r = requests.put(f'https://paint.api.wombo.ai/api/tasks/{data["id"]}', headers=headers, json=input_spec)

print(get_result_url(data['id'], headers))
