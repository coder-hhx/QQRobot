import base64
import json
import re

import requests
from requests.models import Response

# network find this
from PIL import Image

"https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?&g_tk=990452987"

shuoshuo_url = "https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?&g_tk=990452987"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    "cookie": "pgv_pvi=9817097216; RK=RD7xq0tZPk; ptcz=672b14695d9766a17c3f1432a205bfd8cd485b631a687cf8b23787de8a6e9537; tvfe_boss_uuid=349f9ce14790623d; pgv_pvid=220366552; pac_uid=0_5e8c3612e6829; eas_sid=M1Y6K1b4K3G9p079x3s4D5C3D8; uin_cookie=o1021969591; ied_qq=o1021969591; LOLWebSet_AreaBindInfo_1021969591=%257B%2522areaid%2522%253A%25222%2522%252C%2522areaname%2522%253A%2522%25E6%25AF%2594%25E5%25B0%2594%25E5%2590%2589%25E6%25B2%2583%25E7%2589%25B9%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221021969591%2522%252C%2522rolename%2522%253A%2522%25E5%2593%258E%25E5%2591%2580%25E8%25B5%25B7%25E4%25BB%2580%25E4%25B9%2588%25E5%2590%258D%25E5%2591%25A2%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1021969591%257C2%257C1021969591*%257C%257C%257C%257C%2525E5%252593%25258E%2525E5%252591%252580%2525E8%2525B5%2525B7%2525E4%2525BB%252580%2525E4%2525B9%252588%2525E5%252590%25258D%2525E5%252591%2525A2*%257C%257C%257C1614390966%257C%2522%252C%2522md5str%2522%253A%25226CE6EBD36ABC28CF840E3AC9BAC8FE90%2522%252C%2522roleareaid%2522%253A%25222%2522%252C%2522sPartition%2522%253A%25222%2522%257D; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; _qpsvr_localtk=0.8221886239765381; pgv_info=ssid=s1497155190; __Q_w_s_hat_seed=1; ptui_loginuin=%202944208466; pt_sms_phone=176******67; uin=o1021969591; skey=@SgFXtp9nQ; p_uin=o1021969591; pt4_token=--ZvL0D*U-gOW*ZTSK0FozZK4Vnbi3UzHundeai3mA0_; p_skey=W7Vs3kLp1r1diC8CG5UPM3SFO848q0RAeOe*Fyw2WL8_; cpu_performance_v8=10"
}

upload_image_url = "https://up.qzone.qq.com/cgi-bin/upload/cgi_upload_image?g_tk=990452987&&g_tk=990452987"

s = requests.Session()

f = open('img.jpg', 'rb')  # 二进制方式打开图文件
ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
f.close()
# print ls_f
img = Image.open('img.jpg')

hd_width = img.size[0]
hd_height = img.size[1]

img = {
    "filename": "filename",
    "uin": "1021969591",
    "skey": "%40sOs1yRjbY",
    "zzpaneluin": "1021969591",
    "zzpanelkey": "",
    "p_uin": "1021969591",
    "p_skey": "dOrpof51C4Av7JwDnw6piwxJnrkpIiBV5ZQD0U4lqA0_",
    "qzonetoken": "",
    "uploadtype": "1",
    "albumtype": "7",
    "exttype": "0",
    "refer": "shuoshuo",
    "output_type": "jsonhtml",
    "charset": "utf-8",
    "output_charset": "utf-8",
    "upload_hd": "1",
    "hd_width": hd_width,
    "hd_height": hd_height,
    "hd_quality": "96",
    "backUrls": "http%3A%2F%2Fupbak.photo.qzone.qq.com%2Fcgi-bin%2Fupload%2Fcgi_upload_image%2Chttp%3A%2F%2F119.147.64.75%2Fcgi-bin%2Fupload%2Fcgi_upload_image",
    "url": "https%3A%2F%2Fup.qzone.qq.com%2Fcgi-bin%2Fupload%2Fcgi_upload_image%3Fg_tk%3D100187323",
    "base64": "1",
    "jsonhtml_callback": "callback",
    "picfile": ls_f
}

response = s.post(upload_image_url, headers=headers, data=img)

print(response.text)

# resp = json.loads(re.findall(r'({.*})', response.text)[0])

data_open2all = {
    "syn_tweet_verson": "1",
    "paramstr": "1",
    "pic_template": "",
    "richtype": "1",
    "richval": "%2CV1036ZA50qnQ6X%2CNR8AVjZiQ2dBeE1ESXhPVFk1TlRreDkqNDhZTzBvKndrIQcAcGhvdG9neg!!%2CNR8AVjZiQ2dBeE1ESXhPVFk1TlRreDkqNDhZTzBvKndrIQcAcGhvdG9neg!!%2C17%2C680%2C1200%2C%2C680%2C1200",
    "special_url": "",
    "subrichtype": "1",
    "pic_bo": "sASoAgAAAAAREDk!%09sASoAgAAAAAREDk!",
    "who": "1",
    "con": "testtest",  # 文字内容
    "feedversion": "1",
    "ver": "1",
    "ugc_right": "1",
    "to_sign": "0",
    "hostuin": "1021969591",
    "code_version": "1",
    "format": "fs",
    "qzreferrer": "https%3A%2F%2Fuser.qzone.qq.com%2F1021969591"
}

response = s.post(shuoshuo_url, headers=headers, data=data_open2all)

print(response.text)
