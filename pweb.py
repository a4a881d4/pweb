from flask import Flask, request, render_template
from zh_cn import lang
from menu import menus
from plugin import plugins  
app = Flask(__name__,template_folder='views')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

def clean_menu():
  for menu in menus:
    if 'active' in menu:
      menu['active']=False
    
@app.route('/')
def hello_world():
  clean_menu()
  menus[0]['active']=True
  return render_template('frame.jade',lang=lang,menus=menus,my='dashboard')

@app.route('/dashboard')
def dashboard():
  clean_menu()
  menus[0]['active']=True
  return render_template('frame.jade',lang=lang,menus=menus,my='dashboard')

@app.route('/plugin')
def plugin():
  clean_menu()
  menus[3]['active']=True
  return render_template('frame.jade',lang=lang,menus=menus,my='plugin')

@app.route('/load_settings',methods=['GET'])
def load_settings():
  if request.method == 'GET':
    module = request.args.get('my','')
    print module
    return render_template('settings.jade',lang=lang);

@app.route('/load_mainframe',methods=['GET'])
def load_mainframe():
  if request.method == 'GET':
    module = request.args.get('my','')
    print plugins[0]['description'].encode('gb2312')
    return render_template(module+'/main.jade',lang=lang,plugins=plugins);
      
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
