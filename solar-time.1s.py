#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# <bitbar.title>Apparent Solar Time</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Alexandre André</bitbar.author>
# <bitbar.author.github>XanderLeaDaren</bitbar.author.github>
# <bitbar.desc>Displays the apparent solar time. Specify your longitude in the script.</bitbar.desc>
# <bitbar.image>ttps://github.com/XanderLeaDaren/bitbar-solar-time/blob/master/bitbar_solar-time.jpg?raw=true</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/XanderLeaDaren/bitbar-solar-time</bitbar.abouturl>

import datetime
from math import sin
import time
import json
import urllib

def longitude():
    url = 'http://ipinfo.io/json'
    response = urllib.urlopen(url)
    data = response.read()
    return json.loads(data.decode('utf-8'))["loc"].split(",")[1]

def print_information():
    today = datetime.datetime.now()
    day = today.timetuple().tm_yday
    tz = time.timezone

    lg = float(longitude())
    pos = lg / 360 * 24 * 60
    eq_time = 7.655 * sin(2 * (day - 4)) + 9.873 * sin(4 * (day - 172))

    sun = today - datetime.timedelta(minutes = -pos + eq_time, seconds = -tz)

    print "☀️ " + sun.strftime('%H:%M:%S')
    print "---"
    print "Time Zone Offset: " + str(tz / 3600) + " h"
    print "Position Offset: %.3f" % pos + " min"
    print "Equation of Time: %.3f" % -eq_time + " min"

if __name__ == "__main__":
    print_information()
