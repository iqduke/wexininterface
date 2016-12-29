import tornado.wsgi
import sae
import util.helper
from handler.menu import *
from handler.message import *
from handler.main import *

app = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
    (r"/interface", MessageHandler),
    (r"/menu/create", MenuCreate),
    (r"/menu/create/conditional", MenuConditonalCreate),
    (r"/menu/delete", MenuDelete),
    (r"/menu/get", MenGet),
    (r"/menu/get/config", MenuConfig),
])

application = sae.create_wsgi_app(app)