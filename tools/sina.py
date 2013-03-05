import requests
import json
def requestinfo():
    data=requests.get("https://api.weibo.com/2/statuses/public_timeline.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE> public_timeline").text
    json.loads(data)
    # weibo

    # uinfo

