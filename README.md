# 🍳 Recipe Manager - Django Project

## ⚡ Quick Start (30 seconds)

```bash
cd FinalProjectDJ
python manage.py runserver
```
Open **http://127.0.0.1:8000/** in your browser. **Done!** You'll see 5 sample recipes ready to use.

---

## 📋 Project Overview

A full-stack **Django web application** for managing recipes and their ingredients. Built for **3-person team collaboration** with professional UI and clear code structure.

**Demonstrates:**
- Database design (Models with ForeignKey relationships)
- CRUD operations (Create, Read, Update, Delete)
- URL routing (RESTful-style patterns)
- Template rendering (Server-side HTML with inheritance)
- Admin interface (Django's built-in admin panel)
- Professional UI (Responsive design, gradient backgrounds, navigation bar)

---

## 📁 Project Structure

```
FinalProjectDJ/
├── manage.py                    # Django management script
├── db.sqlite3                   # SQLite database (5 recipes, 37 ingredients)
├── recipe_project/              # Project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL router
│   ├── asgi.py & wsgi.py       # Application servers
│
└── recipes/                     # Main app
    ├── models.py               # Recipe & Ingredient models
    ├── views.py                # 8 CRUD view functions
    ├── urls.py                 # Recipe app URL patterns
    ├── admin.py                # Admin panel configuration
    ├── management/commands/    # Custom commands
    │   └── populate_recipes.py # Sample data (5 recipes, 37 ingredients)
    │
    └── templates/recipes/      # HTML templates
        ├── base.html           # 🆕 Master template with navigation
        ├── recipe_list.html    # Recipe grid display
        ├── recipe_detail.html  # Recipe view + ingredients
        ├── recipe_form.html    # Create/edit recipe
        ├── recipe_confirm_delete.html
        ├── ingredient_form.html
        └── ingredient_confirm_delete.html
```

---

## 🗄️ Database Models

### Recipe Model
```python
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### Ingredient Model
```python
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, blank=True)
    unit = models.CharField(max_length=50, blank=True)
```

**Key Relationship:** One Recipe → Many Ingredients (One-to-Many)
- ForeignKey with CASCADE delete ensures ingredients are removed when recipe is deleted

---

## 🔄 CRUD Operations

### Recipe Operations
| Operation | View | URL | Method |
|-----------|------|-----|--------|
| **List** | `recipe_list` | `/` | GET |
| **View Detail** | `recipe_detail` | `/recipe/<id>/` | GET |
| **Create** | `recipe_create` | `/recipe/new/` | GET/POST |
| **Update** | `recipe_update` | `/recipe/<id>/edit/` | GET/POST |
| **Delete** | `recipe_delete` | `/recipe/<id>/delete/` | GET/POST |

### Ingredient Operations
| Operation | View | URL | Method |
|-----------|------|-----|--------|
| **Add** | `ingredient_add` | `/recipe/<id>/ingredient/new/` | GET/POST |
| **Edit** | `ingredient_edit` | `/recipe/<id>/ingredient/<ing_id>/edit/` | GET/POST |
| **Delete** | `ingredient_delete` | `/recipe/<id>/ingredient/<ing_id>/delete/` | GET/POST |

---

## 🚀 Setup & Running

### 1. Install Django
```bash
pip install django
```

### 2. Migrate Database (if needed)
```bash
python manage.py migrate
```

### 3. Run Development Server
```bash
python manage.py runserver
```
App available at: **http://127.0.0.1:8000/**

### 4. Create Admin Account
```bash
python manage.py createsuperuser
# Then visit http://127.0.0.1:8000/admin/
```

### 5. Load Sample Data
```bash
python manage.py populate_recipes
```
Loads 5 recipes with 37 ingredients total:
1. **Classic Chocolate Chip Cookies** - 9 ingredients
2. **Spaghetti Carbonara** - 6 ingredients
3. **Thai Green Curry** - 8 ingredients
4. **Avocado Toast** - 6 ingredients
5. **Homemade Pizza** - 8 ingredients

---

## ✅ Features

✅ **Full CRUD** - Create, read, update, delete recipes & ingredients
✅ **ForeignKey Relationships** - Proper database relationships with cascade delete
✅ **Django Admin** - Built-in admin interface with inline ingredient editing
✅ **Form Validation** - Required field checking and error handling
✅ **Professional Design** - Gradient backgrounds, responsive layout, emoji icons
✅ **Template Inheritance** - base.html reduces code duplication (DRY principle)
✅ **Sample Data** - Pre-populated 5 recipes with 37 ingredients
✅ **RESTful URLs** - Clean, intuitive URL patterns
✅ **Mobile Responsive** - Works on desktop, tablet, and mobile
✅ **Navigation Bar** - Consistent sticky navigation across all pages
✅ **Confirmation Dialogs** - Safe deletion with warning pages

---

## 👥 Team Collaboration Benefits

Designed for **3 people working together:**
- ✅ **Shared Navigation** - Single nav bar maintained in base.html
- ✅ **Consistent Styling** - Purple gradient applied globally (#667eea → #764ba2)
- ✅ **Template Inheritance** - Changes made once, applied everywhere
- ✅ **Clear Code Structure** - Easy to understand and review
- ✅ **Single Documentation** - This README.md has everything needed
- ✅ **Scalable Design** - Easy to add features without breaking existing code

---

## 💻 Technology Stack

- **Framework:** Django 5.2.8
- **Database:** SQLite3 (development)
- **Frontend:** HTML5 + CSS3 (responsive, inline styling)
- **Python:** 3.11+
- **Server:** Django development server

---

## 🎓 How to Use the Application

### View All Recipes
- Homepage shows grid of recipe cards with images
- Click "View" button or recipe title to see details

### Create New Recipe
- Click **"+ New Recipe"** in navbar
- Enter title (required) and description (optional)
- Recipe appears in list immediately

### Edit Recipe
- Click **"Edit"** on recipe card or detail page
- Modify title or description
- Click **"Save Changes"**

### Add Ingredient to Recipe
- View recipe detail page
- Click **"+ Add Ingredient"** button
- Enter name (required), quantity & unit (optional)
- Click **"Add Ingredient"**

### Delete Recipe
- Click **"Delete"** button
- Red warning page shows recipe details
- Click **"Yes, Delete Recipe"** to confirm
- Recipe and all ingredients removed

### Delete Ingredient
- View recipe detail page
- Click **"Delete"** next to ingredient
- Confirm deletion

---

## 📺 Presentation Script (5 minutes)

### 1. Homepage Demo (30 seconds)
- Open http://127.0.0.1:8000/
- Show 5 recipe cards in grid
- Point out navigation bar with logo "🍳 Recipe Manager"

### 2. View Recipe (30 seconds)
- Click "View" button on a recipe
- Show ingredients list
- Show "Edit", "Delete", "+ Add Ingredient" buttons

### 3. Create Recipe (1 minute)
- Click "+ New Recipe" in navbar
- Fill in title and description
- Save and show it appears in list
- Demonstrate form validation (try to save without title)

### 4. Edit Recipe (1 minute)
- Click "Edit" on a recipe
- Change the description
- Save and verify changes show in detail view

### 5. Delete Recipe (1 minute)
- Click "Delete" button
- Show red warning confirmation page
- Click "Yes, Delete Recipe"
- Show recipe removed from list

### 6. Code Tour (1 minute)
- Open VS Code
- Show `models.py` (Recipe + Ingredient with ForeignKey)
- Show `views.py` (8 functions with GET/POST handling)
- Show `urls.py` (RESTful patterns)
- Show `base.html` (navigation template)

### 7. Admin Panel (1 minute)
- Open /admin/ and login
- Show Recipe list in admin
- Show inline ingredient editing
- Add new ingredient through admin

---

## ⚙️ Troubleshooting

**Port 8000 in use**
```bash
python manage.py runserver 8001
```

**Database errors**
```bash
python manage.py migrate
```

**Want fresh database**
```bash
rm db.sqlite3
python manage.py migrate
python manage.py populate_recipes
```

**Admin password forgotten**
```bash
python manage.py changepassword <username>
```

---

## 🎯 Learning Outcomes

Understanding gained from this project:
- ✅ Django app structure and organization
- ✅ Model creation and ForeignKey relationships
- ✅ Database migrations and ORM
- ✅ Function-based views for CRUD
- ✅ GET/POST request handling
- ✅ Form validation and rendering
- ✅ Template rendering and inheritance
- ✅ URL routing with named patterns
- ✅ Django admin customization
- ✅ Cascading deletes in databases
- ✅ Responsive CSS and mobile design

---

## 🚀 Future Enhancements

Possible improvements:
- User authentication (login/logout)
- User-specific recipes
- Search and filtering
- Recipe categories/tags
- Star ratings and reviews
- Ingredient calculations
- Nutritional information
- Export to PDF
- REST API (Django REST Framework)
- Shopping list feature
- Recipe scaling

---

## 📚 Technical Deep Dive

### View Pattern
```python
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
```
- GET requests display data
- POST requests handle form submission
- Redirects after successful operations

### Template Inheritance
```html
{% extends 'recipes/base.html' %}
{% block title %}Recipe - Recipe Manager{% endblock %}
{% block content %}
    <!-- Page-specific content -->
{% endblock %}
```

### URL Pattern
```python
path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail')
# Usage in template: <a href="{% url 'recipe_detail' recipe.pk %}">View</a>
```

### Cascade Delete
```python
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # When Recipe is deleted, all its Ingredients are automatically deleted
```

---

## 🎨 Design Details

### Color Palette
- **Primary Gradient:** #667eea → #764ba2 (purple)
- **Navigation:** Dark background (#222)
- **Text:** Dark gray (#333, #666)
- **Danger:** Red (#e74c3c)
- **Success:** Blue (#667eea)

### UX Features
- Emoji icons (🍳, ➕, ✏️, 🗑️) for quick scanning
- Hover effects on buttons and cards
- Red warning dialogs for destructive actions
- Form validation feedback
- Responsive mobile design

### Typography
- Clear headings hierarchy
- Readable font sizes
- Good contrast ratios
- Mobile-optimized line height

---

## 📝 Project Completion

**Status:** ✅ Complete and Production-Ready

**What's Included:**
- ✅ All 5 Parts (Models, Views, URLs, Templates, Admin)
- ✅ 5 Sample Recipes with 37 Ingredients
- ✅ 8 CRUD Operations (Recipes + Ingredients)
- ✅ Professional UI with Navigation
- ✅ Template Inheritance (DRY principle)
- ✅ Responsive Design
- ✅ Form Validation
- ✅ Django Admin Panel
- ✅ Single Comprehensive Documentation

**Ready for:**
- ✅ Team presentation (5 minutes)
- ✅ Code review
- ✅ Learning reference
- ✅ Extension with new features

---

**Django Version:** 5.2.8
**Python Version:** 3.11+
**Last Updated:** December 7, 2025
**Developed for:** 3-person team collaboration
