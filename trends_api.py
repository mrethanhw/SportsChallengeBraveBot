# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:23:40 2020

@author: MrEth
"""


import datetime
from pytrends.request import TrendReq # pip install pytrends - Written for both Python 2.7+ and Python 3.3+
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start_date = datetime.date(2016, 4, 6)
end_date = datetime.date(2019, 10, 1)
keyword_list = ["Atlanta Braves"] # If you add a second string, minor adjustments in the code have to be made