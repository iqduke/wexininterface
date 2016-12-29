# -*- coding: utf-8 -*- 

import tornado.web
import util.helper

class MenuCreate(tornado.web.RequestHandler):
	"""docstring for MenuCreate"""
	def get(self):
		menu =	{"button":[{"type":"click","name":"今日歌曲","key":"V1001_TODAY_MUSIC"},{"name":"菜单","sub_button":[{"type":"view","name":"搜索","url":"http://www.soso.com/"},{"type":"view","name":"视频","url":"http://v.qq.com/"}]}]}
				
		wxApi = util.helper.WeiXinApi();
		result = wxApi.create_menu(menu)		

		self.write(result)

class MenuConditonalCreate(tornado.web.RequestHandler):
	"""docstring for MenuCreate"""
	def get(self):
		menu =	{
				 	"button":[
				 	{	
				    	"type":"click",
				    	"name":"今日歌曲",
				     	"key":"V1001_TODAY_MUSIC" 
					},
					{ 
						"name":"菜单",
						"sub_button":[
						{	
							"type":"view",
							"name":"搜索",
							"url":"http://www.soso.com/"
						},
						{
							"type":"view",
							"name":"视频",
							"url":"http://v.qq.com/"
						},
						{
							"type":"click",
							"name":"赞一下我们",
							"key":"V1001_GOOD"
						}]
				 }],
				"matchrule":{
				  "group_id":"2",
				  "sex":"1",
				  "country":"中国",
				  "province":"广东",
				  "city":"广州",
				  "client_platform_type":"2",
				  "language":"zh_CN"
				  }
				}
				
		wxApi = util.helper.WeiXinApi();
		result = wxApi.create_menu(menu)		

		self.write(result)
        

class MenuDelete(tornado.web.RequestHandler):
	"""docstring for MenuDelete"""
	def get(self):
		wxApi = util.helper.WeiXinApi();
		result = wxApi.delete_menu()

		self.write(result)

class MenGet(tornado.web.RequestHandler):
	"""docstring for Menu"""
	def get(self):
		wxApi = util.helper.WeiXinApi();
		result = wxApi.get_menu()

		self.write(result)
		
class MenuConfig(tornado.web.RequestHandler):
	"""docstring for MenuConfig"""
	def get(self):
		wxApi = util.helper.WeiXinApi();
		result = wxApi.get_menu_config()

		self.write(result)
		