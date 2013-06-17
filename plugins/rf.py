# coding=utf-8
import json
sRf = """{ "version" : "1"
         , "name" : "射频参数"
         , "description" : "设置射频参数"
         , "author" : "赵明"
         , "email" : "a4a881d4@126.com"
         , "ID" : "RFSET"
}"""

settings = json.loads(sRf)

def init_globe( globe_setting ):
  if globe_setting.has_key("menus"):
    rfmenu={'href':'/rf','title':'rf setting','img':'static/images/tt2.menu.inbox.png'}
    globe_setting["menus"]["RFSET"]=rfmenu
    