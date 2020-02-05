import datetime 
from dateutil import parser

def timelist(startTime,endTime,formation=None,*args,**keywords):
    start_time=parser.parse(startTime)
    end_time=parser.parse(endTime)
    time_range=end_time-start_time
    resolution=datetime.timedelta(**keywords)   # ex. resolution=datetime.timedelta(hours=1) 
    n_timestamp=int(time_range/resolution)
    if formation==None:
        time=[start_time+resolution*value for value in range(n_timestamp)]
        return time
    else:
        # time=[datetime.datetime.strftime(start_time+resolution*value,'%Y-%m-%d %H:%M:%S') for value in range(n_timestamp)]
        time=[datetime.datetime.strftime(start_time+resolution*value,formation) for value in range(n_timestamp)]
        return time

    