
cp -r ./infrastructure/. /etc/nginx/
sudo systemctl reload nginx

source .venv/bin/activate
python manage.py migrate --settings league_fantasy.settings.prod
python manage.py collectstatic --settings league_fantasy.settings.prod

pkill -f gunicorn
nohup gunicorn league_fantasy.wsgi --env DJANGO_SETTINGS_MODULE=league_fantasy.settings.prod &

