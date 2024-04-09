#!/usr/bin/bash 

sed -i 's/\[]/\["18.201.240.183"]/' /home/ubuntu/restaurant/restaurant/settings.py

python manage.py migrate 
python manage.py makemigrations     
python manage.py collectstatic -noinput
sudo service gunicorn restart
sudo service nginx restart
#sudo tail -f /var/log/nginx/error.log
#sudo systemctl reload nginx
#sudo tail -f /var/log/nginx/error.log
#sudo nginx -t
#sudo systemctl restart gunicorn
#sudo systemctl status gunicorn
#sudo systemctl status nginx
# Check the status
#systemctl status gunicorn
# Restart:
#systemctl restart gunicorn
#sudo systemctl status nginx
