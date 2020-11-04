#schedule a job task
#author:Sri venkatesh
import schedule #importing library
import random
import time
#to define a function job
def job():
    print("the job will be done in few minutes")
#to schedule a job 
schedule.every(1).hours
se1=random.int(0,1)
se2=random.int(0,1)
se3=random.int(0,1)
se4=random.int(0,1)
se5=random.int(0,1)
#to check the availability of the service engineer
if(se1==0):
    job()
elif(se2==0):
    job()
elif(se3==0):
    job()
elif(se4==0):
    job()
elif(se5==0):
    job()
else:
    print("all service engineer are busy")

