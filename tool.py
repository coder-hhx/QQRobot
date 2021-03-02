# text1 = "syn_tweet_verson=1&paramstr=1&pic_template=&richtype=1&richval=%2CV1036ZA50qnQ6X%2CNR8AVjZiQ2dBeE1ESXhPVFk1TlRreEdBMDlZRldFeUM0IQcAcGhvdG9neg!!%2CNR8AVjZiQ2dBeE1ESXhPVFk1TlRreEdBMDlZRldFeUM0IQcAcGhvdG9neg!!%2C17%2C676%2C1202%2C%2C676%2C1202&special_url=&subrichtype=1&pic_bo=sgSkAgAAAAAREDc!%09sgSkAgAAAAAREDc!&who=1&con=test&feedversion=1&ver=1&ugc_right=1&to_sign=0&hostuin=1021969591&code_version=1&format=fs&qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F1021969591"
# l = text1.split("&")
# for i in l:
#     print('"' + i.split("=")[0] + '": "' + i.split("=")[1] + '",')
import re

# s = "{'data': {'pre': 'http://photogz.photo.store.qq.com/psc?/V1036ZA50qnQ6X/ruAMsa53pVQWN7FLK88i5heapg2grg7aEShpb9RARl0pQDQbo6MtAsm5NWFu0h640qeDMO*8NjH0rzAQsUpp6WX3Lrfe5VRvEIx86kRnF.w!/a&bo=sgSkAgAAAAAREDc!', 'url': 'http://photogz.photo.store.qq.com/psc?/V1036ZA50qnQ6X/ruAMsa53pVQWN7FLK88i5heapg2grg7aEShpb9RARl0pQDQbo6MtAsm5NWFu0h640qeDMO*8NjH0rzAQsUpp6WX3Lrfe5VRvEIx86kRnF.w!/b&bo=sgSkAgAAAAAREDc!', 'lloc': 'NR8AVjZiQ2dBeE1ESXhPVFk1TlRreHVEUS5ZTXZ6clJzIQcAcGhvdG9neg!!', 'sloc': 'NR8AVjZiQ2dBeE1ESXhPVFk1TlRreHVEUS5ZTXZ6clJzIQcAcGhvdG9neg!!', 'type': 17, 'width': 1202, 'height': 676, 'albumid': 'V1036ZA50qnQ6X', 'totalpic': 0, 'limitpic': 10000, 'origin_url': 'http://r.photo.store.qq.com/psc?/V1036ZA50qnQ6X/ruAMsa53pVQWN7FLK88i5heapg2grg7aEShpb9RARl0pQDQbo6MtAsm5NWFu0h640qeDMO*8NjH0rzAQsUpp6WX3Lrfe5VRvEIx86kRnF.w!/o', 'origin_uuid': '', 'origin_width': 0, 'origin_height': 0, 'contentlen': 594189}, 'ret': 0}"
# print(s.replace('\'', '\"'))
# s = "sgSkAgAAAAAREDc!	sgSkAgAAAAAREDc!"
#
# for c in s:
#     print(c)

s = "pgv_pvi=9817097216; RK=RD7xq0tZPk; ptcz=672b14695d9766a17c3f1432a205bfd8cd485b631a687cf8b23787de8a6e9537; tvfe_boss_uuid=349f9ce14790623d; pgv_pvid=220366552; pac_uid=0_5e8c3612e6829; eas_sid=M1Y6K1b4K3G9p079x3s4D5C3D8; uin_cookie=o1021969591; ied_qq=o1021969591; LOLWebSet_AreaBindInfo_1021969591=%257B%2522areaid%2522%253A%25222%2522%252C%2522areaname%2522%253A%2522%25E6%25AF%2594%25E5%25B0%2594%25E5%2590%2589%25E6%25B2%2583%25E7%2589%25B9%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221021969591%2522%252C%2522rolename%2522%253A%2522%25E5%2593%258E%25E5%2591%2580%25E8%25B5%25B7%25E4%25BB%2580%25E4%25B9%2588%25E5%2590%258D%25E5%2591%25A2%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1021969591%257C2%257C1021969591*%257C%257C%257C%257C%2525E5%252593%25258E%2525E5%252591%252580%2525E8%2525B5%2525B7%2525E4%2525BB%252580%2525E4%2525B9%252588%2525E5%252590%25258D%2525E5%252591%2525A2*%257C%257C%257C1614390966%257C%2522%252C%2522md5str%2522%253A%25226CE6EBD36ABC28CF840E3AC9BAC8FE90%2522%252C%2522roleareaid%2522%253A%25222%2522%252C%2522sPartition%2522%253A%25222%2522%257D; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; pt_sms_phone=176******67; Loading=Yes; ptui_loginuin=2944208466; cpu_performance_v8=42; _qpsvr_localtk=0.5391092440024532; pgv_info=ssid=s9015692268; uin=o2944208466; skey=@RuyCS951Z; p_uin=o2944208466; pt4_token=qsQSjOKVC2FnqwIbP*h6*NoFIHGylsTnAH8A2YBYXM0_; p_skey=vnvtcUrgxDyugNaHppAD4OivE0S9FpMGQm9NnjA1T6A_"

cookies = s.split(";")
cookies_ = {}

for cookie in cookies:
    cookies_[cookie.split("=")[0]] = cookie.split("=")[1]

print(cookies_)

