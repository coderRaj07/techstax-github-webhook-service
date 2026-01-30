# 🚀 TechStax GitHub Webhook Service

A **Flask-based GitHub webhook receiver** that captures repository activity events and displays them in near real-time via a polling UI.

---

## 🌐 Live Demo

* **Deployed Application:**
  👉 [https://techstax-github-webhook-service.onrender.com/](https://techstax-github-webhook-service.onrender.com/)

* **Event Response:**
  💬 [https://techstax-github-webhook-service.onrender.com/events](https://techstax-github-webhook-service.onrender.com/events)

* **Demo Video Walkthrough:**
  🎥 [https://youtu.be/6YqGzMOcYlE](https://youtu.be/6YqGzMOcYlE)

---

## ✨ Features

* Listens to GitHub webhook events:

  * **Push**
  * **Pull Request**
  * **Merge**
* Stores minimal event metadata in **MongoDB**
* Frontend UI polls the backend every **15 seconds**
* Displays recent GitHub activity in a clean, readable format
* Deployed and publicly accessible

---

## 🛠 Tech Stack

* **Backend:** Flask (Python)
* **Database:** MongoDB
* **Frontend:** HTML, CSS, JavaScript
* **Deployment:** Render
* **Version Control:** GitHub Webhooks

---

## 📦 Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/coderRaj07/techstax-github-webhook-service/
cd techstax-github-webhook-service
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure MongoDB

Make sure MongoDB is running locally **or** provide a MongoDB connection string via environment variable:

```bash
export MONGO_URI=mongodb://localhost:27017/github_webhooks
```

### 4️⃣ Start the application

```bash
python app.py
```

The app will start on:

```
http://127.0.0.1:5000
```

---

## 🔄 How It Works

1. GitHub sends webhook events (push, pull request, merge)
2. Flask backend receives and processes the payload
3. Minimal event data is stored in MongoDB
4. UI polls the backend every 15 seconds
5. Recent events are displayed to the user

---

## 📌 Notes

* This project is built as a **technical assessment/demo**
* Designed to be lightweight, scalable, and easy to extend
* Can be enhanced further using WebSockets instead of polling


Just say the word 👌
