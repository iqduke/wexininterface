import tornado.web
import util.helper

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello,World!")
	
		