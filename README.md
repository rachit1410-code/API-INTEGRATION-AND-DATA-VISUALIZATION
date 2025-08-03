# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY:CODTECHIT SOLUTIONS

NAME: RACHIT DUBEY

INTERN ID: ?

DOMAIN:PYTHON DEVELOPER INTERN

DURATION: 2 MONTH

MENTOR: NEELA SANTOSH


                                                                                #Description#


#Weather Report Visualizer in Python
This project is a simple, interactive Python script that allows users to retrieve and visualize real-time weather data for any city using the OpenWeatherMap API. Built as part of an internship exercise, this tool provides not just raw data but also a clean, visual summary of key weather parameters like temperature, humidity, pressure, etc., making it useful for both learners and casual users.


#Features
✅ Takes user input for city name

✅ Fetches real-time weather data from OpenWeatherMap API

✅ Handles errors like wrong city names or invalid API keys

✅ Plots a clean bar chart showing multiple weather parameters

✅ Modular code structure with reusable functions

✅ Beginner-friendly and works directly in Visual Studio Code or terminal


#🔧Tech Stack
Python 3.8+
Requests – for API calls
Matplotlib – for data visualization
OpenWeatherMap API – as the data source


#🧑‍💻How It Works
1. The script asks the user to enter a city name via terminal.
2. It sends a request to the OpenWeatherMap API using the entered city.
3. If the city is valid and the API key is correct, it returns:
Temperature (in Celsius)
Feels like temperature
Humidity
Pressure
4. These values are then plotted as a bar graph, with customized colors and labels.
5. If any error occurs (like wrong city or expired API key), the program gives a clean message with an HTTP error code like 401 or 404.


#📈Sample Output
Once you enter a city like "Mumbai", the program will display:
<img width="700" height="449" alt="Image" src="https://github.com/user-attachments/assets/e5c70230-c857-4182-be2f-86929292e11d" />

<img width="708" height="307" alt="Image" src="https://github.com/user-attachments/assets/4b782045-0b01-4b85-92b0-6faedcbf30bf" />

Weather Report for Mumbai:
Temperature: 30°C
Feels Like: 32°C
Humidity: 70%
Pressure: 1005 hPa

And a bar graph will open showing these values visually.

#⚙How to Run This Project
1. Clone this repository or download the Python script.
2. Make sure you have Python installed.
3. Install required packages:
   
pip install requests matplotlib

4. Open the file in VS Code or terminal.
5. Replace "YOUR_API_KEY" in the script with your actual API key from OpenWeatherMap.
6. Run the script:


#🚧Troubleshooting
Error 401 → Check your API key; it’s either invalid or not added.
Error 404 → City not found. Make sure spelling is correct.
No graph appears? → Ensure matplotlib.pyplot.show() is present and you're not running in a headless mode (like some online editors).
