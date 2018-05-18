import datetime
def setTime(**kwargs):
    time = datetime.datetime.now().replace(microsecond=0)
    if 'month' in kwargs.keys():
        time = time.replace(month = kwargs['month'],day = 1,hour = 0,minute = 0,second = 0)
    if 'day' in kwargs.keys():
        time = time.replace(day = kwargs['day'],hour = 0,minute = 0,second = 0)        
    if 'hour' in kwargs.keys():
        time = time.replace(hour = kwargs['hour'],minute = 0,second = 0)        
    if 'minute' in kwargs.keys():
        time = time.replace(minute = kwargs['minute'],second = 0)
    return str(time)

def setTimeInteractive():
    args = {}
    month = input('month:')
    if month:
        args['month']=int(month)
    day = input('day:')
    if day:
        args['day']=int(day)
    hour = input('hour:')
    if hour:
        args['hour']=int(hour)
    minute = input('minute:')
    if minute:
        args['minute']=int(minute)
    return setTime(**args)  
