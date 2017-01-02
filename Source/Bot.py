#-*- coding: utf-8 -*-
import parser,json,config,telebot
from telebot import types
def chek(str):
    digitcount=0
    charcounter=0
    for i in str:
        if(i.isdigit()==True):
            digitcount=1;
        elif(i.isalpha()==True):
            charcounter=1
    if(digitcount==1 & charcounter==1):
        return True
    else:
        return False
Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []
Saturday = []
bot = telebot.TeleBot(config.token)
class curitem(object):
    def __init__(self,room,num,name,teacher,grp_short=None,grp=None):
        self.room = room;
        self.num = num;
        self.name = name;
        self.teacher = teacher;
AllClass= types.ReplyKeyboardMarkup().row('11', '10', '9', '8', '7')
Week = types.ReplyKeyboardMarkup().row('Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Назад')
reply_markup=AllClass
OneClass = types.ReplyKeyboardMarkup()
bot.send_message(config.chat_id, "Нажми на класс,у которого желаешь узнать расписание:", reply_markup=AllClass)

class curitem(object):
    def __init__(self, room, num, name, teacher, grp_short=None, grp=None):
        self.room = room;
        self.num = num;
        self.name = name;
        self.teacher = teacher;
@bot.message_handler(func=lambda message: True, content_types=['text'])
def detector(message):
    #AllClass.selective=False
    #print (message.text)
    r = message.text
    if(r=='11'):
        print("ElEVEN")
        OneClass.row('11А', '11Б', '11В','11Г','11Д','11Е','11Ж','Назад')
        bot.send_message(message.chat.id, "Укажи параллель:", reply_markup=OneClass)
    elif(r=='10'):
        print("TEN")
        OneClass.row('10А', '10Б','10В','10Г', '10Д','10Е','Назад')
        bot.send_message(message.chat.id, "Укажи параллель:", reply_markup=OneClass)
    elif(r=='9'):
        print("NINE")
        OneClass.row('9А', '9Б', '9В','9Г','9Г','9Д','9Е','9Ж','Назад')
        bot.send_message(message.chat.id, "Укажи параллель:", reply_markup=OneClass)
    elif(r=='8'):
        print("EIGHT")
        OneClass.row('8А', '8Б', '8В','8Г','Назад')
        bot.send_message(message.chat.id, "Укажи параллель:", reply_markup=OneClass)
    elif(r=='7'):
        print("SEVEN")
        OneClass.row('7А','7В','Назад')
        bot.send_message(message.chat.id, "Укажи параллель:", reply_markup=OneClass)
    #print(r)
    if(r=='Назад'):
        bot.send_message(config.chat_id, "Нажми на класс,у которого желаешь узнать расписание:", reply_markup=AllClass)

        print("BACK")
    if(chek(r)==True):
        print("Ready")
        path = "https://api.eljur.ru/api/getschedule?login=linzet&password=56564321&vendor=rbli&devkey=4a1e97af538db6faf5b0220aefacb3d4&class=" + r
        #print(path)
        q = open('path','w')
        q.write(path)
        q.close()
        parser.FileGet()
        jsonStr = parser.Parsing(config.filename)
        jsonStr = json.loads(jsonStr)

        def Works():
            # print (20*'#')
            Monday.clear(),Saturday.clear(),Thursday.clear(),Wednesday.clear(),Friday.clear(),Tuesday.clear()
            for i in range(0, 6):
                day = jsonStr['response']['result']['day'][i]['title']
                #bot.send_message(config.chat_id, day)
                for row in jsonStr['response']['result']['day'][i]['item']:
                    d = curitem(**row)
                    teacher = d.teacher
                    room = d.room
                    num = d.num
                    name = d.name
                    A=[str(num),name,teacher]
                    string = (' '.join(A))
                    string = string.ljust(50," ")
                    if (day == 'Понедельник'):
                        Monday.append(string)
                    elif(day=='Вторник'):
                        Tuesday.append(string)
                    elif(day=='Среда'):
                        Wednesday.append(string)
                    elif(day=='Четверг'):
                        Thursday.append(string)
                    elif(day=='Пятница'):
                        Friday.append(string)
                    elif(day=='Суббота'):
                        Saturday.append(string)
                        # bot.send_message(config.chat_id,"########")
                        #print(string)

        Works()
        bot.send_message(message.chat.id, "Укажи день недели:", reply_markup=Week)
    print(r)
    onestr = ""

    if(r=='Понедельник'):
        for i in Monday:
            onestr=onestr+i+'\n'
        bot.send_message(config.chat_id,onestr)

    elif (r == 'Вторник'):
        for i in Tuesday:
            onestr = onestr + i + '\n'
        bot.send_message(config.chat_id, onestr)
    elif (r == 'Среда'):
        for i in Wednesday :
            onestr = onestr + i + '\n'
        bot.send_message(config.chat_id, onestr)
    elif (r == 'Четверг'):
        for i in Thursday:
            onestr = onestr + i + '\n'
        bot.send_message(config.chat_id, onestr)
    elif (r == 'Пятница'):
        for i in Friday :
            onestr = onestr + i + '\n'
            bot.send_message(config.chat_id, onestr)
    elif(r=='Суббота'):
        for i in Saturday:
            onestr = onestr + i + '\n'
        bot.send_message(config.chat_id, onestr)

bot.polling(none_stop=True,interval=0)