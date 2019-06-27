import requests
# from PIL import Image
from io import BytesIO

# r = requests.get('https://api.github.com/events')
# r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# r = requests.put('https://httpbin.org/put', data = {'key':'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')

# r1 = requests.get('https://httpbin.org/get?key1=value1')
#
# payload = {'key1': 'value1'}
# r2 = requests.get('https://httpbin.org/get', params=payload)
#
# print(r1.text==r2.text)
#
# r = requests.get('https://api.github.com/events')
# r.text
# r.content
#
# # r.encoding='ISO-8859-1'
# i = (BytesIO(r.content))
#
# r.json()

# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
#
# r = requests.get(url, headers=headers)
#
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)
# endpoint = "https://api.staging.splunkbeta.com/testlsdcteam/identity/v1/validate"
# headers = {"Authorization": "Bearer eyJraWQiOiJuRGNXNi1WWVJUZWh0QXdZbExwRTBZWm1wTlltMWo2a3JBeXlMSVpZT0pVIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULnR1eU9xMHBzSE84OHB6TnFyZ2N2VzFxRDQ5NUdaYnVITFluV3hibXVLNmsudGFXVnoxSFIxSCtRa3pWbHRHMVQyZzZ6RkQ4RWhTbGRUQnYwQ0p0cGgvbz0iLCJpc3MiOiJodHRwczovL3NwbHVuay1jaWFtLm9rdGEuY29tL29hdXRoMi9hdXMxcmFyajZ0UVBKZkpsejJwNyIsImF1ZCI6ImFwaTovL3NjcC1kZWZhdWx0IiwiaWF0IjoxNTUxODE5MDA1LCJleHAiOjE1NTE4NjIyMDUsImNpZCI6IjBvYTIzNDhjNnVOdU1jZU94MnA3IiwidWlkIjoiMDB1MXE3OGhzbmZKRHYxMmsycDciLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiLCJwcm9maWxlIiwiZW1haWwiLCJvcGVuaWQiXSwic3ViIjoieWxpYW5nQHNwbHVuay5jb20ifQ.WlcfYa5qnVdV6oQf-K7Ff-C49XqkuZr8Osnw3uETmMYMr-sxUtTRDgxfdwaH9k7i8HuIctGE1izvMoQIbTylPktVohVxj09ZBfWGHGrK7SMMt3f0WMgOnX4-6Iu2zlYeFC8DLFPtszOV2_TZrDs_CHRwRYtXed35R98rXeCdXsLX04HCy2zpkqOagLRMIczmCFgNcjhKp9vXbDME4UEAfaTk59f8zVb4zKC3XOKyRl6rXBGTDTDjZoxUSRyZRLDdOepF8Pn4HAC3Lhvl96LF9SJO-MCXPsUc4MUP_w73L1HlaIo9UdGLhqAeQMa9lOVswTE31MuyI01aAYdGCFBm-w"}
#
# print(requests.post(endpoint, headers=headers).json())

bad_r = requests.get('https://httpbin.org/status/404')
bad_r.status_code
e=bad_r.raise_for_status()
i=2
