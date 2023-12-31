# EFREI Crawler Exams

EFREI Crawler Exams is a Python application designed to streamline the process of retrieving essential student data from [EFREI Moodle](https://moodle.myefrei.fr/login/index.php). By inputting a student's last name, the application downloads relevant Excel sheets containing information about their classrooms & exam details.

## Purpose

This project aims to automate the extraction of student-specific schedule data, providing insights into the classrooms, schedule, date and subject information about their exams. The application simplifies the task of navigating through the website and downloading the necessary Excel sheets, making it efficient and user-friendly.

## Installation & Use

Follow these steps to set up and run the EFREI Crawler Exams application:
```
git clone https://github.com/nicvlt/efrei-crawler-exams
pip install -r requirements.txt
playwright install
python app.py
```

Create a `.env` file in the root folder as follows:
```
MOODLE_ID = "xxx-xxx"
MOODLE_PASSWORD = "xxx-xxx"
```

## Features to add

- Custom Exceptions raising.
- Beautify the output
- [tmp](tmp) folder management
