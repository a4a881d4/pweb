from pweb import app
from flask import render_template
from pweb.globe import get_globe
from pweb.utils import build_menu
from pweb.plugin import init_globe


init_globe()

@app.route('/')
def hello_world():
  globe_settings=get_globe()
  return render_template('views/frame.jade',lang=globe_settings["lang"],menus=build_menu('plugin'),my='plugin')

@app.route('/dashboard')
def dashboard():
  globe_settings=get_globe()
  return render_template('views/frame.jade',lang=globe_settings["lang"],menus=build_menu('dashboard'),my='dashboard')

@app.route('/plugin')
def plugin():
  globe_settings=get_globe()
  return render_template('views/frame.jade',lang=globe_settings["lang"],menus=build_menu('plugin'),my='plugin')


