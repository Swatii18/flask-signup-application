# Flask Signup Application

## Project Overview

This project is a Flask-based Signup Application consisting of two separate Flask services: a frontend and a backend.

The frontend provides a signup form where users can enter their username and password. The submitted data is sent to the backend through an HTTP POST request.

The backend processes the submitted data, stores it in MongoDB, and maintains a local JSON file for API data retrieval.

The application also provides success and error messages based on the submission result.

## Project Architecture

The application follows a two-tier Flask architecture.

1. **Frontend (Port 8000)**
   - Built using Flask and HTML templates.
   - Displays the signup form.
   - Sends submitted form data to the backend using HTTP POST requests.
   - Displays success and error messages.

2. **Backend (Port 9000)**
   - Built using Flask.
   - Receives submitted data from the frontend.
   - Stores submitted records in MongoDB.
   - Maintains records in a local `data.json` file.
   - Provides a `/api` endpoint to retrieve records in JSON format.

3. **Database**
   - MongoDB Atlas is used for persistent data storage.

   User
  |
  v
Frontend (Flask - 8000)
  |
  | POST /submit
  v
Backend (Flask - 9000)
  |
  +------> MongoDB Atlas
  |
  +------> data.json
               |
               v
           GET /api

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- MongoDB Atlas
- PyMongo
- Requests
- JSON
- Git and GitHub

## Prerequisites

Before running the application, ensure the following are installed:

- Python 3.10 or later
- pip (Python package installer)
- Git
- A MongoDB Atlas account
- A code editor such as Visual Studio Code

Basic knowledge of Python, Flask, HTML, and MongoDB is recommended.

## Project Setup


1. Clone the repository:

   git clone 

2. Navigate to the project directory:

   cd flask

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

   Linux/macOS:
   source venv/bin/activate

5. Install backend dependencies:

   cd backend
   pip install -r requirements.txt

6. Install frontend dependencies:

   cd ../frontend
   pip install -r requirements.txt

## Environment Variables

## Environment Variables

The backend requires environment variables for MongoDB connectivity.

Create a `.env` file inside the backend directory and configure:

MONGO_URI=your_mongodb_connection_string

The frontend also requires a Flask secret key for flash messages.

Configure the secret key using an environment variable:

SECRET_KEY=your_secure_secret_key

Do not commit `.env` files or expose database credentials in the repository.

## How to Run the Application

The frontend and backend must run simultaneously in separate terminals.

### Start the Backend

1. Open a terminal.
2. Navigate to the backend directory:

   cd backend

3. Activate the virtual environment if it is not already active.
4. Run:

   python app.py

The backend runs on:

http://127.0.0.1:9000

### Start the Frontend

1. Open another terminal.
2. Navigate to the frontend directory:

   cd frontend

3. Activate the virtual environment if required.
4. Run:

   python app.py

The frontend runs on:

http://127.0.0.1:8000

Open the frontend URL in your browser to access the signup application.

## API Endpoints

The frontend and backend must run simultaneously in separate terminals.

### Start the Backend

1. Open a terminal.
2. Navigate to the backend directory:

   cd backend

3. Activate the virtual environment if it is not already active.
4. Run:

   python app.py

The backend runs on:

http://127.0.0.1:9000

### Start the Frontend

1. Open another terminal.
2. Navigate to the frontend directory:

   cd frontend

3. Activate the virtual environment if required.
4. Run:

   python app.py

The frontend runs on:

http://127.0.0.1:8000

Open the frontend URL in your browser to access the signup application.

## Screenshots

The screenshots folder contains application screenshots demonstrating:

- Signup page
- Successful form submission
- Error handling
- API response displaying stored records
- MongoDB records

