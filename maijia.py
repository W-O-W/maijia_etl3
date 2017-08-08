#程序入口
import time
class maijia_etl:
    def __init__(self,conf):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        msg = "Begin '%s' work task!" % now
