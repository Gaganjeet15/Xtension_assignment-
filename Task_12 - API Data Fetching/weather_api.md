# Write a Python script that fetches data from an open API (e.g., weather, cryptocurrency prices) and displays it in a formatted manner.

  **Weather api**

Explanation:
1. The script uses OpenWeatherMap api to fetch data.
   * Take input from user for city.
   * In the base url of Openwather i have used 'f' string, using this i attaced the city name and api key.
   * If the request is successful (status code 200), the script parses the JSON response.
2. Then it extracts the details such as temperature, description, etc.
3. After extraction using 'f' string, formatted the data.
4. Else if the status code is not 200, then prints "Error fetching data" as status error.
