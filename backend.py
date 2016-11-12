import json
import urllib2

#cue support
# from cue_sdk import *
# Corsair = CUESDK("CUESDK.x64_2013.dll")
# Corsair.RequestControl(CAM.ExclusiveLightingControl)

mint =  urllib2.urlopen("http://intuit-mint.herokuapp.com/api/v1/user/transactions").read()
print mint