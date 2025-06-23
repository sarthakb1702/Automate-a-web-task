# Instagram Automation Bot 🤖

This project automates the following tasks using Python and Selenium WebDriver:

- Logs into Instagram using a dummy account  
- Handles login popups (Save Info, Notifications)  
- Searches for the user `cbitosc`  
- Follows the account (if not already followed)  
- Extracts profile stats: Posts, Followers, Following  
- Saves the extracted data to a local text file

---

## 🔧 Requirements

- Python 3.7+
- Google Chrome (latest)
- Matching ChromeDriver (see setup)

Install required Python packages:

```bash
pip install selenium
```
🛠 Setup Instructions
1.Download the appropriate ChromeDriver for your Chrome version:
```bash
https://chromedriver.chromium.org/downloads
```

2.Place chromedriver.exe in the project directory (or add it to your system PATH)

3.Edit the following in instagram_bot.py if needed:
```python
USERNAME = "your_dummy_username"
PASSWORD = "your_dummy_password"
TARGET_USER = "cbitosc"
```
4.Run the script:
```bash
python instagram_bot.py
```

📄 Output
The script creates a text file named:
```
cbitosc_info.txt
```

💡 Notes:

Make sure to use a dummy account to avoid violating Instagram’s Terms of Service.

Instagram’s layout may change; XPath selectors may need to be updated accordingly.

If automation fails, try increasing wait times or debugging with screenshots.

