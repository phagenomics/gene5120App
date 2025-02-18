#!/bin/bash
cd /home/ec2-user
git pull origin main
sudo systemctl restart flask_app.service
