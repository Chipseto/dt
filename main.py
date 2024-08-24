from datetime import datetime

now = datetime.now()
formatted_now = now.strftime("%H:%M:%S")
gleb = datetime(year=2012, month=5, day=16)
age_gleb = now - gleb

mother = datetime(year=1985, month=7, day=8)
age_mother = now - mother

print("Now is", formatted_now)
print("My mother is", age_mother.days, "days old")
print("I am", age_gleb.days, "days old")
