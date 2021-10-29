# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 12:06:00 2021

@author: user
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())