import holidays
from datetime import date

india_holidays = holidays.country_holidays('IN', years=[2026])
print(date(2026,11,8) in india_holidays)        # True (Republic Day)
print(india_holidays.get('2026-11-8'))         # "Republic Day"