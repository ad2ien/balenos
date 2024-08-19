import json
import os
import shutil
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader

POLICIES_PATH="/etc/firefox/policies/"
POLICIES_INIT_FILE="/home/admin/balenos/assets/firefox-policies.json"
POLICIES_BACKUP= POLICIES_PATH + "policies.json.bak"

USER_ACCOUNT="personne"

def is_sudo():
    return os.geteuid() == 0

def load_firefox_policies(policies_full_filename):
    """
    Load policies.json used for restraining firefox use on every account
    if /etc/firefox/policies/policies.json does not exist, use a local template file
    """
    try:
        with open(policies_full_filename) as json_file:
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

def are_firefox_policies_disabled(policies_full_filename):
    return os.path.isfile(POLICIES_BACKUP) and not os.path.isfile(policies_full_filename)

def disable_firefox_policies(policies_full_filename):
    if not is_sudo():
        display_error("Il faut lancer la commande avec `sudo`")
        return False
    
    if not os.path.isfile(policies_full_filename):
        display_error("Le fichier policies de firefox n'existe pas")
        return False
    
    os.rename(policies_full_filename, POLICIES_BACKUP)
    return True

def get_configured_searchengine_list(json):
    engine_array = json["policies"]["SearchEngines"]["Add"]
    return [engine["Name"] for engine in engine_array]

def get_default_search_engine(json):
    return json["policies"]["SearchEngines"]["Default"]

def display_error(text, e=None):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText(text)
    msgBox.exec()

def move_bookmarks_to_user_profile(target_user):
    if not is_sudo():
        display_error("Il faut lancer l'application avec commande avec `sudo`")
        return
    
    # Get the source and destination Firefox paths
    src_firefox_folder = get_default_folder(os.listdir(f"/home/{os.getlogin()}/snap/firefox/common/.mozilla/firefox/"))
    src_firefox_path = f"/home/{os.getlogin()}/snap/firefox/common/.mozilla/firefox/{src_firefox_folder}"

    dest_firefox_folder = get_default_folder(os.listdir(f"/home/{target_user}/snap/firefox/common/.mozilla/firefox/"))
    dest_firefox_path = f"/home/{target_user}/snap/firefox/common/.mozilla/firefox/{dest_firefox_folder}"

    # Backup the places.sqlite file
    print("Backup places.sqlite.bkp")
    shutil.copy2(f"{dest_firefox_path}/places.sqlite", f"{dest_firefox_path}/places.sqlite.bkp")

    # Copy the places.sqlite file
    shutil.copy2(f"{src_firefox_path}/places.sqlite", f"{dest_firefox_path}/places.sqlite")
    shutil.chown(f"{dest_firefox_path}/places.sqlite", user=f"{target_user}", group=f"{target_user}")

    return True

def get_default_folder(folder_array):
    return [folder for folder in folder_array if ".default" in folder][0]

class BalenosAdmin(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.loader = QUiLoader()
        self.window = self.loader.load("form.ui", None)

        self.window.user_account_name_lineEdit.setText(USER_ACCOUNT)
        self.user_account = USER_ACCOUNT
        self.window.policies_path_lineEdit.setText(POLICIES_PATH)
        self.json_policy = load_firefox_policies(self.get_policies_full_file())

        self.window.save_button.clicked.connect(self.save_firefox_policies)
        self.window.remove_policy_button.clicked.connect(self.disable_firefox_policies)
        self.window.transfer_bookmarks_button.clicked.connect(self.move_bookmarks_to_user_profile)
        self.window.user_account_name_lineEdit.textEdited.connect(self.change_user_account)
        self.window.policies_path_lineEdit.textEdited.connect(self.fill_form)
        self.fill_form()

    def get_policies_path(self):
        return self.window.policies_path_lineEdit.text()
    
    def get_policies_full_file(self):
        return self.get_policies_path() + "policies.json"
    
    def disable_firefox_policies(self):
        disable_firefox_policies(self.get_policies_full_file())
        self.window.message_content_label.setText("👍 restrictions Firefox désactivées")
        self.fill_form()
    
    def move_bookmarks_to_user_profile(self):
        if move_bookmarks_to_user_profile(self.user_account):
            self.window.message_content_label.setText(f"Marques-pages transférés sur le compte {self.user_account} 🚚")
        else:
            display_error("Une erreur est survenue 🤷")


    def change_user_account(self):
        self.user_account = self.window.user_account_name_lineEdit.text()

    def fill_form(self):
        self.window.sudo_indicator_label.setText("✅" if is_sudo() else "❌")
        self.window.file_indicator_label.setText("✅" if os.path.isfile(self.get_policies_full_file()) else "❌")
        self.window.homepage_edit.setText(get_homepage(self.json_policy))
        self.window.engine_comboBox.addItems(get_configured_searchengine_list(self.json_policy))
        self.window.engine_comboBox.setCurrentText(get_default_search_engine(self.json_policy))
        if self.json_policy is None:
            display_error("Firefox policies.json does not exist ??")

    def save_firefox_policies(self):
        # TODO Check inputs

        # update json from form
        self.json_policy["policies"]["Homepage"]["URL"] = self.window.homepage_edit.text()
        self.json_policy["policies"]["SearchEngines"]["Default"] = self.window.engine_comboBox.currentText()

        try:
            with open(self.get_policies_full_file(), 'w') as outfile:
                outfile.write(json.dumps(self.json_policy, indent=2))
            self.window.message_content_label.setText("policies Firefox sauvegardées / activées 👏👏")
            self.fill_form()
        except Exception as e:
            display_error("Impossible de sauvegarder les modifications. Vérifiez les droits d'écriture (sudo)",e)

    def run(self):
        self.window.show()
        sys.exit(self.exec())

if __name__ == "__main__":
    app = BalenosAdmin(sys.argv)
    app.run()

