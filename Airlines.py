
#Objective
#The goal of this SQL-based data analysis project is to identify opportunities to increase the occupancy rate on low-performing flights,
# ultimately leading to increased profitability for the airline.


import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import seaborn as sns

warnings.filterwarnings('ignore')

file_path = r"C:\Users\Lenovo\PycharmProjects\Sneha\Mini Project\travel.sqlite\travel.sqlite"

# Connect to the SQLite database
connection = sqlite3.connect(file_path)
cursor = connection.cursor()
print("Connection to the database was successful.")

cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
table_list = [table[0] for table in cursor.fetchall()]
print('List of tables present in the database:')
for table in table_list:
    print(table)

aircrafts_data=pd.read_sql_query("select * from aircrafts_data",connection)
print("\naircrafts_data")
print(aircrafts_data)

print("\n...............................................................................................\n")

airports_data=pd.read_sql_query("select * from airports_data",connection)
print("\nairports_data")
print(airports_data)

print("\n...............................................................................................\n")

boarding_passes=pd.read_sql_query("select * from boarding_passes",connection)
print("\nboarding_passes")
print(boarding_passes)

print("\n...............................................................................................\n")

bookings=pd.read_sql_query("select * from bookings",connection)
print("\nbookings")
print(bookings)

print("\n...............................................................................................\n")

flights=pd.read_sql_query("select * from flights",connection)
print("\nflights")
print(flights)

print("\n...............................................................................................\n")

seats=pd.read_sql_query("select * from seats",connection)
print("\nseats")
print(seats)

print("\n...............................................................................................\n")

ticket_flights=pd.read_sql_query("select * from ticket_flights",connection)
print("\nticket_flights")
print(ticket_flights)

print("\n...............................................................................................\n")

tickets=pd.read_sql_query("select * from tickets",connection)
print("\ntickets")
print(tickets)

for table in table_list:
    print("\n table:",table)
    column_info = connection.execute("Pragma table_info({})".format(table))
    for column in column_info.fetchall():
        print(column[1:3])

for table in table_list:
    print("\nTable:",table)
    df_table = pd.read_sql_query(f"select * from {table}",connection)
    print(df_table.isnull().sum())

print("\nBasic Analysis")
print("\nHow many Planes have more than 100 seats?\n")
seats=pd.read_sql_query("""\nSelect Aircraft_code , count(*) as num_seats from seats
                   group by aircraft_code""", connection)
print(seats)

print("\nHow the no of tickets booked with the time")
tickets=pd.read_sql_query("""select * from tickets inner join bookings
                    on tickets.book_ref=bookings.book_ref""",connection)
tickets['book_date']=pd.to_datetime(tickets['book_date'])
tickets['date']=tickets['book_date'].dt.date
x=tickets.groupby('date').size().reset_index(name='count')
plt.figure(figsize=(18,6))
plt.plot(x['date'],x['count'],marker='^')
plt.xlabel('Date',fontsize=20)
plt.ylabel('Number of Tickets',fontsize=20)
plt.grid('b')
plt.show()

print("\ncalculate the average charges for each aircraft with different fare conditions\n")
df=pd.read_sql_query("""select fare_conditions, aircraft_code,avg(amount) 
from ticket_flights join flights on ticket_flights.flight_id=flights.flight_id
group by aircraft_code, fare_conditions""",connection)
sns.barplot(data=df, x='aircraft_code', y='avg(amount)', hue='fare_conditions')
plt.show()
print(df)

print("\nAnalyzing occupancy rate")
print("\nFor each aircraft, calculate total revenue per year and the average revenue per ticket\n")
rate=pd.read_sql_query("""select aircraft_code, tickets_count, total_revenue, total_revenue/tickets_count as avg_revenue_per_ticket from 
(select aircraft_code, count(*) as tickets_count, sum(amount) as total_revenue from ticket_flights 
                     join flights on ticket_flights.flight_id=flights.flight_id group by aircraft_code)""",connection)
print(rate)

print("\nCalculate the average occupancy per aircraft.\n")
occupancy_rate=pd.read_sql_query("""SELECT
    a.aircraft_code,
    AVG(a.seats_count) AS booked_seats,
    b.num_seats,
    AVG(a.seats_count) / b.num_seats AS occupancy_rate
FROM
    (SELECT
        aircraft_code,
        flights.flight_id,
        COUNT(*) AS seats_count
    FROM
        boarding_passes
    INNER JOIN
        flights ON boarding_passes.flight_id = flights.flight_id
    GROUP BY
        aircraft_code, flights.flight_id) AS a
INNER JOIN
    (SELECT
        aircraft_code,
        COUNT(*) AS num_seats
    FROM
        seats
    GROUP BY
        aircraft_code) AS b ON a.aircraft_code = b.aircraft_code
GROUP BY
    a.aircraft_code;
""",connection)
print(occupancy_rate)

print("\ncalculate how much the total annual turnover could increase by giving all aircraft a 10% higher occupancy rate\n")
occupancy_rate['Inc occupancy_rate']=occupancy_rate['occupancy_rate'] + occupancy_rate['occupancy_rate']*0.1
occupancy_rate
pd.set_option("display.float_format",str)
total_revenue=pd.read_sql_query("""select aircraft_code, sum(amount) as total_revenue from ticket_flights
                  join flights
                  on ticket_flights.flight_id=flights.flight_id
                  group by aircraft_code""",connection)
occupancy_rate['Inc Total Annual Turnover']=(total_revenue['total_revenue'])/occupancy_rate['occupancy_rate']*occupancy_rate['Inc occupancy_rate']
occupancy_rate

print(total_revenue)


