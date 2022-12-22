# Store the ratings in a dictionary with the rating as the key and the count as the value
ratings = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# Prompt the user for a rating and read their input
rating = int(input("Please rate the restaurant on a scale of 1 to 5 (1 is very poor, 5 is very good): "))

# Loop until the user enters -1
while rating != -1:
  # Increment the count of the rating
  ratings[rating] += 1

  # Prompt the user for another rating
  rating = int(input("Please rate the restaurant on a scale of 1 to 5 (1 is very poor, 5 is very good): "))

# Compute the average rating
total = 0
count = 0
for i in ratings:
  total += i * ratings[i]
  count += ratings[i]
average = total / count

# Output the results
print()
print("Rating\tCount")
for i in ratings:
  print(i, "\t", ratings[i])
print("Average rating:", average)
