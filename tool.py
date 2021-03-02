# text1 = "syn_tweet_verson=1&paramstr=1&pic_template=&richtype=1&richval=%2CV1036ZA50qnQ6X%2CNR8AVjZiQ2dBeE1ESXhPVFk1TlRreEdBMDlZRldFeUM0IQcAcGhvdG9neg!!%2CNR8AVjZiQ2dBeE1ESXhPVFk1TlRreEdBMDlZRldFeUM0IQcAcGhvdG9neg!!%2C17%2C676%2C1202%2C%2C676%2C1202&special_url=&subrichtype=1&pic_bo=sgSkAgAAAAAREDc!%09sgSkAgAAAAAREDc!&who=1&con=test&feedversion=1&ver=1&ugc_right=1&to_sign=0&hostuin=1021969591&code_version=1&format=fs&qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F1021969591"
# l = text1.split("&")
# for i in l:
#     print('"' + i.split("=")[0] + '": "' + i.split("=")[1] + '",')
import json
import re

# s = "{'data': {'pre': 'http://photogz.photo.store.qq.com/psc?/V1036ZA50qnQ6X/ruAMsa53pVQWN7FLK88i5heapg2grg7aEShpb9RARl0pQDQbo6MtAsm5NWFu0h640qeDMO*8NjH0rzAQsUpp6WX3Lrfe5VRvEIx86kRnF.w!/a&bo=sgSkAgAAAAAREDc!', 'url': 'http://photogz.photo.store.qq.com/psc?/V1036ZA50qnQ6X/ruAMsa53pVQWN7FLK88i5heapg2grg7aEShpb9RARl0pQDQbo6MtAsm5NWFu0h640qeDMO*8NjH0rzAQsUpp6WX3Lrfe5VRvEIx86kRnF.w!/b&bo=sgSkAgAAAAAREDc!', 'lloc': 'NR8AVjZiQ2dBeE1ESXhPVFk1TlRreHVEUS5ZTXZ6clJzIQcAcGhvdG9neg!!', 'sloc': 'NR8AVjZiQ2dBeE1ESXhPVFk1TlRreHVEUS5ZTXZ6clJzIQcAcGhvdG9neg!!', 'type': 17, 'width': 1202, 'height': 676, 'albumid': 'V1036ZA50qnQ6X', 'totalpic': 0, 'limitpic': 10000, 'origin_url': 'http://r.photo.store.qq.com/psc?/V1036ZA50qnQ6X/ruAMsa53pVQWN7FLK88i5heapg2grg7aEShpb9RARl0pQDQbo6MtAsm5NWFu0h640qeDMO*8NjH0rzAQsUpp6WX3Lrfe5VRvEIx86kRnF.w!/o', 'origin_uuid': '', 'origin_width': 0, 'origin_height': 0, 'contentlen': 594189}, 'ret': 0}"
# print(s.replace('\'', '\"'))
# s = "sgSkAgAAAAAREDc!	sgSkAgAAAAAREDc!"
#
# for c in s:
#     print(c)

s = '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></head><body><script type="text/javascript">document.domain="qq.com";frameElement.callback({
   "data" : {
      "albumid" : "V118mEBI34vcIa",
      "contentlen" : 72186,
      "height" : 1920,
      "limitpic" : 10000,
      "lloc" : "",
      "pre" : "",
      "sloc" : "",
      "totalpic" : 3589,
      "type" : 1,
      "url" : "",
      "width" : 922
   },
   "ret" : 0
}
);</script></body></html>'''

s = s.replace('\n', '')
print(s)

print(json.loads(re.findall(r'frameElement.callback\(({.*})\)', s)[0]))

