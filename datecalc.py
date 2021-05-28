# import time

# print(time.gmtime(0))
# time_here = time.localtime()
# print(time_here)
# print("Year: ",time_here[0],time_here.tm_year)
# print("Month: ",time_here[1],time_here.tm_mon)
# print("Day: ",time_here[2],time_here.tm_mday)


import time
from time import perf_counter as my_timer       #  'import time, import monotonic' could also be used
import random                                # perf_counter is best
                                            # import 'process_time' gives the time used by the CPU for the process
input("Press enter to start: ")
wait_time = random.randint(1,6)
time.sleep(wait_time)   # this makes the pc sleep for some random seconds between 16 seconds.
start_timer = my_timer()
input("Press enter to stop: ")

end_timer = my_timer()
print("Started at "+ time.strftime("%X", time.localtime(start_timer)))
print("Ended at "+ time.strftime("%X", time.localtime(end_timer)))

print("Your reaction time was {} seconds.".format(end_timer-start_timer))