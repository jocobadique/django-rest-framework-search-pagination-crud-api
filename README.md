# 📘 Drinks Backend — Django REST API
A backend project built using Django REST Framework featuring full CRUD for drinks/categories, role-based permissions, and advanced pagination.

Built with:

- **Backend:** Django 5 + Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Filtering:** django-filter
- **Architecture:** Unified API Response & Role-Based Access


---

# 📂 Project Structure
```
backend-django/
│
├── api/                 # Application module
│   ├── models.py        # Drink + Category models
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # ViewSets with CRUD, validation, roles
│   ├── pagination.py    # Custom pagination with next/prev URLs
│   ├── permissions.py   # Role-based permission class
│   ├── urls.py          # Router-based API URLs
│   └── utils/
│       └── response.py  # Unified API response formatter
│
├── backend_django/      # Project settings
├── manage.py
└── README.md            # Documentation
```


