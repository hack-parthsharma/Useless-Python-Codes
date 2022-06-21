import urllib2

url = "http://www.scanme.org"

headers = {}
headers['User-Agent'] = "GoogleBot"

request  = urllib2.Request(url,headers=headers)
response = uyrllib2.urlopen(request)

print response.read()
response.close()
