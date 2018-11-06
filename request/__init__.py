import requests

# r = requests.get("https://www.douban.com/")
# print(r.status_code)
# print(r.text)

# r = requests.get("https://www.douban.com/search",params={'q': 'python', 'cat': '1001'})
# print(r.url)
# print(r.encoding)
#
# r=requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())
#
r=requests.get('http://www.douban.com',headers ={'key':'value'} )
print(r.headers)
# print(r.text)


#requests默认使用application/x-www-form-urlencoded对POST数据编码。
# r = requests.post('https://accounts.douban.com/login',
#                   data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r.text)

#在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
upload_files= {'file':open('report.xls', 'rb')}
r = requests.post('http://www.baidu.com',files=upload_files)

#超时
r = requests.get('http://www.baidu.com', timeout=2.5) # 2.5秒后超时