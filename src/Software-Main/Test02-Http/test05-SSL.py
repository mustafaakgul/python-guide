
import requests
requests.get('https://github.com', verify='/path')

s=requests.Session()
s.verify='/path'
requests.get('http://arh.bg.ac.rs', verify=False)

requests.get(url='', cert={'/pathClient.cert', '/path/client.key'})