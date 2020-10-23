import utime
import machine

try:
    import usocket as socket
except:
    import socket
try:
    import ustruct as struct
except:
    import struct

# (date(2000, 1, 1) - date(1900, 1, 1)).days * 24*60*60
NTP_DELTA = 3155673600

# The NTP host can be configured at runtime by doing: ntptime.host = 'myhost.org'
host = "pool.ntp.org"

def gettime():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    return val - NTP_DELTA

# When do we change to summertime?
def last_sunday_of_march(year):
    day = math.ceil(31 - ((((5 * year) / 4) + 4) % 7))
    month = 3
    return utime.mktime((year, month, day, 1, 0, 0, 0, 0))

# When do we change back to normal time?
def last_sunday_of_october(year):
    day = math.ceil(31 - ((((5 * year) / 4) + 1) % 7))
    month = 10
    return utime.mktime((year, month, day, 1, 0, 0, 0, 0))

# There's currently no timezone support in MicroPython, and the RTC is set in UTC time.
# This is a simple approach to convert UTC time to Danish CET/CEST time
# depending on time of year
def naive_timezone_adjustment(time_utc, timezone_offset):
    date = utime.localtime(time_utc)
    year = date[0]

    # Get summer/winter time change dates
    to_summer_time = last_sunday_of_march(year)
    to_winter_time = last_sunday_of_october(year)

    offset = 0
    if time_utc < to_summer_time:
        # We are before change to summertime
        offset = 0
    elif time_utc < to_winter_time:
        # We are at summertime, add +1 hour
        offset = 3600
    else:
        # We have changed back to winter time
        offset = 0

    return utime.localtime(time_utc + offset + timezone_offset*3600)


def settime(timezone_offset):
    now_utc = gettime()
    now = naive_timezone_adjustment(now_utc, timezone_offset)
    rtc.setTime(now[0], now[1], now[2], now[3], now[4], now[5])
