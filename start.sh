
cp -r ./infrastructure/. /etc/nginx/
sudo systemctl reload nginx

source .venv/bin/activate
python manage.py migrate --settings self_checklist_proto.settings.prod
python manage.py collectstatic --settings self_checklist_proto.settings.prod

pkill -f gunicorn
nohup gunicorn self_checklist_proto.wsgi --env DJANGO_SETTINGS_MODULE=self_checklist_proto.settings.prod &

