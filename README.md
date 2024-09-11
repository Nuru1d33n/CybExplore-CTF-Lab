# CybExplore CTF Lab

CybExplore CTF Lab is a Capture The Flag (CTF) platform designed for cybersecurity training and skill development. It allows users to practice and learn about various cybersecurity vulnerabilities and scenarios through interactive tasks and challenges.

## Features

- **Lab Categories**: Organize tasks into categories for better management and navigation.
- **Lab Tasks**: Various tasks with different difficulties to challenge users.
- **Progress Tracking**: Monitor user progress through tasks, including scores and completion status.
- **Comments**: Users can leave comments on tasks.
- **User Profiles**: Manage and update user profiles and view notifications.
- **Leaderboards**: View a leaderboard based on user performance.

## Technologies

- **Django**: Web framework for building the application.
- **MariaDB**: Database used to store application data.
- **Python**: Programming language used for development.

## Installation

### Prerequisites

- Python 3.8 or higher
- MariaDB
- Django 5.1.1

### Clone the Repository

```bash
git clone https://github.com/yourusername/cybexplore-ctf-lab.git
cd cybexplore-ctf-lab
```
### Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
```
bash
pip install -r requirements.txt
```

### Configure the Database
- Ensure MariaDB is running.
- Create a new database for the project:
```bash
CREATE DATABASE cybexplore_lab_db;
```
- Update your database configuration in CybExploreLab/settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cybexplore_lab_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```