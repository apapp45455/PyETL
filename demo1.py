from urllib import request

url = 'http://httpbin.org/get'

res = request.urlopen(url=url)

html = res.read()

print(res)
print(html)
print(html.decode('utf-8'))
print(type(res.read().decode('utf-8')))