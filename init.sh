apt-get update
apt-get install -y Nginx
apt-get install -y gunicorn
apt-get install -y python-pip
sudo pip install --upgrade django

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/wsgi.py /etc/gunicorn.d/wsgi.py
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask/ask wsgi &