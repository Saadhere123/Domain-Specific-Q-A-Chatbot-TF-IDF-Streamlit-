# 🤖 Domain-Specific Q&A Chatbot (TF-IDF + Streamlit)

## 📌 Project Overview

This project is a **retrieval-based AI chatbot** that answers user queries using a predefined dataset.
It uses **TF-IDF Vectorization** and **Cosine Similarity** to find the most relevant question and return its answer.

The chatbot is deployed with an interactive **Streamlit UI**, making it easy to use like a real web application.

---

## 🎯 Objective

* Build a domain-specific Q&A chatbot
* Implement TF-IDF for text vectorization
* Use cosine similarity for matching queries
* Create a user-friendly web interface using Streamlit

---

## 🛠 Tech Stack

* Python 🐍
* pandas
* scikit-learn
* Streamlit
* re (Regular Expressions)

---

## ⚙️ Features

✅ Domain-specific dataset (100+ Q&A pairs)
✅ Text preprocessing (lowercase, cleaning)
✅ TF-IDF with n-grams (improves accuracy)
✅ Cosine similarity matching
✅ Confidence score display
✅ Interactive Streamlit UI
✅ Chat history tracking
✅ Clear chat option

---

## 🧠 How It Works

1. User enters a question in the UI
2. Text is preprocessed (cleaned & normalized)
3. Converted into TF-IDF vector
4. Compared with dataset using cosine similarity
5. Best matching question is selected
6. Corresponding answer is returned

---

## 📂 Project Structure

```
QA_Chatbot/
│── qa_dataset.csv
│── utils.py
│── chatbot.py
│── app.py
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit App

```bash
streamlit run app.py
```

### 3️⃣ Open in Browser

```
http://localhost:8501
```

---

## 💬 Example

**User:** What is AI?
**Bot:** AI stands for Artificial Intelligence.

**User:** explain python
**Bot:** Python is a programming language.

---

## ⚠️ Limitations

❌ This chatbot does NOT generate answers
❌ It cannot handle completely unseen questions

✅ It only retrieves the most relevant answer from the dataset

---

## 🚀 Future Improvements

* Add larger and multi-domain datasets
* Integrate BERT embeddings for semantic search
* Deploy on Streamlit Cloud
* Add voice input/output
* Build admin panel to update Q&A dynamically

---

---

## ⭐ Acknowledgment

This project was developed as part of an **AI Internship Task** to demonstrate understanding of:

* Natural Language Processing (NLP)
* Information Retrieval Systems
* Practical AI application development

---

## 📌 License

This project is open-source and free to use for learning purposes.
