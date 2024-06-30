Data Analysis Project

# Airlines Data Analysis 
## Steps Included 
* Understanding the Business Problem
* Importing Libraries
* Database connection to extract data
* Exploring tables present in the Database to identify key variables
* Analysing the key variables
* Creating Report with all the results and analysis for the company.

## Skills 
* Python (Pycharm)
* SQL(MySQL)

## Dataset
* Download the dataset from [Kaggle](https://www.kaggle.com/datasets/fiazbhk/airline-data-analysis?select=travel.sqlite).

## Business Problem
Our company operates a diverse fleet of aircraft ranging from small business jets to medium-sized machines. We have been providing high-quality air transportation services to our clients for several years, 
and our primary focus is to ensure a safe, comfortable, and convenient journey for our passengers. However, we are currently facing challenges due to several factors such as stricter environmental regulations,
higher flight taxes, increased interest rates, rising fuel prices, and a tight labor market resulting in increased labor costs. As a result, the company's profitability is under pressure, and they are seeking ways
to address this issue. To tackle this challenge, they are looking to conduct an analysis of their database to find ways to increase their occupancy rate, which can help boost the average profit earned per seat.

## Main Challenges
1. Stricter environmental regulations: The demand on the airlines industry to reduce its carbon footprint is growing, resulting in more stringent environmental laws that increase operating costs and restrict expansion potential.
3. Higher flight taxes: To address environmental issues and generate revenue, governments worldwide are imposing heavier taxes on aircraft, raising the cost of flying and decreasing demand.
4. Tight labor market resulting in increased labor costs: The shortage of trained personnel in aviation has driven up labor costs and increased turnover rates.

## Objectives
1. Increase Occupancy Rates: By raising occupancy rates, we can enhance the average profit per seat and alleviate the impact of the challenges we're facing.
2. Improve Price Strategy: We need to formulate a pricing strategy that considers the evolving market conditions and customer preferences, aiming to attract and retain customers.
3. Enhance Customer Experience: Our focus should be on delivering a seamless and convenient experience for our customers, spanning from booking to arrival. This approach will differentiate us in a highly competitive industry and foster customer loyalty.

#Goal:
The end goal of this task would be to identify opportunities to increase the occupancy rate on low-performing flights, which can ultimately lead to increased profitability for the airline.

## Basic Analysis
The basic analysis of data provides insights into the number of planes with more than 100 seats, how the number of tickets booked, and the total amount earned changed over time, 
as well as the average fare for each aircraft with different conditions. These findings will be helpful in developing strategies to optimize occupancy rates and pricing for each aircraft. 
**Table 1** shows the aircraft with more than 100 seats and the actual count of seats.

| aircraft_code | num_seats |
|---------------|-----------|
| 319           | 116       |
| 320           | 140       |
| 321           | 170       |
| 733           | 130       |
| 763           | 222       |
| 773           | 402       |

In order to gain a deeper understanding of the trend in ticket bookings and revenue earned through those bookings, we utilized a line chart visualization. Upon analysis of the chart, 
we observe that the number of tickets booked exhibits a gradual increase from June 22nd to July 7th, followed by a relatively stable pattern from July 8th until August, with a noticeable peak in ticket 
bookings where the highest number of tickets was booked on a single day. It is important to note that the revenue earned by the company from these bookings is closely tied to the number of tickets booked. 
Therefore, we can see a similar trend in the total revenue earned by the company throughout the analyzed time period. These findings suggest that further exploration of the factors contributing to the peak
in ticket bookings may be beneficial for increasing overall revenue and optimizing operational strategies.

**Figure 1*
We were able to generate a bar graph to graphically compare the data after completing computations for the average cost associated with different fare conditions for each aircraft. 
Figure 3 displays data for three types of fares: business, economy, and comfort. It's worth mentioning that the comfort class is available on only one aircraft, the 773. Conversely, 
the CN1 and CR2 planes provide only the economy class. When comparing different pricing circumstances within each aircraft, the charges for the business class are consistently greater than those for
the economy class. This trend may be observed across all planes, irrespective of fare conditions.
 
**Figure 3**

## Analyzing Occupancy Rate
Airlines must thoroughly analyze their revenue streams in order to maximize profitability. The overall income per year and average revenue per ticket for each aircraft are important metrics to consider. 
Airlines may use this information to determine which aircraft types and itineraries generate the most income and alter their operations appropriately. This research can also assist in identifying potential 
for pricing optimization and allocating resources to more profitable routes. The below Figure 4 shows the total revenue, total tickets, and average revenue made per ticket for each aircraft. The aircraft
with the highest total revenue is SU9, and from Figure 3, it can be seen that the price of the business class and economy class is the lowest on this aircraft. This could be the reason that most people 
bought tickets for this aircraft as it costs less compared to others. The aircraft with the least total revenue is CN1, and the possible reason behind this is that it only offers economy class with a very 
low price. It might be because of its poor conditions or fewer facilities.

| aircraft_code | total_revenue | tickets_count | avg_revenue_per_ticket |
|---------------|---------------|---------------|------------------------|
| 319           | 2706163100    | 52853         | 51201                  |
| 321           | 1638164100    | 107129        | 15291                  |
| 733           | 1426552100    | 86102         | 16568                  |
| 763           | 4371277100    | 124774        | 35033                  |
| 773           | 3431205500    | 144376        | 23765                  |
| CN1           | 96373800      | 14672         | 6568                   |
| CR2           | 1982760500    | 150122        | 13207                  |
| SU9           | 5114484700    | 365698        | 13985                  |

**Figure 4**

The average occupancy per aircraft is another critical metric to consider. Airlines may measure how successfully they fill their seats and discover opportunities to boost occupancy rates by using this metric. 
Higher occupancy rates can help airlines increase revenue and profitability while lowering operational expenses associated with vacant seats. Pricing strategy, airline schedules, and customer satisfaction are
all factors that might influence occupancy rates. The below Figure 5 shows the average booked seats from the total number of seats for each aircraft. The occupancy rate is calculated by dividing the booked seats
by the total number of seats. Higher occupancy rate means the aircraft seats are more booked and only few seats are left unbooked.

| aircraft_code | booked_seats | num_seats | occupancy_rate |
|---------------|--------------|-----------|----------------|
| 319           | 53.583181    | 116       | 0.461924       |
| 321           | 88.809231    | 170       | 0.522407       |
| 733           | 80.255462    | 130       | 0.617350       |
| 763           | 113.937294   | 222       | 0.513231       |
| 773           | 264.925806   | 402       | 0.659019       |
| CN1           | 6.004431     | 12        | 0.500369       |
| CR2           | 21.482847    | 50        | 0.429657       |
| SU9           | 56.812113    | 97        | 0.585692       |

**Figure 5**

Airlines can assess how much their total yearly turnover could improve by providing all aircraft with a 10% higher occupancy rate to further examine the possible benefits of raising occupancy rates. 
This research can assist airlines in determining the financial impact of boosting occupancy rates by 10%, which results in a gradual increase. Therefore, airlines should focus more on pricing strategies.

| aircraft_code | booked_seats | num_seats | occupancy_rate | Inc_occupancy_rate | Inc_Total_Annual_Turnover |
|---------------|--------------|-----------|----------------|--------------------|---------------------------|
| 319           | 53.58318098720292 | 116   | 0.46192397402761143 | 0.5081163714303726 | 2976779410.0              |
| 321           | 88.80923076923077 | 170   | 0.5224072398190045  | 0.574647963800905  | 1801980510.0              |
| 733           | 80.25546218487395 | 130   | 0.617349709114415   | 0.6790846800258565 | 1569207310.0000002        |
| 763           | 113.93729372937294 | 222  | 0.5132310528350132  | 0.5645541581185146 | 4808404810.0              |
| 773           | 264.9258064516129 | 402   | 0.659019419033863   | 0.7249213609372492 | 3774326050.0              |
| CN1           | 6.004431314623338  | 12    | 0.5003692762186115  | 0.5504062038404727 | 106011180.00000001        |
| CR2           | 21.48284690220174  | 50    | 0.42965693804403476 | 0.4726226318484382 | 2181036550.0              |
| SU9           | 56.81211267605634  | 97    | 0.5856918832583128  | 0.644261071584144  | 5625933169.999999         |

**Figure 6**

## Conclusion 
In summary, analyzing revenue data such as total revenue per year, average revenue per ticket, and average occupancy per aircraft is crucial for airlines aiming to maximize profitability. 
By assessing these indicators, airlines can identify areas for improvement and adapt their pricing and route plans accordingly. A higher occupancy rate stands as a crucial factor in enhancing profitability since
it enables airlines to optimize revenue while minimizing costs related to empty seats. Additionally, airlines should consider revising the pricing strategy for each aircraft. The disparity between lower and higher
prices may deter people from purchasing tickets for those specific aircraft. Establishing a reasonable price aligned with the aircraft's condition and facilities is essential, avoiding extremes of overly cheap or expensive prices.

Moreover, increasing occupancy rates should not compromise consumer satisfaction or safety standards. Airlines must strike a balance between the imperative for profit and the importance of delivering high-quality service while upholding stringent safety regulations. By adopting a data-driven approach to revenue analysis and optimization, airlines can potentially achieve long-term success in a highly competitive industry.



Solution :

Output :
Connection to the database was successful.
List of tables present in the database:
aircrafts_data
airports_data
boarding_passes
bookings
flights
seats
ticket_flights
tickets

aircrafts_data
  aircraft_code                                              model  range
0           773    {"en": "Boeing 777-300", "ru": "Боинг 777-300"}  11100
1           763    {"en": "Boeing 767-300", "ru": "Боинг 767-300"}   7900
2           SU9  {"en": "Sukhoi Superjet-100", "ru": "Сухой Суп...   3000
3           320  {"en": "Airbus A320-200", "ru": "Аэробус A320-...   5700
4           321  {"en": "Airbus A321-200", "ru": "Аэробус A321-...   5600
5           319  {"en": "Airbus A319-100", "ru": "Аэробус A319-...   6700
6           733    {"en": "Boeing 737-300", "ru": "Боинг 737-300"}   4200
7           CN1  {"en": "Cessna 208 Caravan", "ru": "Сессна 208...   1200
8           CR2  {"en": "Bombardier CRJ-200", "ru": "Бомбардье ...   2700

...............................................................................................


airports_data
    airport_code  ...          timezone
0            YKS  ...      Asia/Yakutsk
1            MJZ  ...      Asia/Yakutsk
2            KHV  ...  Asia/Vladivostok
3            PKC  ...    Asia/Kamchatka
4            UUS  ...     Asia/Sakhalin
..           ...  ...               ...
99           MMK  ...     Europe/Moscow
100          ABA  ...  Asia/Krasnoyarsk
101          BAX  ...  Asia/Krasnoyarsk
102          AAQ  ...     Europe/Moscow
103          CNN  ...      Asia/Yakutsk

[104 rows x 5 columns]

...............................................................................................


boarding_passes
            ticket_no  flight_id  boarding_no seat_no
0       0005435212351      30625            1      2D
1       0005435212386      30625            2      3G
2       0005435212381      30625            3      4H
3       0005432211370      30625            4      5D
4       0005435212357      30625            5     11A
...               ...        ...          ...     ...
579681  0005434302871      19945           85     20F
579682  0005432892791      19945           86     21C
579683  0005434302869      19945           87     20E
579684  0005432802476      19945           88     21F
579685  0005432802482      19945           89     21E

[579686 rows x 4 columns]

...............................................................................................


bookings
       book_ref               book_date  total_amount
0        00000F  2017-07-05 03:12:00+03        265700
1        000012  2017-07-14 09:02:00+03         37900
2        000068  2017-08-15 14:27:00+03         18100
3        000181  2017-08-10 13:28:00+03        131800
4        0002D8  2017-08-07 21:40:00+03         23600
...         ...                     ...           ...
262783   FFFEF3  2017-07-17 07:23:00+03         56000
262784   FFFF2C  2017-08-08 05:55:00+03         10800
262785   FFFF43  2017-07-20 20:42:00+03         78500
262786   FFFFA8  2017-08-08 04:45:00+03         28800
262787   FFFFF7  2017-07-01 22:12:00+03         73600

[262788 rows x 3 columns]

...............................................................................................


flights
       flight_id flight_no  ...        actual_departure          actual_arrival
0           1185    PG0134  ...                      \N                      \N
1           3979    PG0052  ...                      \N                      \N
2           4739    PG0561  ...                      \N                      \N
3           5502    PG0529  ...                      \N                      \N
4           6938    PG0461  ...                      \N                      \N
...          ...       ...  ...                     ...                     ...
33116      33117    PG0063  ...  2017-08-02 19:25:00+03  2017-08-02 20:10:00+03
33117      33118    PG0063  ...  2017-07-28 19:30:00+03  2017-07-28 20:15:00+03
33118      33119    PG0063  ...                      \N                      \N
33119      33120    PG0063  ...  2017-08-01 19:26:00+03  2017-08-01 20:12:00+03
33120      33121    PG0063  ...                      \N                      \N

[33121 rows x 10 columns]

...............................................................................................


seats
     aircraft_code seat_no fare_conditions
0              319      2A        Business
1              319      2C        Business
2              319      2D        Business
3              319      2F        Business
4              319      3A        Business
...            ...     ...             ...
1334           773     48H         Economy
1335           773     48K         Economy
1336           773     49A         Economy
1337           773     49C         Economy
1338           773     49D         Economy

[1339 rows x 3 columns]

...............................................................................................


ticket_flights
             ticket_no  flight_id fare_conditions  amount
0        0005432159776      30625        Business   42100
1        0005435212351      30625        Business   42100
2        0005435212386      30625        Business   42100
3        0005435212381      30625        Business   42100
4        0005432211370      30625        Business   42100
...                ...        ...             ...     ...
1045721  0005435097522      32094         Economy    5200
1045722  0005435097521      32094         Economy    5200
1045723  0005435104384      32094         Economy    5200
1045724  0005435104352      32094         Economy    5200
1045725  0005435104389      32094         Economy    5200

[1045726 rows x 4 columns]

...............................................................................................


tickets
            ticket_no book_ref passenger_id
0       0005432000987   06B046  8149 604011
1       0005432000988   06B046  8499 420203
2       0005432000989   E170C3  1011 752484
3       0005432000990   E170C3  4849 400049
4       0005432000991   F313DD  6615 976589
...               ...      ...          ...
366728  0005435999869   D730BA  0474 690760
366729  0005435999870   D730BA  6535 751108
366730  0005435999871   A1AD46  1596 156448
366731  0005435999872   7B6A53  9374 822707
366732  0005435999873   7B6A53  7380 075822

[366733 rows x 3 columns]

 table: aircrafts_data
('aircraft_code', 'character(3)')
('model', 'jsonb')
('range', 'integer')

 table: airports_data
('airport_code', 'character(3)')
('airport_name', 'jsonb')
('city', 'jsonb')
('coordinates', 'point')
('timezone', 'text')

 table: boarding_passes
('ticket_no', 'character(13)')
('flight_id', 'integer')
('boarding_no', 'integer')
('seat_no', 'character varying(4)')

 table: bookings
('book_ref', 'character(6)')
('book_date', 'timestamp with time zone')
('total_amount', 'numeric(10,2)')

 table: flights
('flight_id', 'integer')
('flight_no', 'character(6)')
('scheduled_departure', 'timestamp with time zone')
('scheduled_arrival', 'timestamp with time zone')
('departure_airport', 'character(3)')
('arrival_airport', 'character(3)')
('status', 'character varying(20)')
('aircraft_code', 'character(3)')
('actual_departure', 'timestamp with time zone')
('actual_arrival', 'timestamp with time zone')

 table: seats
('aircraft_code', 'character(3)')
('seat_no', 'character varying(4)')
('fare_conditions', 'character varying(10)')

 table: ticket_flights
('ticket_no', 'character(13)')
('flight_id', 'integer')
('fare_conditions', 'character varying(10)')
('amount', 'numeric(10,2)')

 table: tickets
('ticket_no', 'character(13)')
('book_ref', 'character(6)')
('passenger_id', 'character varying(20)')

Table: aircrafts_data
aircraft_code    0
model            0
range            0
dtype: int64

Table: airports_data
airport_code    0
airport_name    0
city            0
coordinates     0
timezone        0
dtype: int64

Table: boarding_passes
ticket_no      0
flight_id      0
boarding_no    0
seat_no        0
dtype: int64

Table: bookings
book_ref        0
book_date       0
total_amount    0
dtype: int64

Table: flights
flight_id              0
flight_no              0
scheduled_departure    0
scheduled_arrival      0
departure_airport      0
arrival_airport        0
status                 0
aircraft_code          0
actual_departure       0
actual_arrival         0
dtype: int64

Table: seats
aircraft_code      0
seat_no            0
fare_conditions    0
dtype: int64

Table: ticket_flights
ticket_no          0
flight_id          0
fare_conditions    0
amount             0
dtype: int64

Table: tickets
ticket_no       0
book_ref        0
passenger_id    0
dtype: int64

Basic Analysis

How many Planes have more than 100 seats?

  aircraft_code  num_seats
0           319        116
1           320        140
2           321        170
3           733        130
4           763        222
5           773        402
6           CN1         12
7           CR2         50
8           SU9         97

How the no of tickets booked with the time

calculate the average charges for each aircraft with different fare conditions

   fare_conditions aircraft_code    avg(amount)
0         Business           319  113550.557703
1          Economy           319   38311.402347
2         Business           321   34435.662664
3          Economy           321   11534.974764
4         Business           733   41865.626175
5          Economy           733   13985.152000
6         Business           763   82839.842866
7          Economy           763   27594.721829
8         Business           773   57779.909435
9          Comfort           773   32740.552889
10         Economy           773   19265.225693
11         Economy           CN1    6568.552345
12         Economy           CR2   13207.661102
13        Business           SU9   33487.849829
14         Economy           SU9   11220.183400

Analyzing occupancy rate

For each aircraft, calculate total revenue per year and the average revenue per ticket

  aircraft_code  tickets_count  total_revenue  avg_revenue_per_ticket
0           319          52853     2706163100                   51201
1           321         107129     1638164100                   15291
2           733          86102     1426552100                   16568
3           763         124774     4371277100                   35033
4           773         144376     3431205500                   23765
5           CN1          14672       96373800                    6568
6           CR2         150122     1982760500                   13207
7           SU9         365698     5114484700                   13985

Calculate the average occupancy per aircraft.

  aircraft_code  booked_seats  num_seats  occupancy_rate
0           319     53.583181        116        0.461924
1           321     88.809231        170        0.522407
2           733     80.255462        130        0.617350
3           763    113.937294        222        0.513231
4           773    264.925806        402        0.659019
5           CN1      6.004431         12        0.500369
6           CR2     21.482847         50        0.429657
7           SU9     56.812113         97        0.585692

calculate how much the total annual turnover could increase by giving all aircraft a 10% higher occupancy rate

  aircraft_code  total_revenue
0           319     2706163100
1           321     1638164100
2           733     1426552100
3           763     4371277100
4           773     3431205500
5           CN1       96373800
6           CR2     1982760500
7           SU9     5114484700

























                                                                                        
