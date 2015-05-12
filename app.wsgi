import sys, os, bottle

sys.path.append('/var/www/python_bottle_experiment')
os.chdir(os.path.dirname(__file__))

import products # This loads your application

application = bottle.default_app()