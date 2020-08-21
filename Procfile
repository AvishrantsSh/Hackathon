web: gunicorn Hackathon.wsgi --log-file -
release: python3 manage.py makemigrations central
release: python3 manage.py makemigrations
release: python3 manage.py migrate
