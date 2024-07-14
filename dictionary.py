# dictionary is like a object

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "Devember"
}

print(monthConversions)
print(monthConversions["Dec"])
print(monthConversions.get("May" ))
print(monthConversions.get("Luv", "Not a valid key" ))

