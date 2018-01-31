"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 31 January, 2018 @ 4:51 PM.
  Copyright © 2018. Victor. All rights reserved.
"""

import os

APP_NAME = 'flask_react_template'

PROJECT_DIR = os.getcwd()
PROJECT_SUB_DIR = os.path.join(PROJECT_DIR, APP_NAME)

CLIENT_FOLDER = os.path.join(PROJECT_SUB_DIR, 'client')
SERVER_FOLDER = os.path.join(PROJECT_SUB_DIR, 'server')

STATIC_FOLDER = os.path.join(CLIENT_FOLDER, 'static')
TEMPLATE_FOLDER = os.path.join(CLIENT_FOLDER, 'templates')
