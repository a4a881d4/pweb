from flask import Flask
app = Flask(__name__,template_folder='..',static_folder='../static')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

import pweb.views
