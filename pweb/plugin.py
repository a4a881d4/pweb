import os
from import_file import import_file
import json
from pweb.globe import default_globe
from pweb.globe import get_globe

mplugins = {}
plugins = []
plugin_files=os.listdir('plugins')
for file in plugin_files:
  if file[-2:]=='py':
    mplugin=import_file('plugins/'+file)
    plugins.append(mplugin.settings)
    mplugins[mplugin.settings['ID']]=mplugin
    
def plugin_settings():
  return json.loads(open('plugin_settings.json').read())

def save_plugin_settings( settings ):
  with open('plugin_settings.json', 'w') as outfile:
    json.dump( settings, outfile )

def init_globe():
  default_globe()
  globe_settings = get_globe()
  settings=plugin_settings()
  for k in mplugins:
    if k in settings and settings[k]=="active":
      if mplugins[k].init_globe:
        mplugins[k].init_globe( globe_settings )
