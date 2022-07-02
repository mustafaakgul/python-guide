
import requests
proxies={'https':'https://192.168.1.1:80', 'https':'https://192.168.1.1:80'}
requests.get('http://arh.bg.ac.rs', proxies=proxies)