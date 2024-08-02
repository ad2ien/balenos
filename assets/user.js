// Disable saving passwords:
user_pref("signon.rememberSignons", false);

// Disable autofill login and passwords:
user_pref("signon.autofillForms", false);

// Disable formless login capture for Password Manager:
user_pref("signon.formlessCapture.enabled", false);

// Disable private browsing mode and enable restoring sessions
user_pref("browser.privatebrowsing.autostart", false);

// start with defined homepage
user_pref("browser.startup.page", 1);

// Enable persistence of site data
user_pref("permissions.memory_only", false);

// Customise clear on shutdown
user_pref("privacy.clearOnShutdown.cache", true);
user_pref("privacy.clearOnShutdown.cookies", true);
user_pref("privacy.clearOnShutdown.sessions", true);
user_pref("privacy.clearOnShutdown.offlineApps", true);
user_pref("privacy.clearOnShutdown.openWindows", false);
user_pref("privacy.clearOnShutdown.siteSettings", false);
user_pref("privacy.clearOnShutdown.downloads", false);
user_pref("privacy.clearOnShutdown.formdata", false);
user_pref("privacy.clearOnShutdown.history", false);