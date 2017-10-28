# -*- coding: utf-8 -*- 
import zipfile
import collections
import os


class ArcZip():
	
	def __init__(self, p_path):
		if p_path is not None:
			self.path = p_path
		else:
			raise ValueError('Не указан путь')
		
	def _get_name_file_arc(self):
		self.zipfile = os.path.join(self.path, os.path.split(self.path)[1] + '.zip')
		return self.zipfile
		
	def _create_zipfile(self):
		zip = zipfile.ZipFile(self._get_name_file_arc(), 'w')
		return zip
		
	def run(self):
		zip = self._create_zipfile()
		for root, dirs, files in os.walk(self.path):
			for file in files:
				f = os.path.join(root, file)
				zip.write(f)
		zip.close
