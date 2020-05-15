from crontab import CronTab


cron = CronTab(user=True)

for job in cron:
    # cron.remove(job)
    print(job)


# cron.remove_all()




# job = cron.new(command='python test.py')
# job.minute.every(1)
# job.enable(False)

# cron.write()
