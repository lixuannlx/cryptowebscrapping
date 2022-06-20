import requests 

#r = requests.get('http://xkcd.com/353/')
#r = requests.get('https://imgs.xkcd.com/comics/python.png')

#using get request 
#payload = {'page': 2, 'count': 25}
#r = requests.get('http://httpbin.org/post', params=payload)

#using post request 
#payload = {'username': 'corey', 'password': 'testing'}
#r = requests.post('http://httpbin.org/post', data=payload)

#authentication 
r = requests.get('http://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))

print(r)
#r_dict = r.json()
#print(r_dict['headers'])  #this is quite  useful!! can access specific values 
#print(r.url)
#print(help(r))
#print(r.text)
#print(r.status_code)
#print(r.headers)
