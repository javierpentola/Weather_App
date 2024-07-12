# Weather App

### **Project Documentation: Weather Application**

---

#### **Project Overview**

**Project Name:** Weather Application

**Technologies Used:**
- **HTML:** For creating the structure and content of the web pages.
- **CSS:** For styling the web pages to make them visually appealing.
- **JavaScript:** For adding interactivity to the frontend.
- **Python:** The main programming language used for backend development.
- **Flask:** A lightweight web framework for Python that we used to create the web application, define routes, handle requests, and connect to the database.
- **SQLite:** A lightweight database used to store the weather data.

**Description:** This project is a web application designed to display the weather information for 20 capitals around the world, distributed across different continents.

---

### **Technologies Usage**

1. **HTML:**
   - **Usage:** HTML was used to create the structure of the web pages. The main view displays weather information for different capitals.
   - **Files:** `index.html` for the main view.

2. **CSS:**
   - **Usage:** CSS was used for styling the HTML elements to make the application visually appealing. The XP.css library was used to give the application a classic Windows XP look and feel.
   - **Files:** CSS styles are embedded directly within `index.html`.

3. **JavaScript:**
   - **Usage:** JavaScript was used to add interactivity to the web pages, such as fetching weather data and dynamically updating the UI.
   - **Files:** JavaScript code is embedded directly within `index.html`.

4. **Python:**
   - **Usage:** Python was the main programming language for backend development. It was used to write the application logic, handle requests, and process data.
   - **Files:** `app.py` contains the main application logic.

5. **Flask:**
   - **Usage:** Flask was used as the web framework to build the web application. It helped in defining routes, handling HTTP requests, rendering templates, and connecting to the database.
   - **Key Components:**
     - **Routes:** Defined in `app.py` to map URLs to functions.
     - **Templates:** HTML files rendered by Flask using the `render_template` function.
     - **Database:** Connected using SQLite for data storage.

6. **SQLite:**
   - **Usage:** SQLite was used as the database to store weather data. It is a lightweight, file-based database that is ideal for small to medium-sized applications.
   - **Files:** `weather.db` (the database file).

---

### **Setup and Usage Instructions**

To use the project after downloading the code, follow these steps:

1. **Clone the Repository:**
   - Use `git clone` to clone the repository to your local machine.

2. **Navigate to the Project Directory:**
   - Change your working directory to the project folder.
   ```bash
   cd weather_app
   ```

3. **Create and Activate a Virtual Environment:**
   - Create a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

4. **Install Dependencies:**
   - Install the required Python packages using `pip`.
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the Database:**
   - Initialize the SQLite database by running the `app.py` script once.
   ```bash
   python app.py
   ```

6. **Run the Application:**
   - Start the Flask development server.
   ```bash
   flask run
   ```

7. **Access the Application:**
   - Open a web browser and go to `http://127.0.0.1:5000`.

8. **Viewing the Database:**
   - The database file (`weather.db`) is located in the project directory. You can use tools like DB Browser for SQLite or the SQLite command line to view and manage the database contents.
