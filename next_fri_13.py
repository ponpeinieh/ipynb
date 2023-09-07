import datetime

# 今天的日期
today = datetime.datetime.now()
n=0
while n<10:
    today = today + datetime.timedelta(days=1)
    #print(today.strftime("%Y-%m-%d"))
    mday = today.day
    wday = today.weekday()
    if mday==13 and wday==4:
        print(today.strftime("%Y-%m-%d:%A"))
        n+=1

 

