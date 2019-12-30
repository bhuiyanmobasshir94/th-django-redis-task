#!/bin/sh
#!/bin/sh
sudo systemctl start redis && pip install -r requirements.txt && cd django_cache && python manage.py test store.tests