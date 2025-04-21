---
<p align="center">
  <h1>🎯 <span style="color:#DC143C">MilanoTask</span> 🖤</h1>
  <p><em>🗒️ A Flask to‑do list app with login/auth, styled in AC Milan red ❤️ &amp; black 🖤</em></p>
</p>
---

## 🚩 About
**MilanoTask** is a sleek Flask‑powered to‑do list web application featuring user registration, login/logout, and full CRUD operations on tasks. Built with the application‑factory pattern and styled in Milan’s iconic red ❤️ &amp; black 🖤.

## ✨ Features
- 🔴 **User Authentication**  
  - Register new users (username, email, securely hashed passwords)  
  - Login &amp; logout with session protection via `@login_required`  
- ⚫️ **Task Management**  
  - Create, view, edit &amp; delete personal to‑do items  
  - Toggle completion status (completed tasks are struck through)  
- 🔴 **Factory Pattern**  
  - `create_app()` initializes Flask, SQLAlchemy, Flask‑Login &amp; blueprints  
- ⚫️ **Responsive UI**  
  - Jinja2 templates &amp; Bootstrap overrides in `static/css/style.css`  
- 🔴 **AC Milan Theme**  
  - Custom CSS variables define `--primary-color: #DC143C` &amp; `--secondary-color: #000000`  

## 🚀 Tech Stack
- **Backend:** Python &amp; [Flask](https://palletsprojects.com/p/flask/)  
- **Database:** SQLite (via Flask‑SQLAlchemy)  
- **Frontend:** HTML5, CSS3 &amp; Bootstrap 5  

## 🛠️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YoussefNasr909/MilanoTask.git
   cd MilanoTask
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install Flask Flask-Login Flask-WTF Flask-SQLAlchemy
   ```

4. **Set environment variables**  
   ```bash
   export SECRET_KEY="your_secret_key"      # default is 'dev-key-for-testing'
   ```

5. **Initialize the database**  
   ```bash
   python app.py    # auto-creates todo.db in project root
   ```

## ▶️ Usage
```bash
python app.py    # starts Flask in debug mode
```
- Visit <http://127.0.0.1:5000/>  
- 🔴 Register a new account or 🖤 log in  
- ⚫️ Add, edit, delete or toggle completion of tasks  

## 📂 Project Structure
```
MilanoTask/
├── app.py                    # Entry point: calls create_app()
├── todo/
│   ├── __init__.py           # Factory, DB & LoginManager setup
│   ├── auth.py               # Blueprint: register & login
│   ├── tasks.py              # Blueprint: task CRUD routes
│   ├── models.py             # SQLAlchemy models: User & Task
│   ├── forms.py              # WTForms: Auth & Task forms
│   ├── static/css/style.css  # AC Milan theme overrides
│   └── templates/            # Jinja2 HTML templates
└── requirements.txt          # Locked dependencies
```

## 🤝 Contributing
1. Fork this repo  
2. Create a branch: `git checkout -b feature/YourFeature`  
3. Commit your changes: `git commit -m "Add feature"`  
4. Push branch: `git push origin feature/YourFeature`  
5. Open a Pull Request  

---

❤️🖤 Enjoy managing your tasks in true Milan style! 🎉
```
