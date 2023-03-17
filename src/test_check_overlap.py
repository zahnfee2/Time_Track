from Function import check_overlap
# 2023-03-09 09:00:00 - 2023-03-09 09:33

# TRUE
timerow = ['2023-03-09 08:00:00', '2023-03-09 09:01:00', '0 days 00:33:00', '##']
print(str(check_overlap(timerow)))

# TRUE
timerow = ['2023-03-09 09:32:00', '2023-03-09 10:03:00', '0 days 00:33:00', '##']
print(str(check_overlap(timerow)))

# FALSE
timerow = ['2023-03-09 10:00:00', '2023-03-09 11:03:00', '0 days 00:33:00', '##']
print(str(check_overlap(timerow)))

# FALSE
timerow = ['2023-03-08 08:00:00', '2023-03-08 09:01:00', '0 days 00:33:00', '##']
print(str(check_overlap(timerow)))