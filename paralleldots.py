import requests

BASE_URL ='https://apis.paralleldots.com/'
API_KEY='5d1i6JwqibzZaZJrgAW84Fb6VdSpwmVxRD5xvcAA6VE'

input= raw_input("enter text")
request_url=BASE_URL + 'sentiment?sentence1=%s&apikey=%s' %(input,API_KEY)
response=requests.get(request_url, verify=False).json()
print response
#apis.paralleldots.com/sentiment?sentence1=i%20am%20the%20best&apikey=5d1i6JwqibzZaZJrgAW84Fb6VdSpwmVxRD5xvcAA6VE