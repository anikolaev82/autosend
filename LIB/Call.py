# -*- coding: utf-8 -*- 
import subprocess
from .config import Config


class Call():
	def __init__(self):
		self._path_crypt = [Config.CRYPT]
		self._path_outlook = [Config.MAIL]
		
	def crypt(self, *args):
		call_programm = ' '.join(self._path_crypt + list(args))
		print(call_programm)
		subprocess.call(call_programm)
		
	def mail(self, *args):
		call_programm = ' '.join(self._path_outlook + list(args))
		print(call_programm)
		subprocess.call(call_programm)