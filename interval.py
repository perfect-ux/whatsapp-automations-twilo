from apscheduler.schedulers.blocking import BlockingScheduler
from autowhatsapp import send_love

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_love(), 'interval', hours=10)

sched.start()