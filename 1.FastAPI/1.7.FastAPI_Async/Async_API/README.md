# 🧩 Multi API Async Project

This project shows how to work with **multiple APIs in Python** using asynchronous functions (`asyncio`).
It connects to:

1. [Rhyming.ir API](https://rhyming.ir/) – for finding Persian rhymes.
2. [Iran Locations API](https://iran-locations-api.ir/) – for getting states and cities in Iran.

---

## 🚀 Features

- Find Persian rhymes for any word.
- Get all Iranian states.
- Get city or state details (name, latitude, longitude).
- Easy `.env` setup for API keys.
- Uses `asyncio.gather()` for concurrent API calls.

---

## 📦 Installation

Install requirements before running:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```bash
API_KEY_RHYME_FINDER=your_api_key_here
```

> 🔑 Get your free API key from [https://rhyming.ir/](https://rhyming.ir/).

---

## ▶️ Run the Script

Run the project with Python 3.11+:

```bash
python main.py
```

You can edit `main()` to change test values:

```python
await asyncio.gather(
    rhyme_finder("جان"),
    get_states(),
    get_cities(1)
)
```

---

## 🧠 Code Overview

### rhyme_finder(word)
Finds rhyming words using **rhyming.ir API**.

### get_states()
Fetches and prints all Iranian states.

### get_cities(state_id)
Gets and prints details of one state.

### main()
Runs all three functions together using `asyncio.gather()`.

---

## 📁 Project Structure

```
📦 Multi_API_Async_Project
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🧰 Example Output

```
{'word': 'جان', 'rhymes': ['مان', 'توان', 'نشان', ...]}
{'id': 1, 'name': 'آذربایجان شرقی', ...}
name: آذربایجان شرقی
latitude: 37.9035733
longitude: 46.2682109
```

---

## ⚠️ Notes

- This version uses **requests** inside async functions for simplicity.
  For better performance, use **aiohttp**.
- Internet connection is required for API calls.

---

## 📜 License

Released under the **MIT License**.

---

## 💡 Author

**Moein Moatali**  
📍 Mashhad, Iran  
💻 Computer Engineering Student  
📧 [GitHub Profile](https://github.com/Moein-Moatali-2006)
