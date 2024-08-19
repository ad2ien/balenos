#!/bin/bash
set -e

cd /home/admin/balenos/admin-assets/balenos-admin-app
python3 -m venv ./venv
source ./venv/bin/activate

./venv/bin/pip install -r requirements.txt

sudo ./venv/bin/python balenosadminmainwindow.py
