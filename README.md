# Lab 12: REST Weather Map
## Objectives
-Access information via REST
-Work with JSON formatted data
-Display data with SVG file and jQuery
-Use Google to find answers
## Assignment
In this assignment create a web page showing the weather across the USA.

Each state will be color-coded according to its current temperature.

### Part 0 - National Weather Service API
-Browse the documentation at: https://www.weather.gov/documentation/services-web-api
-Get weather json data from the command line: `curl 'https://api.weather.gov/gridpoints/BOU/53,74/forecast'`
--You should get back a json document with forecast information.
### Part 1 - Static HTML
1) Download a map of the United States in SVG format.
2) Create a new HTML file named weather.html.
3) In your HTML file, add the following code to create a web page:
```
 <html>
 <head>
   <title>Weather Map Lab by Your last name</title>
 </head>
 <body>
```
4) On the next line in the file, insert the downloaded SVG map. Copy-paste isn’t very effective here, but you can do this in vim with the following:

 `:r Blank_US_Map.svg`
5) Close the HTML page with:
```
 </body>
 </html>
```
6) Read the docs for python's simple http server. Run a python http server on your machine (Use the CGI version)

`python3 -m http.server 8000 --cgi --bind 127.0.0.1`
7) Test in your browser: `http://127.0.0.1:8000/weather.html` – the map of the US should show up.
8) Now convert this to a Python CGI script that prints this HTML code.
- Copy your html file to a new file named `weather_script.py`
- Be sure to put this in the cgi-bin directory.
- Check permissions! `chmod +x cgi-bin/weather_script.py`
- The first line in weather_script.py should be the shebang line: `#!/usr/bin/python3`. You may need to change this based on your python3 install location.
- Then add this:
```
         print("Content-type: text/html")
         print() # This extra newline is important!
```
- Then convert each html line into a python statement printing that line: `print('<html>') print('<body>') print('<svg xmlns=...') ... print('</html>')` You can create multi-line strings with triple quotes, such as:

`highlight print(''' <html> <body> ... etc. </html>''')`

Test in your browser: `http://127.0.0.1:8000/cgi-bin/weather_script.py` You should see the same map as before. *Hint*: If you get stuck, look for errors in two places: the server output in your terminal, and the developer console in your browser.

### Part 2 - Dynamic weather data
Now we want to call the NWS URL to get the weather. To start, do this with Boulder, CO. To do this in python, if you Google how to read the JSON from a URL you can find a great answer at StackOverflow

Remember, if you use this source then attribute it in your code!

Our next step is to test manually changing the colors of the states. Add the following code to the header section of your script:

print('''
<script>
window.onload = function() {
''')
print("document.getElementById('CO').setAttribute('fill', '#CFB87C');")

print('''
};
</script>
''')
This sets the event handler for window.onload Note: We are dividing up the printing into separate print statements because we will need to add python code in the middle.

Reload the page, and you should see Colorado filled in gold!

Now we certainly don’t want to manually type in all the states.

This file has average latitude and longitude for each state.
This one has state names mapped to abbreviations.
Combine these to get a dictionary mapping each state abbreviation (CO) to coordinates.
Instead of color-coding Colorado only, create a loop through the dictionary and color-code every state.

Hint: As of python 3.6, you can do string interpolation like so:

for statename in states:
  print(f"blahblahblah {statename} blahblahblah")
See PEP 498.

Time to call the weather API for each state’s capital so we can color-code each state based on the temperature!

Very important: We don’t want to hit the API a billion times while we are testing (I started to get denied service if I did it too much in an hour, and it takes a while to call it for all 50 states). So comment out the last 45 states (vim – go to the line to start and do :.,+44s/^/#/

Determine which color should be used for the state. Based on the temperature, use the following color

Temperature	Color
[default]	Gray
\< 10	Blue
10..30	Cyan
30..50	Green
50..80	Orange
> 80	Red
Credit
To receive credit for this assignment:

Submit your .py and .html files as a zip Firstname_Lastname.zip to Moodle.

Make sure only 5 states show up to make grading easier on the TAs.

Optional
Once everything is working, uncomment the rest of the states and run it again to see the full color map. We can do this now without worrying about API request limits.
