# 💬 Modern Real-Time Chat Application

A full-stack, real-time messaging application built with **Django**, **Django Channels (WebSockets)**, and **Vanilla JavaScript**. This project demonstrates the ability to handle bidirectional client-server communication, database persistence, and secure user authentication.

## ✨ Key Features

* **⚡ Real-Time Messaging:** Bidirectional communication powered by WebSockets (Django Channels) ensures zero-refresh message delivery.
* **🔍 Client-Side Search:** A highly optimized, real-time search bar that filters and highlights text in the DOM instantly as the user types.
* **🔐 Secure Authentication:** Custom login and registration flows with a modern, glassmorphism UI.
* **💾 Database Persistence:** All messages, user data, and room histories are securely stored in a relational database (SQLite).
* **📸 Image Attachments:** Users can seamlessly attach and render base64-encoded images within the chat flow.
* **🗑️ CRUD Operations:** Users can instantly delete their own messages, with WebSockets instantly broadcasting the removal to all connected clients.
* **♻️ Auto-Reconnect Logic:** The client-side JavaScript automatically attempts to re-establish dropped WebSocket connections, ensuring a seamless user experience.

## 🛠️ Tech Stack

**Backend:**
* Python 3 / Django
* Django Channels (WebSockets / ASGI)
* SQLite (Relational Database)
* python-dotenv (Environment Variable Security)

**Frontend:**
* HTML5 / CSS3 (Custom Glassmorphism UI & Flexbox)
* Vanilla JavaScript (DOM Manipulation, WebSocket API, Fetch API)

## 🚀 How to Run Locally

If you'd like to test this project on your local machine, follow these steps:

**1. Clone the repository**
\`\`\`bash
git clone https://github.com/thepremkumar04/real-time-chat-application
cd real-time-chat-application
\`\`\`

**2. Create a virtual environment & install dependencies**
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

**3. Set up Environment Variables**
Create a `.env` file in the root directory and add your secret key:
\`\`\`env
DEBUG=True
SECRET_KEY=your-secure-django-key-here
\`\`\`

**4. Run Database Migrations**
\`\`\`bash
python manage.py migrate
\`\`\`

**5. Start the ASGI Server**
\`\`\`bash
python manage.py runserver
\`\`\`
*Navigate to `http://127.0.0.1:8000` in your browser. Open a second incognito window to log in as a different user and test the real-time chat!*

## 📸 Screenshots
![App Screenshot](images/Login%20Page.png)
![App Screenshot](images/Chat%20interface.png)
![App Screenshot](images/Search%20Bar.png)


---
*Developed by [Premkumar] - [https://www.linkedin.com/in/gudala-premkumar/]*