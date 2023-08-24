# Portfolio
## AppShare
#### Description:
I have used Django as a framework (which I am still continually learning and developing new skills in) and downloaded a template from Bootstrap (modified it for my own needs). 
I decided to use Django because I aspire to become a Python backend developer who utilizes this framework.

The user's path:
The web application serves multiple purposes for the user to exploit. The user can either log in with their username or password or sign up by entering their new username, email, and password twice. 
Afterward, they are redirected to a form to select their country, and upon submission, the data is saved to the database. All countries of users are shown on the world map with markers and usernames. 
A CSV file is used with all countries, their longitude, and latitude. Additionally, users can choose an exact city by clicking on the field in the navbar. By typing in the city, the application uses an API to check if the city exists. 
Once the user provides the city, the page renders with all usernames and their current weather, listed from highest to lowest. The app is designed for my friends and relatives who live across the whole globe, enabling them to share their weather and location.

Backend:
Using Django, I created models for Users, Maps, and Weather apps, which saved the information that users either entered or typed. Django's methods and documentation came in handy, providing features such as form validation, built-in authentication, and error messages.
One of the most interesting aspects was using an API. I had to use the link: https://api.openweathermap.org to retrieve live data and render the page with weather information for each user and their city.

Frontend:
I coded the CSS and HTML myself for every page of my website, and I integrated a Bootstrap navbar and some JS to give it a presentable view.
In the future, I intend to revamp the frontend with more appealing visuals, including interactive elements and animations. Additionally, I will work on improving the overall layout and user interface to make it more engaging and user-friendly.


#### Known Issues and Future Improvements

Code:
The main issue that I noticed on my website is related to the weather of all users' page. I need to find a way to optimize this process because as the number of users increases, the page loads slower.

To address this, I plan to implement data pagination and lazy loading for weather data. By fetching weather information in smaller chunks and loading it on-demand, I can significantly improve the page's performance.

Design:
I aim to add more clarity to my homepage and create a better title layout, positioned to the right of the picture. On the page where the map is located, the '+' and '-' signs, along with the line below the map, override some content of the page. I plan on fixing that.


In conclusion, AppShare is an ongoing project where I continuously seek to improve both its functionality and aesthetics. With a passion for learning and a dedication to delivering an exceptional user experience, I look forward to refining this web application and expanding its capabilities in the future.

Link for the app: https://appshare.pythonanywhere.com
