# ♟️ Chess Pieces Info API

A simple FastAPI project that provides information and images for the six standard chess pieces.

---

## 🚀 Endpoints

### `GET /`
- Returns a short description of the API.

### `GET /pieces`
- Returns a list of all available chess pieces:
  ```
  [ "pawn", "bishop", "knight", "rook", "queen", "king" ]
  ```

### `GET /pieces/{piece_name}`
- Returns a short description of the selected piece.

#### Example:
```
GET /pieces/rook
→ "Moves straight: horizontally or vertically"
```

### `GET /pieces/{piece_name}/image`
- Returns the image of the selected piece as a `.png` file.

---

## 📁 Folder Structure

```
.
├── main.py            # FastAPI application
├── images/            # Folder containing images of each chess piece
│   ├── king.png
│   ├── queen.png
│   └── ...
└── README.md
```

Make sure your `images/` folder contains **PNG files** with the exact names:
```
king.png, queen.png, rook.png, bishop.png, knight.png, pawn.png
```

---

## 🛠️ Requirements

Install dependencies using `pip`:

```bash
pip install fastapi uvicorn opencv-python
```

---

## 🧪 Run the App

```bash
uvicorn main:app --reload
```

Then open your browser or Postman:
```
http://127.0.0.1:8000
```

---

## 📷 Example

Access image of the knight:
```
http://127.0.0.1:8000/pieces/knight/image
```

---

## 📌 Notes

- If an invalid piece name is provided, the API returns a `400 Bad Request`.
- If the image file is missing, a `404 Not Found` error is returned.

---

## 👨‍💻 Author

Developed by Moein Moatali – 2025