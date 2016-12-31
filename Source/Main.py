import parser
import config
import json
class curitem(object):
    def __init__(self,room,num,name,teacher,grp_short=None,grp=None):
        self.room = room;
        self.num = num;
        self.name = name;
        self.teacher = teacher;
        #self.grp_short=grp_short
        #self.grp = grp
jsonStr = parser.Parsing(config.filename)
#print jsonStr
jsonStr = json.loads(jsonStr)
#print jsonStr
def Works():
    print (20*'#')

    for i in range(0,5):
        day = jsonStr['response']['result']['student']['day'][i]['title']
        print (day)
        for row in jsonStr['response']['result']['student']['day'][i]['item']:

            d=curitem(**row)
            teacher=d.teacher
            room = d.room
            num = d.num
            name = d.name
            print (num,name,room,teacher)

