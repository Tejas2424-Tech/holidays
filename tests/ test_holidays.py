from datetime import date
import holidays

# Create a holiday calendar for the USA in a specific year
us_holidays = holidays.US(years=2025)

# Check if a date is a holiday
print(date(2025, 1, 1) in us_holidays)  # True (New Year's Day)
print(date(2025, 2, 1) in us_holidays)  # False (normal day)

# Get the holiday name
print(us_holidays.get('2025-01-01'))    # "New Year's Day"