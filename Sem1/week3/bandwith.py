
# Define the variables
max_bandwidth = 1000 * 1000000
concurrent_users = 200
app_a = 200000
app_b = 100000
new_app = 350000

#Calculations for the bandwith 
network_capacity = max_bandwidth * concurrent_users
current_usage = app_a + app_b
current_availability = network_capacity - current_usage
bandwidth_available = current_availability - new_app


# Convert the bandwidth available to Mbps and print the result
bandwidth_available_mbps = bandwidth_available / 1000000
print("Bandwidth available if the new application is installed:", bandwidth_available_mbps, "Mbps")
