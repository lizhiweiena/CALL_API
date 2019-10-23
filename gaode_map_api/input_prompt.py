# coding: utf-8
# @Time    : 2019/9/17 9:58
# @Author  : 李志伟
# @Email   : lizhiweiena@163.com

import urllib3
import string
from urllib.parse import quote
import ast


urllib3.disable_warnings()
http = urllib3.PoolManager()

key = "e9144432d5798d13e15a9d434e9aa8df"   # 通过前面步骤创建的key，key参数为必需参数
keywords = "平安科技"
output = "json"                             # 支持XML和JSON
url = quote(f"https://restapi.amap.com/v3/assistant/inputtips?key={key}&keywords={keywords}&output={output}",
            safe=string.printable)

resp = http.request('GET', url)
result_str = resp.data.decode("utf-8")

# Python 如何将字符串转为字典
# http://funhacks.net/2016/04/24/python_%E5%B0%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E4%B8%BA%E5%AD%97%E5%85%B8/
result = ast.literal_eval(result_str)  # 将字符串转成字典
tips = result['tips']

for item in tips:
    name = item['name']
    district = item['district']
    address = item['address']
    print("name: ", name)
    print("district: ", district)
    print("address: ", address)
    print('------------------------------')
