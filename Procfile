release: sh -c 'python manage.py migrate && python manage.py loaddata kelurahan_data.json'
web: gunicorn depoksmartcity.wsgi --log-file -