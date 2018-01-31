"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 31 January, 2018 @ 4:57 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask_react_template.server.config.base import Config, APP_NAME


class Production(Config):
    DATABASE_URI = f'mysql://victor@localhost/{APP_NAME}'


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
