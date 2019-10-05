import smtplib
import random
lis=[1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
code=str(random.choice(lis))+str(random.choice(lis))+str(random.choice(lis))+str(random.choice(lis))+str(random.choice(lis))+str(random.choice(lis))
content="Hey there!\n\nYou have requested for verification. Here is your temporary verification code: "+code+"\n\nDo not share this code with anyone.\n\nIf this were not you, then you may simply disregard this email.\n\n\nRegards,\nTeam Jumble Juggle."
print(code)
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
recipient=input('Recipent Email: ')
sender='noreply.jumblejuggle@gmail.com'
mail.login('noreply.jumblejuggle@gmail.com','Jumble@123')
header="To:"+recipient+"\n"+"From:"+sender+"\n"+"Subject:Confirmation for Jumble Juggle Sign Up\n"
content=header+content
mail.sendmail(sender,recipient,content)
mail.close()