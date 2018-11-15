from nameparser import HumanName
import pandas as pd
import numpy as np

import time

'''
    download data from meetup.com
    convert it to xlsx
    #TODO - use meetup.com api if we continue to use the meetup.com's garbage rsvp system
'''

df = pd.read_excel('input.xlsx')
df.rename(columns={'Please enter your full name as it appears on your ID. This is required for security reasons for access to the venue.':'FullName'}, inplace=True)

df1 = df.replace(np.nan, '', regex=True)
res = pd.DataFrame()

res['MeetupName'] = df1['Name']
res['LastName'] = df1.apply(lambda x: HumanName(x['FullName']).last if x['FullName'] else '', axis=1)
res['FirstName'] = df1.apply(lambda x: HumanName(x['FullName']).first if x['FullName'] else '', axis=1)
res['Middle'] = df1.apply(lambda x: HumanName(x['FullName']).middle if x['FullName'] else '', axis=1)
res['Suffix'] = df1.apply(lambda x: HumanName(x['FullName']).suffix if x['FullName'] else '', axis=1)

pd.options.display.max_rows = 999
r=res.reindex(columns=['MeetupName','FirstName','Middle','LastName','Suffix'])

timestr = time.strftime("%Y%m%d-%H%M%S")
writer = pd.ExcelWriter(f'output_{timestr}.xlsx')
r.to_excel(writer,'Sheet1')
writer.save()

'''
    email to:
    chicagooffice AT braintreepayments DOT com
    community AT getbraintree DOT com
    ray
    zax
'''