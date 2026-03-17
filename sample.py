from datetime import datetime

# Get the current date and time
now = datetime.now()

# Print it in a default format
print("Default Format:", now)

# Print it in a more readable format (Day, Month Date, Year, Time)
readable_format = now.strftime("%A, %B %d, %Y - %I:%M:%S %p")
print("Readable Format:", readable_format)