from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
bookings=pd.read_csv(ROOT/'data'/'hotel_bookings.csv',parse_dates=['booking_date','check_in','check_out'])
inventory=pd.read_csv(ROOT/'data'/'room_inventory.csv')

print('Duplicate booking IDs:',bookings['booking_id'].duplicated().sum())
print('Missing values:\n',bookings.isna().sum())

active=bookings.loc[~bookings['cancelled']].copy()
active['month']=active['check_in'].dt.to_period('M').astype(str)
active['revenue']=active['booking_value']

monthly=(active.groupby('month').agg(bookings=('booking_id','count'),room_nights=('nights','sum'),revenue=('revenue','sum'),adr=('nightly_rate','mean')).reset_index())
monthly['days']=pd.to_datetime(monthly['month']+'-01').dt.days_in_month
monthly['available_room_nights']=monthly['days']*inventory['units'].sum()
monthly['occupancy_pct']=100*monthly['room_nights']/monthly['available_room_nights']
monthly['revpar']=monthly['revenue']/monthly['available_room_nights']

channel=(bookings.groupby('channel').agg(bookings=('booking_id','count'),cancellation_rate=('cancelled','mean'),avg_lead_time=('lead_time_days','mean')).reset_index())
channel['cancellation_rate']*=100

print('\nMonthly KPIs:\n',monthly.round(2))
print('\nChannel Summary:\n',channel.round(2))

fig,ax=plt.subplots(figsize=(11,5.5))
x=pd.to_datetime(monthly['month']+'-01')
ax.plot(x,monthly['occupancy_pct'],marker='o')
ax.set_title('Monthly Occupancy')
ax.set_ylabel('Occupancy %')
fig.autofmt_xdate(); fig.tight_layout(); plt.show()
