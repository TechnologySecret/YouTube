import time  #convert a time expressed in seconds since epoch to a readable string.
            # Epoch = when you computer thinks time began (reference point)

# NOte: For More Information pls read official website of (https//python//library/timemodule)


# print(time.ctime(0))   #return current seconds since epoch
# print(time.ctime(time.time()))



# time_object = time.localtime()  #local time
# time_object = time.gmtime()         #UTC time
# local_time = time.strftime("%B %d %Y  %H:%M:%S", time_object)
# print(local_time)


# Explanation:
# %d: Day of the month (01-31).
# %b: Abbreviated month name (e.g., "Dec").
# %Y: Year (e.g., 2024).

# time_string = "1 Dec, 2024"
# time_object = time.strptime(time_string, '%d %b,  %Y')
# print("\n",time_object)

#(year , months, day , hours, minutes, secs, #day of the week, $day of the year, dst)
time_tuple = (2020, 4, 20, 4,20, 0,0,0,0)
time_string = time.asctime(time_tuple)
print(time_string)


#(year , months, day , hours, minutes, secs, #day of the week, $day of the year, dst)
time_tuple = (2020, 4, 20, 4,20, 0,0,0,0)
time_string = time.mktime(time_tuple)
print(time_string)





