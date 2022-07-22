# if __ name _ _ == '_ _ main _ _ '
# this is a stand-alone program
# this module can be imported and used by other modules

# time module
# epoch is a date and time from which a computer measures system time
# will use epoch as a reference point


# import time
# convert a time express in seconds since epoch to readable string
# epoch when your computer thinks time began (reference point)

# print(time.ctime(0))

# time method
# return current seconds since epoch

# print(time.time())

# going to call an argument
# to get the current date and time

# print(time.ctime(time.time()))

# local time will create a time object
# time_object = time.localtime()
# print(time_object)
# to turn the time format into a readable we would we use a string
# local_time = time.strftime("%B %d %Y %H: %M", time_object)
# print(local_time)


# time_string = "20 April, 2022"
# time_object = time.strptime(time_string, "%d %B, %Y ")
# print(time_object)


# ( year, month, day, hours, minutes, secs, # day of the week, #day of the year, dst)

# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# ( year, month, day, hours, minutes, secs, # day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

# -------------------------------------------------------------------------------------------------------------------
# 64 threading
# thread = a flow of execution . like a separate order of instructions.
#  however each thread takes a turn running to achieve concurrency
# allows only one thread  to hold the control of python interpreter

import threading
import time


# late for school what are some to the task you do
# amount of time to complete the tasks
def eat_breakfast():
    # how long is it going to take to finish. this is 3 seconds
    time.sleep(4)
    print("You eat breakfast")


# each of these tasks are io bound, they are going to wait for external events
def make_smoothie():
    time.sleep(3)
    print("You made smoothie")


def review_work():
    time.sleep(3)
    print("You reviewed work")


# eat_breakfast()
# make_smoothie()
# review_work()

x = threading.Thread(target=eat_breakfast, args=())
x.start()

s = threading.Thread(target=make_smoothie, args=())
s.start()

y = threading.Thread(target=review_work, args=())
y.start()
