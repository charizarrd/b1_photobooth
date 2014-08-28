import datetime
import os
import re
import smtplib
import subprocess
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import Image

class Device:

    @staticmethod
    def _exec(cmd):
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE).communicate()[0].decode('utf-8')

    @staticmethod
    def raise_exception_if_not_installed():
        if not Device._exec('command -v gphoto2'):
            raise Exception('gPhoto2 is not installed')

    @classmethod
    def all(cls):
        cls.raise_exception_if_not_installed()

        description = cls._exec('gphoto2 --auto-detect | grep "usb"').strip()
        if not description:
            return []

        devices = []

        records = description.split('\n')

        for record in records:
            camera, port = record.split('usb:')
            camera, port = camera.strip(), 'usb:' + port.strip()
            devices.append(Device(camera, port))

        return sorted(devices)

    def __init__(self, camera, port):
        self.camera = camera
        self.port = port

    def capture(self, path):
        self.raise_exception_if_not_installed()

        cmd_tmpl = ('gphoto2 --quiet --camera "{0}" --port {1}'
                    ' --capture-image-and-download --filename "{2}"')
        cmd = cmd_tmpl.format(self.camera, self.port, path)
        self._exec(cmd)

    def __str__(self):
        return '{0} {1}'.format(self.camera, self.port)

    def __repr__(self):
        return 'Device("{0}", "{1}")'.format(self.camera, self.port)

    def __lt__(self, other):
        return self.port < other.port

    def __hash__(self):
        return hash((self.camera, self.port))

def take_photo():
    devices = Device.all()
    camera = devices[0]
    date = datetime.datetime.now().isoformat(' ')
    for x in range(0, 4):
        file_path = date + '-' + str(x)
        print(file_path)
        camera.capture('/Users/Leo/b1 photobooth/' + file_path + '.jpg')

    combine_photos(date)

def combine_photos(date):
    print("Combining photos into photostrip...")
    comp = Image.new('RGBA', (484,1296+190), (255, 255, 255, 255))
    for i in range(0, 4):
        file_path = date + '-' + str(i)
        img=Image.open('/Users/Leo/b1 photobooth/'+file_path+'.jpg','r')
        img.thumbnail((484,324), Image.ANTIALIAS)
        comp.paste(img, (0, i*324))
    img=Image.open('/Users/Leo/Downloads/b1 photobooth.jpg','r')
    comp.paste(img, (0, 4*324))
    comp_file_path = "/Users/Leo/b1 photobooth/" + date + ".jpg"
    comp.save(comp_file_path)
    get_email(comp_file_path)



def get_email(path):
    email = raw_input("Please enter your KERBOROS, not your email!: ")
    email = email + "@mit.edu"
    print("Sending to " + email + "...")
    send_email(email, path)

def send_email(email, path):
    img_data = open(path, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'B1 Photobooth'
    msg['From'] = 'charz@mit.edu'
    msg['To'] = email
    msg['Bcc'] = 'charz@mit.edu'

    text = MIMEText("Thanks for coming to B1 floor rush!")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(path))
    msg.attach(image)

    s = smtplib.SMTP('outgoing.mit.edu', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("charz", "hivincent1010")
    s.sendmail("charz@mit.edu", [email, "charz@mit.edu"] , msg.as_string())
    s.quit()

    print("Email sent! You will receive an email from charz@mit.edu")

if __name__ == "__main__":
    take_photo()
