# 📘 Drinks Backend — Django REST API
A backend project built using Django REST Framework featuring full CRUD for drinks/categories, role-based permissions, and advanced pagination.

Built with:

- **Backend:** Django 5 + Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Filtering:** django-filter
- **Pagination:** Custom advanced pagination
- **Serialization:** DRF ModelSerializers
- **Architecture:** Unified API Response & Role-Based Access


---


# 📂 Project Structure
```
drinks-api/
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
├── core/                # Project settings
├── manage.py
└── README.md            # Documentation
```

---

# Unified Response Structure

{
  "data": { ... },
  "message": "",
  "error": null,
  "status": 200
}

---

# ✔ Advanced Pagination

"data": {
  "results": [...],
  "pagination": {
    "filtered_count": 37,
    "total_count": 120,
    "page": 2,
    "page_size": 10,
    "total_pages": 12,
    "next_page_url": "/api/drinks/?page=3&page_size=10",
    "prev_page_url": "/api/drinks/?page=1&page_size=10"
  }
}


