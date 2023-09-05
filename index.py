from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "http://10.54.130.221/locker/test.json"
  
# store the response of URL
data = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(data.read())

# print json response id 1
for i in data_json:
    if (i['id'] == 1):
      print(i)