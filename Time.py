from datetime import datetime


def getTime(bool):

    time = datetime.now()
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    minutes = time.minute
    seconds = time.second

    if bool:
        print "%s/%s/%s %s:%s:%s" % (year, month, day, hour, minutes, seconds)
    else:
        itisnow = "%s/%s/%s %s:%s:%s" % (year, month, day, hour, minutes, seconds)
        return itisnow

