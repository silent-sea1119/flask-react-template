"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 31 January, 2018 @ 3:07 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import Flask

from flask_react_template.settings import STATIC_FOLDER, TEMPLATE_FOLDER, APP_NAME

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config.from_object(f'{APP_NAME}.server.config.mode.Development')

from flask_react_template.server.views import *
