# coding=utf-8
import json
from pweb import app
from pweb.globe import get_globe
from pweb.utils import build_menu
from flask import render_template
from pweb.purelayoutapi import get_globe as pure_globe

sRf = """{ "version" : "1"
         , "name" : "射频参数"
         , "description" : "设置射频参数"
         , "author" : "赵明"
         , "email" : "a4a881d4@126.com"
         , "ID" : "RFSET"
         , "menu" : { "href":"/rf"
                    , "title":"rf setting"
                    , "img":"static/images/tt2.menu.inbox.png"
                    , "template":"views/purelayout.jade"
                    }
}"""

settings = json.loads(sRf)

def init_globe( globe_setting ):
  if globe_setting.has_key("menus"):
    globe_setting["menus"][settings["ID"]]=settings["menu"]
  if globe_setting.has_key("special_setting_menu"):
    globe_setting["special_setting_menu"]["RFSET"] = """
      <li><a href="javascript:show_float_box( 'TeamToy' , '/dashboard/about' );void(0);">RF Setting</a>
      </li>
      <li class="divider"></li>
      """
  _pure = pure_globe()
  if _pure.has_key("special_nav"):
    _pure["special_nav"][settings["ID"]] = """
      <li><a href="javascript:show_float_box('set t freq', '/getsetting/tfreq');void(0);" id="tfreqview">T freq %lfM</a>
      </li>
    """ % 1980.0
  print _pure["special_nav"]
  
@app.route('/rf')
def rf():
  globe_settings=get_globe()
  return render_template('views/frame.jade',lang=globe_settings["lang"],menus=build_menu('RFSET'),my='RFSET')
@app.route('/getsetting/tfreq')
def tfreq():
  return render_template('plugins/rftset.jade')

