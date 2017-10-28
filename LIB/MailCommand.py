from .config import Config


class MailCommand():
	
	def __init__(self):
		print(Config.SUBJECT)
		self.command = Config.KEY_MAILTO + ' "' + Config.RECEPIENT+'&subject='+Config.SUBJECT+'"'
	
	def get_command(self):
		return self.command