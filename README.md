# LAB_DICTIONARY


## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
You can follow the table below:

| Name     | Number     |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |


- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".




# Bonus (use a new file)

### Exercise: Weather Data Aggregation

**Objective:** Write a Python program that aggregates weather data for different cities and provides weather data based on user queries.

#### Requirements:

1. **Input Weather Data:** Allow the user to input weather data for different cities. Each entry should include the city name, date, temperature, humidity, and weather condition (e.g., sunny, rainy).
2. **Store Data in a Dictionary:** Use a nested dictionary to store the weather data. The outer dictionary's keys will be the city names, and the values will be another dictionary containing date and weather details.
3. **Query by City:** Allow the user to query the weather data by city name, displaying all the recorded weather data for that city.

#### Guidelines:

- Use nested dictionaries to store the weather data efficiently.
- Implement separate functions for inputting data, querying by city.
- Validate user inputs to ensure correctness.

#### Challenge:

- Extend the program to allow the user to update or delete weather data for a specific city and date.
