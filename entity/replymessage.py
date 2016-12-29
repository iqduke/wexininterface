
class ReplyMessage(object):
	
	text = '''
			<xml>
			<ToUserName><![CDATA[{0}]]></ToUserName>
			<FromUserName><![CDATA[{1}]]></FromUserName>
			<CreateTime>{2}</CreateTime>
			<MsgType><![CDATA[{3}]]></MsgType>
			<Content><![CDATA[{4}]]></Content>
			</xml>
			'''
	image = ""

	imageText = """
				<xml>
				<ToUserName><![CDATA[{0}]]></ToUserName>
				<FromUserName><![CDATA[{1}]]></FromUserName>
				<CreateTime>{2}</CreateTime>
				<MsgType><![CDATA[news]]></MsgType>
				<ArticleCount>1</ArticleCount>
				<Articles>
				<item>
				<Title><![CDATA[{3}]]></Title> 
				<Description><![CDATA[{4}]]></Description>
				<PicUrl><![CDATA[{5}]]></PicUrl>
				<Url><![CDATA[{6}]]></Url>
				</item>
				</Articles>
				</xml> 
				"""

		