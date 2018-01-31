"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 31 January, 2018 @ 4:30 PM.
  Copyright © 2018. Victor. All rights reserved.
"""

from flask_react_template.server import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')
