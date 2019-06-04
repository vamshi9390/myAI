# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 00:38:55 2019

@author: Vamshi Krishna
"""

import pandas as pd
company=[{'Name':'Vamshi','Age':20,'salary':50000},
         {'Name':'Santhosh','Age':20,'salary':40000},
        {'Name':'Preethi','Age':18,'salary':40000}]
data=pd.DataFrame(company,index=[0,1,2])

data.plot.bar(x='Name',y='salary')



