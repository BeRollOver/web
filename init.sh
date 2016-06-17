sudo apt-get update
sudo apt-get install -y Nginx
sudo apt-get install -y gunicorn
sudo apt-get install -y python-pip
sudo pip install --upgrade django

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/wsgi.py /etc/gunicorn.d/wsgi.py
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask/ask/ wsgi &