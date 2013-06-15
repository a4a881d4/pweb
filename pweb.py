from flask import Flask, render_template_string, render_template
from zh_cn import Lang  
app = Flask(__name__,template_folder='views')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

         
@app.route('/')
def hello_world():
  return render_template('dashboard.jade',lang=Lang())
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
