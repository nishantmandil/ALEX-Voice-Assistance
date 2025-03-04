# Alex - Your Virtual Assistant 🤖

Alex is a Python-based voice assistant that can perform a variety of tasks, including web searching, playing music, opening applications, sending emails, fetching news, and much more.

---

## 📌 Features

- 🎙️ **Voice Recognition** - Understands your voice commands.
- 🔍 **Wikipedia Search** - Retrieves short Wikipedia summaries.
- 🌐 **Web Browsing** - Opens websites like YouTube, Facebook, and Google.
- 🎵 **Play Music** - Plays your favorite songs.
- 📧 **Send Emails** - Sends emails to predefined contacts.
- 📰 **Get News Updates** - Fetches the latest headlines.
- 🖥️ **Open & Close Applications** - Launches or closes apps like Notepad, VS Code, Edge.
- 📷 **Take Screenshots** - Saves a screenshot on command.
- 🗑️ **Empty Recycle Bin** - Cleans up unnecessary files.
- 🕒 **Set Alarms** - Plays a song at a specified time.
- 🏙️ **Find Location** - Determines your current location.
- 📞 **Send WhatsApp Messages** - Uses PyWhatKit to send messages.
- 💬 **Tell Jokes** - Makes you laugh with random jokes.
- 🔢 **Perform Calculations** - Solves mathematical queries via WolframAlpha.
- 🔄 **Restart, Shutdown & Lock System** - Controls system power options.

---

## 🛠️ Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/Alex-Assistant.git
cd Alex-Assistant
2️⃣ Install Dependencies
Make sure you have Python installed. Then run:

sh
Copy
Edit
pip install -r requirements.txt
🚀 How to Run
Run the Python script:

sh
Copy
Edit
python alex.py
Speak to Alex and enjoy its features!

⚠️ Prerequisites
Python 3.7+

Install the required Python packages:

sh
Copy
Edit
pip install pyttsx3 SpeechRecognition wikipedia webbrowser pywhatkit pyjokes opencv-python requests wolframalpha winshell GoogleNews twilio pyautogui json5 instaloader PyQt5
Windows users may need to install PyAudio manually:

sh
Copy
Edit
pip install pipwin
pipwin install pyaudio
📝 Configuration
Email Sending: Update the sendEmail function with your SMTP credentials.
API Keys: Add your own WolframAlpha and NewsAPI keys for enhanced functionality.
Contacts & Phone Numbers: Modify the contact and phone dictionaries to send emails & WhatsApp messages.
🎯 Future Improvements
Adding GUI enhancements.
More integrations like weather updates.
Improved NLP for better voice recognition.
📌 Credits
Developed by Nishant Mandil. Inspired by J.A.R.V.I.S. from Iron Man. 😎

