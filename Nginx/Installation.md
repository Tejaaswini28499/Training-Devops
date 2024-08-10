# Nginx Installation Amazon Linux 2023

sudo dnf update -y
sudo dnf install nginx -y
sudo systemctl start nginx
sudo systemctl enable  nginx
sudo systemctl status nginx