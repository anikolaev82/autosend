# -*- coding: utf-8 -*- 
from .Call import Call
from .MailCommand import MailCommand


class SendMail():
	"""
		Создает настроенное почтовое сообщение в Outlook
	"""
	def __init__(self, p_attach):
		self.attach = '/a "{0}"'.format(p_attach)
		self.call = Call()
		
	def cr_form(self, *args):
		self.call.mail(*args)

	def run(self):
		cmd = MailCommand()
		self.cr_form(self.attach, cmd.get_command())