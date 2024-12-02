import numpy as np

data=np.array([
    [1500, 2000, 1800, 1200, 900],
    [1600, 2100, 1900, 1300, 950],
    [1700, 2200, 2000, 1400, 1000],
    [1650, 2150, 1950, 1350, 980],
    [1750, 2250, 2050, 1450, 1020],
    [1800, 2300, 2100, 1500, 1050], 
    [1900, 2400, 2200, 1600, 1100],
    
])

case_register_each_country=[sum(row[col] for row in data) for col in range(len(data[0]))]
print(case_register_each_country)

highest_case_country=max(case_register_each_country)
print(highest_case_country)
# np.argmax

case_register_each_day=[sum(row) for row in data]
print(case_register_each_day)

average_case_register_per_day_country=[num/7 for num in case_register_each_day]
print(average_case_register_per_day_country)


# 2.b.
max_case_day=np.argmax(case_register_each_day)
print(f"Day {max_case_day}")

# 3.a.
percentage_inc_dec_country=np.diff(case_register_each_country) / case_register_each_country[:-1] * 100
print(percentage_inc_dec_country)


#3.b. 
max_percent_inc=max(percentage_inc_dec_country)
print(max_percent_inc)