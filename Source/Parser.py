import xmljson, json
from xmljson import badgerfish as bf
from json import dumps, loads
from xml.etree.ElementTree import fromstring
def Parsing(filename):
    str = open(filename,'r').read()
    json = dumps(bf.data(fromstring(str))).replace("@", "")
    return json