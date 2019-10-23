# coding: utf-8
# @Time    : 2019/10/15 14:46
# @Author  : 李志伟
# @Email   : lizhiweiena@163.com


import uuid
from urllib.parse import urlencode

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

client = AcsClient('LTAI4FcqpUcSu5Ytbt9FTvPg', 'AX38rHYJgtWVwjAxyZjx0oIGXm11nW', 'cn-hangzhou')
request = CommonRequest()
request.set_domain("automl.cn-hangzhou.aliyuncs.com")
request.set_uri_pattern("/api/automl/predict")
request.set_version('2019-05-29')
request.set_method('POST')
request.add_header("x-acs-signature-method", "HMAC-SHA1")
request.add_header("x-acs-signature-nonce", uuid.uuid4().hex)
request.add_header("x-acs-signature-version", "1.0")
request.set_content_type("application/x-www-form-urlencoded")
request.set_accept_format("application/json;chrset=utf-8")
new_content = {
    'ModelId': 1408,
    'Content': 'Delegates Urge Cleric to Pull Out of Najaf',
    'Version': 'V1'
}
request.set_content(urlencode(new_content))
response = client.do_action_with_exception(request)
print(str(response, encoding='utf-8'))

