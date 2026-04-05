# Smart Parking System

Smart Parking System is a web-based application that combines user authentication with real-time parking visualization. It uses a Flask backend with MySQL for user management and integrates a frontend dashboard for accessing parking-related features.

---

## Overview

This project demonstrates a full-stack system with authentication and dashboard access.

It includes:
- User signup and login system  
- MySQL database integration  
- Flask-based backend routing  
- Web interface for accessing parking map/dashboard  

---

## Features

### Authentication System
- User signup with password validation  
- Secure login using MySQL database  
- Error handling for invalid credentials  
- Redirect-based navigation  

### Backend System
- Flask-based routing  
- MySQL database connectivity  
- Logging for error tracking  
- Template rendering for UI pages  

### Dashboard Access
- Map/dashboard page after login  
- Structured navigation flow  
- Scalable backend for adding features  

---

## Tech Stack

- **Backend:** Flask (Python)  
- **Database:** MySQL  
- **Frontend:** HTML, CSS  
- **Other:** Logging module  

---

## Project Structure

```
Parking/
│── template/           # HTML templates
│── app.py              # Main Flask application
│── flask_errors.log    # Error logs
│── README.md
```

---

## Installation

1. Clone the repository  
```bash
git clone https://github.com/ProjectBA14/Parking.git
```

2. Navigate to the project directory  
```bash
cd Parking
```

3. Install dependencies  
```bash
pip install flask mysql-connector-python
```

4. Setup MySQL database  
- Create a database named `login`  
- Create table:

```sql
CREATE TABLE userinfo (
    mailid VARCHAR(255),
    password VARCHAR(255)
);
```

---

## Usage

1. Run the Flask app  
```bash
python app.py
```

2. Open in browser  
```
http://localhost:8001
```

3. Use the system  
- Sign up a new user  
- Login with credentials  
- Access dashboard/map page  

---

## Application Flow

- User lands on homepage  
- Navigates to login/signup  
- Credentials validated using MySQL  
- On success → redirected to dashboard (`/maps`)  
- On failure → error message displayed  

---

## Screenshots

Add screenshots inside a folder (e.g., `/assets`) and update paths below:

```
![Login Page](./assets/login.png)
![Signup Page](./assets/signup.png)
![Dashboard](./assets/dashboard.png)
```

---

## Limitations

- Passwords are stored in plain text (not secure)  
- No session management or authentication tokens  
- Basic UI without responsiveness  
- Limited validation and security checks  

---

## Future Improvements

- Password hashing (bcrypt)  
- Session-based authentication  
- Role-based access control  
- Improved UI/UX  
- Integration with parking detection system  
- Deployment on cloud  

---

## License

This project is intended for academic and demonstration purposes.
