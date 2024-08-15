#!/bin/bash
set -e

cd /home/admin/baleinos/admin-assets/baleinos-admin-app
python3 -m venv ./venv
source ./venv/bin/activate

./venv/bin/pip install -r requirements.txt

sudo ./venv/bin/python baleinosadminmainwindow.py
