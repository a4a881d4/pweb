from pweb import app
from flask import render_template
from pweb.globe import get_globe
from pweb.plugin import init_globe

init_globe()

def build_menu(active):
  menus=[]
  globe_settings=get_globe()
  for menu in globe_settings["menus"]:
    if 'active' in globe_settings["menus"][menu]:
      globe_settings["menus"][menu]['active']=False
    if active == menu:
      globe_settings["menus"][menu]['active']=True
    menus.append( globe_settings["menus"][menu] )
  return menus
    
@app.route('/')
def hello_world():
  globe_settings=get_globe()
  return render_template('frame.jade',lang=globe_settings["lang"],menus=build_menu('dashboard'),my='dashboard')

@app.route('/dashboard')
def dashboard():
  globe_settings=get_globe()
  return render_template('frame.jade',lang=globe_settings["lang"],menus=build_menu('dashboard'),my='dashboard')

@app.route('/plugin')
def plugin():
  globe_settings=get_globe()
  return render_template('frame.jade',lang=globe_settings["lang"],menus=build_menu('plugin'),my='plugin')


