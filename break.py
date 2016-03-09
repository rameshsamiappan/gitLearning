'Udacity Pyton Training
'Started on 8-Mar-2016
import time
import webbrowser

total_breaks = 3
break_count = 0
wait_time_s = 5 'seconds

print("Started on:" + time.ctime())
while(break_count < total_breaks):
    time.sleep(wait_time_ms)
    webbrowser.open("www.google.com")
    break_count=break_count+1

print("Completed on" + time.ctime())
