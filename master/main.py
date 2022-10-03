import sys, requests


for host in sys.argv[1:]:
    with open('./data', 'rb') as f:
        r = requests.post(host, files={'file': f.read()})
        print("Response Headers: ", r.headers)
