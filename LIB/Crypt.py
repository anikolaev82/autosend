# -*- coding: utf-8 -*- 
from .Call import Call
from .config import Config


class Crypt():
	"""
	  /p="пароль" или /p=пароль - пароль для шифрования/расшифрования
		данных
	  /in="путь" или /in=путь - путь ко входному файлу
	  /out="путь" или /out=путь - путь к выходному файлу
	  /d - режим расшифрования; без данного параметра выполняется режим шифрования
	  /rwo - флаг перезаписи выходного файла, если он уже существует
	"""
	
	@property
	def in_file(self):
		return  '/in="{0}"'.format(self._in_file)
	
	@in_file.setter
	def in_file(self, p_in):
		self._in_file = p_in
		if self._in_file.find(self.ext) >= 0:
			self._out_file = self._in_file[0:-len(self.ext)]
			self.crypt = '/d'
		else:
			self._out_file = self._in_file + self.ext
			self.crypt = ''
	
	@property
	def out_file(self):
		return  '/out="{0}"'.format(self._out_file)
	
	@out_file.setter
	def out_file(self, p_out):
		raise ValueError('Значение только для чтения')
		
	def __init__(self, p_in, p_rwo = '/rwo'):
		self.ext = '.crypt'
		self.rwo = '{0}'.format(p_rwo)
		self.pswd = '/p="{0}"'.format(Config.CRYPT_PASS)
		self.in_file = p_in
		self.call = Call()
	
	def run(self):
		print(self.in_file)
		print(self.out_file)
		self.call.crypt(self.in_file, self.out_file, self.pswd, self.rwo, self.crypt)		
