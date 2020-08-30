import cv2
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.naver.com"
port = 587
portssl = 465
userid = "otter35@naver.com"
passwd = "************"

def sendmail(image):
    to=[userid]
    imageByte=cv2.imencode(".jpeg", image)[1].tostring()
    msg = MIMEMultipart()
    imageMime=MIMEImage(imageByte)
    msg.attach(imageMime)
    msg["From"] = 'Me'
    msg["To"] = to[0]
    msg["Subject"] = "Invader is coming!"

    server = smtplib.SMTP_SSL(smtp_server, portssl)
#     server = smtplib.SMTP(smtp_server, port)
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    ret, m = server.login(userid, passwd)
    if ret != 235:
        print("login fail")
        return
    server.sendmail('me', to, msg.as_string())
    server.quit()

if __name__ == "__main__":
    sendmail('image_processing/images/load_image.jpg')
    