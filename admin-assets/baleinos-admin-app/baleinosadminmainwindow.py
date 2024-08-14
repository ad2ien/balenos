import json
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader

POLICIES_PATH="./"
# POLICIES_PATH="/etc/firefox/policies/"
POLICIES_FILE= POLICIES_PATH + "policies.json"
POLICIES_BACKUP= POLICIES_PATH + "policies.json.bak"

def is_sudo():
    return os.geteuid() == 0

def load_firefox_policies():
    try:
        with open(POLICIES_FILE) as json_file:
            json_data = json.load(json_file)
            return json_data
    except:
        return None

def get_homepage(json):
    try:
        return json["policies"]["Homepage"]["URL"]
    except:
        return None

def are_firefox_policies_disabled():
    return os.path.isfile(POLICIES_BACKUP) and not os.path.isfile(POLICIES_FILE)

def disable_firefox_policies():
    print("disable_firefox_policies")
    if not is_sudo():
        display_error("Il faut lancer la commande avec `sudo`")
        return False
    
    if not os.path.isfile(POLICIES_FILE):
        display_error("Le fichier policies de firefox n'existe pas")
        return False
    
    os.rename(POLICIES_FILE, POLICIES_BACKUP)
    return True

def save_firefox_policies(json):
    # update json from form
    with open(POLICIES_FILE, 'w') as outfile:
        json.dump(json, outfile)

def display_error(text):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText(text);
    msgBox.exec();

if __name__ == "__main__":
    json_policy = load_firefox_policies()
        
    app = QApplication(sys.argv)
    loader = QUiLoader()
    window = loader.load("form.ui",None)
    window.sudo_indicator_label.setText( "✅" if is_sudo() else "❌" )
    window.file_indicator_label.setText( "✅" if os.path.isfile(POLICIES_FILE) else "❌" )
    window.remove_policy_button.clicked.connect(disable_firefox_policies)
    window.homepage_edit.setText(get_homepage(json_policy))
    if json_policy is None:
        window.message_content_label.setText("Firefox policies.json does not exist")
        # window.remove_policy_button.setEnabled(False)
    window.show()
    sys.exit(app.exec())
