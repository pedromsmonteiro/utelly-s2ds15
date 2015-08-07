# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 18:18:30 2015

@author: Client
"""

import pandas as pd

def aggregate_columns(column1, column2, name1, name2):
    df_name = name1 + '_VS_'+ name2 +'.csv'
    df = pd.DataFrame({name1: column1 , name2: column2})
    df.to_csv(df_name, sep=';')
    return df
   
 

  
aggregate_columns(range(0,10), range(1,11), 'a', 'b')   