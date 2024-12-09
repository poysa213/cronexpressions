from cronexpressions import CronExpression, CronBuilder

# Test predefined constants
print(CronExpression.EVERY_MINUTE)  # Output: '* * * * *'
print(CronExpression.EVERY_HOUR)  # Output: '* * * * *'
# Test custom builder
cron = CronBuilder().set_second("15").set_minute("30").set_hour("10").build()
print(cron)  # Output: '15 30 10 * * *'

# Initialize a new CronBuilder instance
builder = CronBuilder()

# Build a cron expression for every 5 minutes
cron = builder.every('minute', 5).build()
print(cron)  # Output: '*/5 * * * *'

# Reset the builder and build a cron expression for every 2 hours
builder = CronBuilder()
cron = builder.every('hour', 2).build()
print(cron)  # Output: '0 */2 * * *'

# Reset the builder and build a cron expression for a range of hours (9 AM to 5 PM)
builder = CronBuilder()
cron = builder.set_range('hour', 9, 17).build()
print(cron)  # Output: '0 9-17 * * *'

# Reset the builder and build a cron expression for a specific weekday (first Monday of the month)
builder = CronBuilder()
cron = builder.set_specific('weekday', '1#1').build()
print(cron)  # Output: '0 0 * * 1#1'

# Reset the builder and build a cron expression for every second and every day
builder = CronBuilder()
cron = builder.every_second().every_day().build()
print(cron)  # Output: '* * * * * *'
