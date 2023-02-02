
def convert_to_time(seconds):
    # Calculate the number of hours by dividing the total seconds by 3600 (the number of seconds in an hour)
    hours = seconds // 3600
    # Calculate the number of minutes by dividing the remaining seconds (after hours) by 60
    minutes = (seconds % 3600) // 60
    # Calculate the remaining seconds after hours and minutes
    remaining_seconds = seconds % 60
    # Return the hours, minutes and seconds
    return hours, minutes, remaining_seconds

# Prompt the user to enter the number of seconds
seconds = int(input("Enter the number of seconds: "))

# Call the convert_to_time function and store the results in hours, minutes, and seconds variables
hours, minutes, seconds = convert_to_time(seconds)

# Print the results
print("Input:   Hours:   Minutes:   Seconds:")
print("{0:<8} {1:<8} {2:<8} {3:<8}".format(seconds, hours, minutes, seconds))
