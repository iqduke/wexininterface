import tornado.web
import util.helper
import hashlib

class MessageHandler(tornado.web.RequestHandler):
	
	def get(self):
		signature = self.get_argument("signature")
		timestamp = self.get_argument("timestamp")
		nonce = self.get_argument("nonce")
		echostr = self.get_argument("echostr")
		token = util.helper.WeiXinApi.token

		arr = [token,timestamp,nonce]
		arr.sort()

		temp = "".join(arr)
		tempsha1 = hashlib.sha1(temp)

		sha1 = tempsha1.hexdigest()

		self.write(echostr if (sha1 == signature) else "")

	def post(self):
		wxMessage = util.helper.WeiXinMessage(self.request.body)
		msg = wxMessage.reply_message();
		
		self.write(msg)
