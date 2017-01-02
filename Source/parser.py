
import xmljson, json
import requests

from xmljson import badgerfish as bf
from json import dumps, loads
from xml.etree.ElementTree import fromstring
def FileGet():
    File = open('path','r').read()
    MF=open('getschedule.xml','w')
    import requests
    r = requests.get(File)
    MF.write(r.text)
    MF.close()


def Parsing(filename):
    str = open(filename,'r').read()
    json = dumps(bf.data(fromstring(str))).replace("@", "")
    return json





