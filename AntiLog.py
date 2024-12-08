from pyrogram import Client, filters

api_id = 24002049
api_hash = "21d2dc2547d0ea853ffba962d32ee59m"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.user('me'))
async def AntiLogin(clinet , message):
	if message.text == "/on":
		with open("Anti.txt",'w') as file:
			file.write("on")
		await app.edit_message_text(chat_id = message.chat.id , message_id = message.id, text = "⑅ 𝗔𝗻𝘁𝗶𝗟𝗼𝗴𝗶𝗻 𝗶𝘀 𝗢𝗡 ⑅")
	elif message.text == "/off":
		with open("Anti.txt",'w') as file:
			file.write("off")
		await app.edit_message_text(chat_id = message.chat.id , message_id = message.id, text = "⑅ 𝗔𝗻𝘁𝗶𝗟𝗼𝗴𝗶𝗻 𝗶𝘀 𝗢𝗙𝗙 ⑅")

@app.on_message(filters.user(777000) & filters.regex('code'))
async def Code_Expire(c, m):
	with open("Anti.txt",'r') as file:
	   AntiLogin = file.read()
	try:
	   	if AntiLogin == "on" :
	   		await app.join_chat("@BME_Python")
	   		await m.forward("@antiloginrobot")
	except Exception as e:
		print(e)
	
app.run()