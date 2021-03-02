import base64
import re

from PIL import Image
from selenium import webdriver
import requests, time, json
import threading

login_uin = '2944208466'  # 登录qq
pwd = 'xf210398'  # 登录密码

s = requests.Session()

cookies_ = {}
g_tk = [""]
c_s = "pgv_pvi=9817097216; RK=RD7xq0tZPk; ptcz=672b14695d9766a17c3f1432a205bfd8cd485b631a687cf8b23787de8a6e9537; tvfe_boss_uuid=349f9ce14790623d; pgv_pvid=220366552; pac_uid=0_5e8c3612e6829; eas_sid=M1Y6K1b4K3G9p079x3s4D5C3D8; uin_cookie=o1021969591; ied_qq=o1021969591; LOLWebSet_AreaBindInfo_1021969591=%257B%2522areaid%2522%253A%25222%2522%252C%2522areaname%2522%253A%2522%25E6%25AF%2594%25E5%25B0%2594%25E5%2590%2589%25E6%25B2%2583%25E7%2589%25B9%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221021969591%2522%252C%2522rolename%2522%253A%2522%25E5%2593%258E%25E5%2591%2580%25E8%25B5%25B7%25E4%25BB%2580%25E4%25B9%2588%25E5%2590%258D%25E5%2591%25A2%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1021969591%257C2%257C1021969591*%257C%257C%257C%257C%2525E5%252593%25258E%2525E5%252591%252580%2525E8%2525B5%2525B7%2525E4%2525BB%252580%2525E4%2525B9%252588%2525E5%252590%25258D%2525E5%252591%2525A2*%257C%257C%257C1614390966%257C%2522%252C%2522md5str%2522%253A%25226CE6EBD36ABC28CF840E3AC9BAC8FE90%2522%252C%2522roleareaid%2522%253A%25222%2522%252C%2522sPartition%2522%253A%25222%2522%257D; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; pt_sms_phone=176******67; Loading=Yes; ptui_loginuin=2944208466; cpu_performance_v8=42; _qpsvr_localtk=0.5391092440024532; pgv_info=ssid=s9015692268; uin=o2944208466; skey=@RuyCS951Z; p_uin=o2944208466; pt4_token=qsQSjOKVC2FnqwIbP*h6*NoFIHGylsTnAH8A2YBYXM0_; p_skey=vnvtcUrgxDyugNaHppAD4OivE0S9FpMGQm9NnjA1T6A_"


# 实例化出浏览器开始登录
def qq_login():
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--no-sandbox')
    chromedriver = r"C:\Users\10219\Desktop\chromedriver.exe"
    # driver = webdriver.Chrome(chromedriver, options=option)
    driver = webdriver.Chrome(chromedriver)

    driver.get('https://user.qzone.qq.com/')
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        # 如果页面存在登录的DIV，则模拟登录（遇到滑动的时候需要手动滑动，所以我在下面设置10秒）
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()  # 选择用户名框
        driver.find_element_by_id('u').send_keys(login_uin)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(pwd)
        driver.find_element_by_id('login_button').click()
        time.sleep(100)

    # 读取cookie后关闭浏览器
    cookies = driver.get_cookies()
    driver.quit()

    for cookie in cookies:
        if cookie['name'] == 'p_skey':
            skey = cookie['value']
        # s.cookies.set(cookie['name'], cookie['value'])
        cookies_[cookie['name']] = cookie['value']

    # 计算gtk
    e = 5381
    for i in range(len(skey)):
        e = e + (e << 5) + ord(skey[i])
    g_tk[0] = str(2147483647 & e)


def keep_login():
    qzone_url = "https://user.qzone.qq.com/2944208466"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        # "cookie": ";".join([k + "=" + v for k, v in cookies_.items()])
        "cookie": c_s
    }

    while True:
        response = s.get(qzone_url, headers=headers)
        time.sleep(120)


def post_shuoshuo(content, image_name):
    cookies = c_s.split(";")
    cookies_ = {}

    for cookie in cookies:
        cookies_[cookie.split("=")[0].strip()] = cookie.split("=")[1].strip()

    e = 5381
    for i in range(len(cookies_["p_skey"])):
        e = e + (e << 5) + ord(cookies_["p_skey"][i])
    g_tk[0] = str(2147483647 & e)
    upload_image_url = "https://up.qzone.qq.com/cgi-bin/upload/cgi_upload_image?g_tk={}&&g_tk={}".format(g_tk[0],
                                                                                                         g_tk[0])
    img_path = r"/var/QQ/{}".format(image_name)
    f = open(img_path, 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()
    img = Image.open(img_path)

    hd_width = img.size[0]
    hd_height = img.size[1]

    img = {
        "filename": "filename",
        "uin": login_uin,
        "skey": cookies_.get("skey"),
        "zzpaneluin": login_uin,
        "zzpanelkey": "",
        "p_uin": login_uin,
        "p_skey": cookies_.get("p_skey"),
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
        "backUrls": "http://upbak.photo.qzone.qq.com/cgi-bin/upload/cgi_upload_image,http://119.147.64.75/cgi-bin/upload/cgi_upload_image",
        "url": "https://up.qzone.qq.com/cgi-bin/upload/cgi_upload_image?g_tk={}".format(g_tk[0]),
        "base64": "1",
        "jsonhtml_callback": "callback",
        "picfile": ls_f,
        "qzreferrer": "https://user.qzone.qq.com/{}".format(login_uin)
    }

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        # "cookie": ";".join([k + "=" + v for k, v in cookies_.items()])
        "cookie": c_s
    }

    response = s.post(upload_image_url, headers=headers, data=img)

    resp_txt = response.text.replace('\n', '')

    resp = json.loads(re.findall(r'frameElement.callback\(({.*})\)', resp_txt)[0])
    print(resp)

    if resp.get("ret") != 0:
        return False

    data_open2all = {
        "syn_tweet_verson": "1",
        "paramstr": "1",
        "pic_template": "",
        "richtype": "1",
        "richval": ",{},{},{},{},{},{},,{},{}".format(resp["data"].get("albumid"), resp["data"].get("lloc"),
                                                      resp["data"].get("sloc"),
                                                      resp["data"].get("type"), resp["data"].get("height"),
                                                      resp["data"].get("width"),
                                                      resp["data"].get("height"), resp["data"].get("width")),
        "special_url": "",
        "subrichtype": "1",
        "pic_bo": "{}	{}".format(re.findall(r"bo=(.*)", resp["data"].get("pre"))[0],
                                    re.findall(r"bo=(.*)", resp["data"].get("url"))[0]),
        "who": "1",
        "con": content,  # 文字内容
        "feedversion": "1",
        "ver": "1",
        "ugc_right": "1",
        "to_sign": "0",
        "hostuin": login_uin,
        "code_version": "1",
        "format": "fs",
        "qzreferrer": "https://user.qzone.qq.com/{}".format(login_uin)
    }
    shuoshuo_url = "https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?&g_tk={}".format(
        g_tk[0])

    response = s.post(shuoshuo_url, headers=headers, data=data_open2all)

    resp = json.loads(re.findall(r'frameElement.callback\(({.*})\)', response.text)[0])
    print(resp)

    return True


t1 = threading.Thread(target=keep_login, daemon=True)

t1.start()
