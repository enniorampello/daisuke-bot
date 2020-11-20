from datetime import datetime, timedelta, tzinfo, date

format = f'%Y-%m-%dT%H:%M:%S+01:00'

class TZ(tzinfo):
     """A time zone with an arbitrary, constant +01:00 offset."""
     def utcoffset(self, dt):
         return timedelta(hours=1, minutes=0)

def tomorrow(hh='00', mm='00', add_days=0) -> str:
    return str(date.today() + timedelta(days=1+add_days)) + f'T{hh}:{mm}:00+01:00'

def duration(event) -> int:
    datetime_end = datetime.strptime(event['end'].get('dateTime'), format)
    datetime_start = datetime.strptime(event['start'].get('dateTime'), format)
    return int((datetime_end - datetime_start).total_seconds() / 60)