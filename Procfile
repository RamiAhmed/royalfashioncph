web: python ./manage.py compress; python ./manage.py update_index; newrelic-admin run-program python ./manage.py run_gunicorn -w 3 -k gevent --max-requests 500 royalfashioncph.wsgi