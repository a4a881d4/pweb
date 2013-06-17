from flask import request, render_template
from flask.views import MethodView
from pweb.zh_cn import lang
from pweb.plugin import plugins, plugin_settings, save_plugin_settings, init_globe 
import json
from pweb import app
from pweb.globe import get_globe

class LoadSettings(MethodView):
  def get(self):
    module = request.args.get('my','')
    g = get_globe()
    if module in g["special_setting_menu"]:
      return g["special_setting_menu"][module]+g["globe_setting_menu"]
    else:
      return g["globe_setting_menu"]
      
app.add_url_rule('/load_settings',view_func=LoadSettings.as_view('load_settings'))

class LoadMainFrame(MethodView):
  def get(self):
    module = request.args.get('my','')
    g = get_globe()
    menu = g["menus"][module]
    return render_template( menu["template"]
                          , lang=lang
                          , plugins=plugins
                          , plugin_settings=plugin_settings()
                          , my=module
                          );
app.add_url_rule('/load_mainframe',view_func=LoadMainFrame.as_view('load_mainframe'))

class PluginTurn(MethodView):
  def get(self):
    if request.method == 'GET':
      ID = request.args.get('my','')
      settings=plugin_settings()
      if ID in settings:
        if  settings[ID]=="active":
          settings[ID]="deactive"
        else:
          settings[ID]="active"
      else:
        settings[ID]="active"
      save_plugin_settings(settings)
      init_globe()
    ret = {"err_code":0}
    return json.dumps(ret)                          
app.add_url_rule('/plugin_turn',view_func=PluginTurn.as_view('plugin_turn'))
