# -*- coding: utf-8 -*- 
import urllib
import urllib2
import json
import time
from entity.event import EventEntity
from entity.eventkey import EventKeyEntity
from entity.replymessage import ReplyMessage
from xml.etree import ElementTree 

class WeiXinApi(object):
	"""docstring for WeiXinApi"""
	token = 'weixin'

	def __init__(self, grant_type='client_credential'):
		self.grant_type = grant_type
		
		self.appid = "appid"
		self.secret ="secret"
		self.access_token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type={self.grant_type}&appid={self.appid}&secret={self.secret}".format(self=self)
		self.weixin_url_request = WeiXinUrlRequest()

	#获取access token
	def get_access_token(self):
		token = self.weixin_url_request.post_request(self.access_token_url)
		jn = self.weixin_url_request.dict_format(token)
		return jn.get("access_token")

	#普通菜单
	def create_menu(self,post_data):
		token = self.get_access_token()
		url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}".format(token)
		return self.weixin_url_request.post_request(url,post_data)

	#个性化菜单
	def create_conditonal_menu(self,post_data):
		token = self.get_access_token()
		url = "https://api.weixin.qq.com/cgi-bin/menu/addconditional?access_token={0}".format(token)
		return self.weixin_url_request.post_request(url,post_data)

	#获取普通菜单
	def get_menu(self):
		token = self.get_access_token()
		url = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token={0}".format(token)
		return self.weixin_url_request.post_request(url)

	#删除菜单
	def delete_menu(self):
		token = self.get_access_token()
		url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={0}".format(token)
		return self.weixin_url_request.post_request(url)

	#获取公众号菜单配置
	def get_menu_config(self):
		token = self.get_access_token()
		url = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token={0}".format(token)
		return self.weixin_url_request.post_request(url)

class WeiXinUrlRequest(object):

	def post_request(self,url,data=None):
		parmas = json.dumps(data, ensure_ascii=False) if data !=None else data
		headers = {'Content-Type': 'application/json'} if data !=None else {}
		req = urllib2.Request(url,data=parmas,headers = headers)
		response = urllib2.urlopen(req)
		result = response.read()
		return result

	def dict_format(self,result):
		return json.loads(result)
		
class WeiXinMessage(object):

	def __init__(self,req_bodys):
		self.body = req_bodys
		self.msg_dict = {
			"event" : self.__event_handler,
			"text"	: self.__text_handler,
			"image"	: self.__image_handler
		}
		
	def reply_message(self):
		root = ElementTree.fromstring(self.body)  
		msg_type = root.findtext('MsgType') 
		return self.msg_dict[msg_type](msg_type,root)

	def __event_handler(self,msg_type,root):
		to_uesr_name = root.findtext('ToUserName') 
		from_user_name = root.findtext('FromUserName') 
		event = root.findtext("Event")
		event_key = root.findtext("EventKey")
		if event == EventEntity.click:
			if event_key == EventKeyEntity.music:
				return ReplyMessage.imageText.format(from_user_name,to_uesr_name,time.time(),"test","这是测试用的图片","http://1.wexininterface.applinzi.com/static/image/test.jpg","http://1.wexininterface.applinzi.com/static/image/test.jpg")

	def __text_handler(self,msg_type,root):
		
		to_uesr_name = root.findtext('ToUserName') 
		from_user_name = root.findtext('FromUserName') 
		content = root.findtext('Content') 
		return ReplyMessage.text.format(from_user_name,to_uesr_name,time.time(),msg_type,content)

	def __image_handler(self,msg_typ,root):
		pass

	
		
	
