web: gunicorn Hackathon.wsgi --log-file -
clock: python3 updater.py
release: python3 manage.py makemigrations central
release: python3 manage.py makemigrations
release: python3 manage.py migrate
