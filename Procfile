release: sh -c 'python manage.py migrate && python manage.py loaddata kelurahan_data.json && python manage.py loaddata initial_restaurant_data.json'
web: gunicorn depoksmartcity.wsgi --log-file -