import json
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader

POLICIES_PATH="./"
# POLICIES_PATH="/etc/firefox/policies/"
POLICIES_FILE= POLICIES_PATH + "policies.json"
POLICIES_INIT_FILE="./firefox-policies.json"
POLICIES_BACKUP= POLICIES_PATH + "policies.json.bak"

def is_sudo():
    return os.geteuid() == 0

def load_firefox_policies():
    try:
        with open(POLICIES_FILE) as json_file:
            json_data = json.load(json_file)
            return json_data
    except:
        with open(POLICIES_INIT_FILE) as json_file:
            json_data = json.load(json_file)
            return json_data

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


def display_error(text, e=None):
    print(text,e)
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText(text);
    msgBox.exec();


class BaleinosAdmin(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.json_policy = load_firefox_policies()

        self.loader = QUiLoader()
        self.window = self.loader.load("form.ui", None)
        self.fill_form()

    def fill_form(self):
        self.window.sudo_indicator_label.setText("✅" if is_sudo() else "❌")
        self.window.file_indicator_label.setText("✅" if os.path.isfile(POLICIES_FILE) else "❌")
        self.window.remove_policy_button.clicked.connect(disable_firefox_policies)
        self.window.save_button.clicked.connect(self.save_firefox_policies)
        self.window.homepage_edit.setText(get_homepage(self.json_policy))
        if self.json_policy is None:
            self.window.message_content_label.setText("Firefox policies.json does not exist")

    def save_firefox_policies(self):
        # Check inputs

        # update json from form
        self.json_policy["policies"]["Homepage"]["URL"] = self.window.homepage_edit.text()

        try:
            with open(POLICIES_FILE, 'w') as outfile:
                print(self.json_policy)
                outfile.write(json.dumps(self.json_policy, indent=2))
            self.window.message_content_label.setText("policies Firefox sauvegardées 👏👏")
        except Exception as e:
            display_error("Impossible de sauvegarder les modifications. Vérifier les droits d'écriture (sudo)",e)

    def run(self):
        self.window.show()
        sys.exit(self.exec())
if __name__ == "__main__":
    app = BaleinosAdmin(sys.argv)
    app.run()
