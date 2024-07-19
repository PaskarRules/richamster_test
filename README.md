# Project Title

This is a web project utilizing Django and Django REST Framework to manage announcements.

## Technology Stack

- Django
- Django REST Framework (DRF)
- DRF-YASG (Yet Another Swagger Generator)
- PostgreSQL

## Setup Instructions

### Creating Virtual Environment

```bash
python3 -m venv myprojectenv
```

### Activating the Virtual Environment

```bash
source myprojectenv/bin/activate
```

### Installing Dependencies

```bash
pip install -r requirements.txt
```

### Database Migrations

Create migrations:

```bash
./manage.py makemigrations
```

Apply migrations:

```bash
./manage.py migrate
```

### Running the Server

```bash
./manage.py runserver
```

## Endpoints

### Public Access

- `GET api/announcement/` - Retrieves all announcements with their details.
- `GET api/announcement/count/` - Returns the total count of announcements.
- `GET api/announcement/<announcement_id>/` - Retrieves a specific announcement.

- `POST api/announcement/<announcement_id>/like/` - Likes an announcement, requires `user_id` in the request body.
- `POST api/announcement/<announcement_id>/dislike/` - Dislikes an announcement, requires `user_id` in the request body.

### Restricted Access (Authenticated, Admins Only)

- `POST api/announcement/` - Create a new announcement.
- `PUT api/announcement/<announcement_id>/` - Fully update an existing announcement.
- `PATCH api/announcement/<announcement_id>/` - Partially update an existing announcement.
- `DELETE api/announcement/<announcement_id>/` - Delete an announcement.
```
