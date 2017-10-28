# -*- coding: utf-8 -*- 
from LIB.Crypt import Crypt
from LIB.SendMail import SendMail
from LIB.arczip import ArcZip
	
	
zip = ArcZip(path)
zip.run()

crypt = Crypt(zip.zipfile)
crypt.run()
	
mail = SendMail(crypt._out_file)
mail.run()
	
