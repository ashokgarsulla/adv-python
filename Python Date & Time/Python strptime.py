# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  Python strptime()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# In this article, you will learn to create a datetime object from a string (with the help of examples).

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  string to datetime object
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

from datetime import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  string to datetime object with full time and date 
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

from datetime import datetime

dt_string = "12/11/2018 09:15:32"


print("-" *30,'LINE 34',"-" *30)
# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)