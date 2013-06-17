from pweb.zh_cn import lang
from pweb.jade import jade_render

globe_settings = {}

def default_menus():
  menus = { "plugin":{  'href':'/plugin'
                      , 'title':'plugin'
                      , 'img':'static/images/tt2.menu.plugin.png'
                      , 'template':'views/plugin/main.jade' 
                      }
          }
  return menus
  
def default_globe():
  global globe_settings
  gSettingMenu = jade_render("views/settings.jade",lang=lang)
  globe_settings = { "menus":default_menus(), "lang":lang, "special_setting_menu":{}, "globe_setting_menu":gSettingMenu }

def get_globe():
  return globe_settings
    