from speedrun.timer_calc import format_time as time
from speedrun.records import check_personal_best as checker

current_time = 55.983 # Current time, preety self explanatory
old_pb = 57.5 # Your latest pb ig?

formatted = time(current_time)
result = checker(current_time, old_pb)

print(result)
