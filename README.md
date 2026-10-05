# Django Portfolio

This project was created from the personal profile content you shared, adapted into a clean Django site.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Notes
- This project uses a simple SQLite database and Django templates.
- The home page follows the visual identity from your HTML draft.
- You can replace the example contact links and project data in `portfolio_app/views.py`.
