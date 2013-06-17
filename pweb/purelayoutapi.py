from flask import request, render_template
from flask.views import MethodView
from pweb.jade import jade_render

import json

from pweb import app

globe_settings = {}

def get_globe():
  return globe_settings

def init_globe():
  global globe_settings
  _nav = jade_render('views/purelayout/navitems.jade')
  _list = jade_render('views/purelayout/listitems.jade')
  _main = jade_render('views/purelayout/mainitems.jade')
  globe_settings["special_nav"]={}
  globe_settings["globe_nav"]=_nav
  globe_settings["special_list"]={}
  globe_settings["globe_list"]=_list
  globe_settings["special_main"]={}
  globe_settings["globe_main"]=_main

class LoadItems(MethodView):
  def get(self,itemtype):
    module = request.args.get('my','')
    g = get_globe()
    _s = "special_"+itemtype
    _g = "globe_"+itemtype
    if g.has_key(_g):
      if g.has_key(_s) and module in g[_s]:
        return g[_s][module]+g[_g]
      else:
        return g[_g]
    else:
      pass
app.add_url_rule('/pureload/<itemtype>',view_func=LoadItems.as_view('pureload'))

