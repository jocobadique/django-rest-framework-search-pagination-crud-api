📘 Drinks Backend — Django REST API

A backend project built using Django REST Framework featuring:

Full CRUD API for Drinks & Categories

Advanced pagination with URLs

Search, filter, and ordering

JWT Authentication (SimpleJWT)

Browsable API login

Role-based permissions (Admin-only write access)

Unified API response formatting

Custom validation (duplicate name, required category)

Admin panel integration



📂 Project Structure
petsival-backend/
│
├── api/                     # Main Django app (Drinks, Categories)
├── backend_django/          # Django project folder
├── venv/                    # Virtual environment (ignored in Git)
└── README.md

⚙️ Backend — Django REST Framework
📌 Features
✔ Unified API Response Format

All endpoints return responses in this format:

{
  "data": { ... },
  "message": "",
  "error": null,
  "status": 200
}

✔ Drink Management (CRUD)

Unique name validation

Category required

Searchable and filterable

Ordering supported

Custom response structure

Accepts category by ID or by name

✔ Category Support

Manageable inside Django Admin

Required for every drink

Category name automatically returned in responses

✔ Advanced Pagination

Includes:

results

filtered_count

total_count

page

page_size

total_pages

next_page_url

prev_page_url

Format:

"data": {
  "results": [...],
  "pagination": {
    "filtered_count": 37,
    "total_count": 120,
    "page": 2,
    "page_size": 10,
    "total_pages": 12,
    "next_page_url": "/api/drinks/?page=3",
    "prev_page_url": "/api/drinks/?page=1"
  }
}

✔ Role-Based Permissions

Only users whose:

user.profile.role == "admin"


can create, update, and delete.

All authenticated users can read.

✔ Authentication

JWT Authentication (SimpleJWT)

Session Authentication for DRF's browsable UI

✔ Admin Panel

Manage:

Drinks

Categories

With searching and filtering built-in.

▶️ Running the Backend Locally
1️⃣ Clone the repo
git clone <your-repo-url>
cd petsival-backend

2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Run the server
python manage.py runserver


Backend API will be available at:

http://127.0.0.1:8000/api/


Browsable API Login:

http://127.0.0.1:8000/api-auth/login/


Admin Panel:

http://127.0.0.1:8000/admin/

🧪 API Endpoints
JWT Authentication
Method	Endpoint	Description
POST	/api/token/	Obtain access + refresh token
POST	/api/token/refresh/	Refresh access token
Drinks
Method	Endpoint	Description
GET	/api/drinks/	List (search, filter, ordering, pagination)
POST	/api/drinks/	Create drink (admin only)
GET	/api/drinks/<id>/	Retrieve drink
PUT	/api/drinks/<id>/	Update drink (admin only)
DELETE	/api/drinks/<id>/	Delete drink (admin only)

Supports:

?search=cola
?category=1
?ordering=name
?page=1
?page_size=20

Categories
Method	Endpoint	Description
GET	/admin/api/category/	Manage inside Django Admin
🔧 Request Format Examples
Create Drink (via JSON)
{
  "name": "Coke",
  "category": "Soda"
}


Supports:

"Soda" (name)

2 (category ID)

Error Example (duplicate name)
{
  "data": null,
  "message": "See error on form fields",
  "error": {
    "name": ["See error on field"]
  },
  "status": 400
}

📄 Environment & Tools

Python 3

Django 5

Django REST Framework

SimpleJWT

django-filter

🧪 Testing (Optional)
pytest

👨‍💻 Author

Joco Badique
Software Engineer
