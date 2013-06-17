import pyjade
from jinja2 import Environment, FileSystemLoader
import os

def jade_render(file,**argv):
  THIS_DIR = os.path.dirname(os.path.abspath(__file__))
  j2_env = Environment( loader=FileSystemLoader(THIS_DIR+'/..')
                      , extensions=['pyjade.ext.jinja.PyJadeExtension']
                      , trim_blocks=True
                      )
  html = j2_env.get_template(file).render(argv)
  return html    