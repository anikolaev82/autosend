# -*- coding: utf-8 -*- 
import configparser


class Config():
	
	config = configparser.ConfigParser()
	config.read('config.settings')
	
	MAIL = config['PROGRAMM']['MAIL']
	CRYPT = config['PROGRAMM']['CRYPT']
	RECEPIENT = config['CONFIG_MAIL']['RECEPIENT']
	SUBJECT = config['CONFIG_MAIL']['SUBJECT'].encode('cp1251').decode('utf8')
	BODY = config['CONFIG_MAIL']['BODY'].encode('cp1251').decode('utf8')
	KEY_ATTACH = config['KEY_MAIL']['ATTACH']
	KEY_MAILTO = config['KEY_MAIL']['MAILTO']
	CRYPT_PASS = config['CONFIG_CRYPT']['PASSWORD']
		