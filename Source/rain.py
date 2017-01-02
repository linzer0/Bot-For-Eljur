import parser
import config
import json
import telebot
bot = telebot.TeleBot(config.token)
class curitem(object):
    def __init__(self,room,num,name,teacher,grp_short=None,grp=None):
        self.room = room;
        self.num = num;
        self.name = name;
        self.teacher = teacher;
jsonStr = parser.Parsing(config.filename)
jsonStr = json.loads(jsonStr)
def Works():
        #print (20*'#')
        for i in range(0,5):
            day = jsonStr['response']['result']['day'][i]['title']
            bot.send_message(config.chat_id,day)
            for row in jsonStr['response']['result']['day'][i]['item']:
                d=curitem(**row)
                teacher=d.teacher
                room = d.room
                num = d.num
                name = d.name
                A = [teacher,name,str(num)]
                string = (' '.join(A))
                #bot.send_message(config.chat_id,"########")
                bot.send_message(config.chat_id,string)

            #print(20 * '#')
