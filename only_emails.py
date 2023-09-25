from email.message import EmailMessage
import ssl
import smtplib

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login('jacobantoine506@gmail.com', 'bmhvvxwxevtxzmbz')
# content = '''
#     Hi, an email from the wizard
# '''
# server.sendmail("jacobantoine506@gmail.com", "adamssteph456@gmail.com", content)
# print("email gone")

from email.message import EmailMessage

msg = EmailMessage()


msg["From"] = "jacobantoine506@gmail.com"
msg["To"] = "ab.ayebea@gmail.com,tsikatawill@gmail.com,lkanner21@gmail.com,topboyasante@gmail.com,etiboah@gmail.com,slightly.techie@gmail.com,tonnybright35@gmail.com,bquansah007@gmail.com,samson.dadson@gmail.com,abbeyeleazer@gmail.com,agyakomajas@gmail.com,ahinakwahcaleb@gmail.com,akkatsekpor@gmail.com,amissahevans95@gmail.com,b.afedzi@gmail.com,cyrilawadey@gmail.com,dandarkamo1@gmail.com,danielkwammy@gmail.com,derrickyebs@gmail.com,edemcoffie41@gmail.com,forsonbaah@gmail.com,frederickotuafro@gmail.com,gertrude.kaneah.abagale@gmail.com,info.benandy.news@gmail.com,iscoolbruce@gmail.com,jacobantoine506@gmail.com,jerrykrah20@gmail.com,ken.ahonya@gmail.com,kingdela1@gmail.com,kusiwaahboateng1997@gmail.com,lizamimi7@gmail.com,maestrofly3@gmail.com,malikbanks01@gmail.com,mimiiboateng3@gmail.com,obengagyen@gmail.com,p.afflade123@gmail.com,philpottersmith@gmail.com,pyawinbe@gmail.com,ranceasamoah50@gmail.com,rechealgademehetornam@gmail.com,rkboahene2@gmail.com,sammiedaga@gmail.com,sammyostii@gmail.com,sefordzip@gmail.com,setrivigil@gmail.com,seyliemenz@gmail.com,thekwakuvictus@gmail.com,yaafrimpomaaboateng@gmail.com,yadjeidarko@gmail.com,frank.amoako-dev@outlook.com,abdulazizmohammed313@yahoo.com,derrickalberto@ymail.com,dkteng@outlook.com,marvinalamu_1@live.com"
# msg["Cc"] = "gibsonbrian389@gmail.com, fredrobertson815@gmail.com"
# msg["Bcc"] = "invisible@example.int, undisclosed@example.org.au"
msg["Subject"] = "Hello from the other side"

msg.set_content('''Sorry to interrupt, this is Stephen, 
                your fellow slightly Techie student, drop your twitter handl, let us connect,mine is @wizardincarnate''')
# You can put an HTML body instead by ading a subtype string argument "html"
# msg.set_content("<p>This is the main text/html message.</p>", "html")

# You can add attachments of various types as you see fit;
# if there are no other parts, the message will be a simple
# text/plain or text/html, but Python will change it into a
# suitable multipart/related or etc if you add more parts
# with open("image.png", "rb") as picture:
#     msg.add_attachment(picture.read(), maintype="image", subtype="png")

# Here, we use SMTP instead of SMTP_SSL, but pivot to encrypted
# traffic with STARTTLS after the initial handshake.
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # Some servers insist on this, others are more lenient ...
    # It is technically required by ESMTP, so let's do it
    # (If you use server.login() Python will perform an EHLO first
    # if you haven't done that already, but let's cover all bases)
    server.ehlo()
    # Whether or not to use STARTTLS depends on the mail server
    server.starttls()
    # Bewilderingly, some servers require a second EHLO after STARTTLS!
    server.ehlo()
    # Login is the norm rather than the exception these days
    # but if you are connecting to a local mail server which is
    # not on the public internet, this might not be useful or even possible
    server.login("jacobantoine506", "bmhvvxwxevtxzmbz")

    # Finally, send the message
    server.send_message(msg)