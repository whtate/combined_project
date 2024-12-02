# Waddle Django Project

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Creating a Superuser](#creating-a-superuser)
- [Running the Development Server](#running-the-development-server)
- [Usage](#usage)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/downloads)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (optional but recommended)

## Installation

### 1. Clone the Repository

Open your terminal and clone the repository:

```bash
git clone https://github.com/whtate/combined_project
cd combined_project
```

*Replace `<YOUR_GITHUB_REPO_URL>` with the URL of your Git repository.*

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```
## Configuration

### 1. Set Up Environment Variables

The project uses environment variables to manage sensitive information like the Django secret key and the Mapbox API token.

1. **Create a `.env` File:**

   Copy the provided `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` File:**

   Open the `.env` file in your preferred text editor and set the following variables:

   ```env
   SECRET_KEY=your_django_secret_key_here
   MAPBOX_ACCESS_TOKEN=your_mapbox_access_token_here
   DEBUG=True

   ```

   - **SECRET_KEY:** Generate a unique secret key for Django. You can use Django's `get_random_secret_key` method:

     ```python
     from django.core.management.utils import get_random_secret_key
     print(get_random_secret_key())
     ```

   - **MAPBOX_ACCESS_TOKEN:** Obtain your Mapbox access token from your [Mapbox account](https://account.mapbox.com/access-tokens/).

   - **DEBUG:** Set to `True` for development and `False` for production.

### 2. Ensure `.env` is Excluded from Git

The `.gitignore` file is configured to exclude the `.env` file, ensuring that sensitive information is not committed to the repository.

## Database Setup

### 1. Apply Migrations

Apply the database migrations to set up the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

*If you encounter prompts about adding non-nullable fields, provide appropriate default values as instructed.*

### 2. Handle Initial Migration Issues (If Any)

If migrations prompt you to provide default values for non-nullable fields (e.g., `created_by`), ensure you have a superuser created to assign as the default.

## Creating a Superuser

Create a superuser account to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser account with a username, email, and password.

## Running the Development Server

Start the Django development server with the following command:

```bash
python manage.py runserver
```

Access the application by navigating to `http://127.0.0.1:8000/` in your web browser.

## Usage

1. **Register an Account:**
   - Navigate to `http://127.0.0.1:8000/register/`.
   - Fill out the registration form to create a new user account.

2. **Log In:**
   - Navigate to `http://127.0.0.1:8000/login/`.
   - Enter your credentials to log in.

3. **Add Events:**
   - After logging in, navigate to the map view.
   - Click on the "Add Event" button to add a new event with a title, description, date, and geographic coordinates.

4. **View Events on the Map:**
   - All added events will be displayed as markers on the interactive Mapbox map.
   - Click on a marker to view event details in a popup.

5. **Admin Interface:**
   - Access the admin interface at `http://127.0.0.1:8000/admin/` using your superuser credentials.
   - Manage users and events through the admin dashboard.

---

**Note:** Ensure that all environment variables are correctly set in your `.env` file before running the application. Do not share your `.env` file or expose sensitive information in the repository.

---
