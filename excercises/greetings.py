#automated greetings according to time

import time
hour=int(time.strftime("%H",))
if hour<=11 and hour>=6:
    print("Gd Mg Sir")
elif hour<=15 and hour>=12:
    print("gd noon sir")
elif hour<=18 and hour>=16:
    print("gd afternoon sir")
elif hour<=21 and hour>=19:
    print("gd evening sir")
else:
    print("gd night...Sweet Dreams")
