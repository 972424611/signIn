import urllib.request
import urllib.parse
import json
import random

username = "201650080523"
password = "074016"

loginHeader = {
    "Accept": "text/html, application/xhtml+xml,image/jxr,*/*",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.4.1",
    "Content-Length": 80,
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "Keep-Alive",
    "Host": "csust.edu.chsh8j.com:8088",
}

# 登陆
loginUrl = "https://csust.edu.chsh8j.com:8088/magus/appuserloginapi/userlogin"
loginData = bytes(urllib.parse.urlencode({'params': '{"password":"' + password + '","userName":"' + username + '"}'}), encoding='utf8')
req = urllib.request.Request(loginUrl, headers=loginHeader, data=loginData)
data = urllib.request.urlopen(req).read()
data = json.loads(data)
token = data['result']['token']
print(token)

# 获取signId
getInfoheader = {
    "Accept": "text/html, application/xhtml+xml,image/jxr,*/*",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.4.1",
    "Content-Length": 88,
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "Keep-Alive",
    "Host": "csust.edu.chsh8j.com:8088",
    "token": token
}
getInfoUrl = "https://csust.edu.chsh8j.com:8088/dorm/app/dormsign/sign/student/detail"
getInfoData = bytes(urllib.parse.urlencode({'token': token}), encoding='utf8')
req = urllib.request.Request(getInfoUrl, headers=getInfoheader, data=getInfoData)
data = urllib.request.urlopen(req).read()
data = json.loads(data)
signId = data['data']['signId']
print(signId)

# 签到
bleId = str(random.randint(0, 100000))
devUuid = str(random.randint(0, 100000))
osName = str(random.randint(0, 100000))

signInUrl = "https://csust.edu.chsh8j.com:8088/dorm/app/dormsign/sign/student/edit"
info = "signId=" + signId + "&token=" + token + "bleId=" + bleId + "&devUuid=" + devUuid + "&osName=" + osName

signInHeader = {
    "Accept": "text/html, application/xhtml+xml,image/jxr,*/*",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.4.1",
    "Content-Length": len(info),
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "Keep-Alive",
    "Host": "csust.edu.chsh8j.com:8088",
    "token": token
}
signInfo = {
    "signId": signId,
    "token": token,
    "bleId": bleId,
    "devUuid": devUuid,
    "osName": osName
}

singInData = bytes(urllib.parse.urlencode(signInfo), encoding='utf8')
req = urllib.request.Request(signInUrl, headers=signInHeader, data=singInData)
data = urllib.request.urlopen(req).read()
print(data.decode())