# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 00:48:35 2019

@author: Vamshi Krishna
"""

import matplotlib.pyplot as plt
emp_names=['vamshi','preethi','santhosh','deexita']
emp_salary=[80000,75000,60000,80000]
plt.pie(emp_salary,labels=emp_names,radius=2,autopct='%0.0f%%',shadow=True,explode=[0.2,0,0,0])
plt.show()
