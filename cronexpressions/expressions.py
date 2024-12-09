class CronExpression:
    # Every second, minute, and hour
    EVERY_SECOND = "* * * * * *"
    EVERY_30_SECONDS = "*/30 * * * * *"
    EVERY_MINUTE = "* * * * *"
    EVERY_5_MINUTES = "*/5 * * * *"
    EVERY_10_MINUTES = "*/10 * * * *"
    EVERY_15_MINUTES = "*/15 * * * *"
    EVERY_30_MINUTES = "*/30 * * * *"
    
    # Every hour or multiple hours
    EVERY_HOUR = "0 * * * *"
    EVERY_2_HOURS = "0 */2 * * *"
    EVERY_3_HOURS = "0 */3 * * *"
    EVERY_4_HOURS = "0 */4 * * *"
    EVERY_6_HOURS = "0 */6 * * *"
    EVERY_12_HOURS = "0 */12 * * *"
    
    # Daily expressions
    EVERY_DAY_AT_MIDNIGHT = "0 0 * * *"
    EVERY_DAY_AT_NOON = "0 12 * * *"
    EVERY_DAY_AT_3AM = "0 3 * * *"
    EVERY_DAY_AT_6PM = "0 18 * * *"
    EVERY_DAY_AT_9PM = "0 21 * * *"
    
    # Weekly and weekend
    EVERY_WEEK = "0 0 * * 0"
    EVERY_SUNDAY = "0 0 * * 0"
    EVERY_MONDAY = "0 0 * * 1"
    EVERY_TUESDAY = "0 0 * * 2"
    EVERY_WEDNESDAY = "0 0 * * 3"
    EVERY_THURSDAY = "0 0 * * 4"
    EVERY_FRIDAY = "0 0 * * 5"
    EVERY_SATURDAY = "0 0 * * 6"
    EVERY_WEEKDAY = "0 0 * * 1-5"
    EVERY_WEEKEND = "0 0 * * 6,0"
    
    # Monthly
    EVERY_1ST_OF_MONTH = "0 0 1 * *"
    EVERY_15TH_OF_MONTH = "0 0 15 * *"
    EVERY_LAST_DAY_OF_MONTH = "0 0 28-31 * *"
    
    # Yearly
    EVERY_YEAR = "0 0 1 1 *"
    EVERY_1ST_DAY_OF_YEAR = "0 0 1 1 *"
    
    # Specific day of the month (e.g., the first Monday of every month)
    FIRST_MONDAY_OF_MONTH = "0 0 * * 1#1"
    SECOND_MONDAY_OF_MONTH = "0 0 * * 1#2"
    THIRD_MONDAY_OF_MONTH = "0 0 * * 1#3"
    FOURTH_MONDAY_OF_MONTH = "0 0 * * 1#4"
    
    # Random intervals
    EVERY_5_DAYS = "0 0 */5 * *"
    EVERY_10_DAYS = "0 0 */10 * *"
    EVERY_30_DAYS = "0 0 1/30 * *"
    
    # Complex intervals (using ranges, specific minutes, and days)
    EVERY_WEEKDAY_AT_9AM = "0 9 * * 1-5"
    EVERY_FIRST_MONDAY_AT_9AM = "0 9 * * 1#1"
    EVERY_LAST_DAY_OF_MONTH_AT_NOON = "0 12 28-31 * *"
    
    # Work-related schedules
    EVERY_9AM_TO_5PM_WEEKDAY = "0 9-17 * * 1-5"
    EVERY_8AM_TO_6PM = "0 8-18 * * *"
    EVERY_12AM_TO_12PM = "0 0-12 * * *"
    
    # Every specific minute of every hour
    EVERY_MINUTE_1 = "1 * * * *"
    EVERY_MINUTE_2 = "2 * * * *"
    EVERY_MINUTE_5 = "5 * * * *"
    EVERY_MINUTE_10 = "10 * * * *"
    EVERY_MINUTE_20 = "20 * * * *"
    EVERY_MINUTE_30 = "30 * * * *"
    EVERY_MINUTE_45 = "45 * * * *"
    
    # Specific times and ranges
    EVERY_HOUR_AT_15 = "15 * * * *"
    EVERY_HOUR_AT_30 = "30 * * * *"
    EVERY_HOUR_AT_45 = "45 * * * *"
    
    # Edge Cases
    EVERY_5_SECOND = "*/5 * * * * *"
    EVERY_60_SECOND = "*/60 * * * * *"  # Equivalent to every minute
    
    # More advanced interval patterns
    EVERY_DAY_AT_8AM_AND_6PM = "0 8,18 * * *"
    EVERY_SUNDAY_AT_9AM_AND_6PM = "0 9,18 * * 0"
