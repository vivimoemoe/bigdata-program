import requests
import dbm
db = dbm.open('img_type','c')

# API地址
url = "http://127.0.0.1:5000/predict"
# 图片地址
file_path = 'C:\Users\HP\Desktop\vivi-image-api\1.png'
# 图片名
file_name = file_path.split('/')[-1]
# 二进制打开图片
file = open(file_path, 'rb')
# 拼接参数
files = {'file': (file_name, file, 'image/jpg')}
# 发送post请求到服务器端
r = requests.post(url, files=files)
print(r.content)
db[file_path] = r.content
# print(db.keys())