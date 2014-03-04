web: python royalfashioncph/manage.py compress; python royalfashioncph/manage.py update_index; newrelic-admin run-program gunicorn -w 3 -k gevent --max-requests 500 royalfashioncph.wsgi
