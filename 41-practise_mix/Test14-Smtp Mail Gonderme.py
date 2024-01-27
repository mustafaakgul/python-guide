
import smtplib

content = "merhaba"

mail = smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()   #senn uzernden mail aticam demek bu

mail.starttls()   #encryption

mail.login("komonder93@gmail.com","beyinlikoltuk21")

mail.sendmail("komonder93@gmail.com","mustafaakgul@yandex.com",content)

#birde gmail uzernden bir ayar var oradan ayarın acılması lazım

