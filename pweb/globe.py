from pweb.zh_cn import lang

globe_settings = {}

def default_menus():
  menus = { "dashboard":{'href':'/dashboard','title':'Todo','img':'static/images/tt2.menu.todo.png'}
          , "feed":{'href':'/feed','title':'feed','img':'static/images/tt2.menu.feed.png'}
          , "buddy":{'href':'/buddy','title':'buddy','img':'static/images/tt2.menu.buddy.png' }
          , "plugin":{'href':'/plugin','title':'plugin','img':'static/images/tt2.menu.plugin.png' }
          }
  return menus
  
def default_globe():
  global globe_settings
  globe_settings = { "menus":default_menus(), "lang":lang, "special_setting":{} }

def get_globe():
  return globe_settings
    