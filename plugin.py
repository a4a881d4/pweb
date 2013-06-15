import os
from import_file import import_file
mplugins = {}
plugins = []
plugin_files=os.listdir('plugins')
for file in plugin_files:
  if file[-2:]=='py':
    mplugin=import_file('plugins/'+file)
    plugins.append(mplugin.settings)
    mplugins[mplugin.settings['ID']]=mplugin
