#url별 비밀번호 생성

url = 'http://naver.com'
url_str = url.replace('http://','')
print(url_str)
my_str = url_str[:url_str.index('.')]
print(my_str)
my_str[:3]
print(my_str[:3])
passwd = (my_str[:3] + str(len(my_str)) + str(my_str.count('e'))+'!')
print(passwd)
print('{}의 비밀번호는 {}입니다.'.format(url, passwd))
