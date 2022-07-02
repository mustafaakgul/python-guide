from requests import Request,Session

s=Session()
req=Request('GET','https://python.org')
headers={'Connection' : 'Not-Alive'}
req=Request('GET','https://python.org', headers=headers)