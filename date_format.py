from datetime import datetime, timedelta, tzinfo, date

# time format 'YYYY-MM-DDTHH:MM:SS+01:00'

class TZ(tzinfo):
     """A time zone with an arbitrary, constant +01:00 offset."""
     def utcoffset(self, dt):
         return timedelta(hours=1, minutes=0)

def tomorrow(hh='00', mm='00'):
    return str(date.today() + timedelta(days=1)) + f'T{hh}:{mm}:00+01:00'