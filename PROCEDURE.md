# 🚀 MathLab Pro — Setup & Procedure Guide

## 📁 Project Structure
```
mathlab/
├── app.py              ← Flask backend with all 12 API endpoints
├── requirements.txt    ← Python dependencies
├── templates/
│   └── index.html      ← Full frontend (HTML + CSS + JS)
└── static/             ← (optional) extra assets
```

---

## ⚙️ Step-by-Step Setup

### Step 1 — Install Python
Download Python 3.8+ from https://python.org

### Step 2 — Install Flask
```bash
pip install flask
```
Or use the requirements file:
```bash
pip install -r requirements.txt
```

### Step 3 — Run the Server
```bash
cd mathlab
python app.py
```

### Step 4 — Open in Browser
```
http://localhost:5000
```

---

## 🧮 Programs Included

| # | Program              | Input         | Logic                          |
|---|----------------------|---------------|-------------------------------|
| 1 | Odd / Even Checker   | One number    | n % 2 == 0                    |
| 2 | Grade Calculator     | Marks 0–100   | Range-based A+/A/B+/B/C/D/F   |
| 3 | Multiplication Table | Number, limit | n × 1 to n × limit            |
| 4 | Pass / Fail Checker  | CSV scores    | score >= 40 per subject        |
| 5 | Leap Year Detector   | Year          | ÷4 not ÷100 unless ÷400       |
| 6 | Factorial Calculator | n (0–20)      | math.factorial(n)              |
| 7 | Prime Number Checker | Number        | No divisor from 2 to √n        |
| 8 | Fibonacci Sequence   | Count (≤30)   | a,b = b, a+b loop              |
| 9 | BMI Calculator       | Weight, Height| weight / (height_m)²           |
|10 | Simple Interest      | P, R, T       | SI = (P×R×T)/100               |
|11 | Quadratic Solver     | a, b, c       | Discriminant b²-4ac            |
|12 | Temperature Converter| Value, unit   | Formula-based C↔F↔K            |

---

## 🌐 API Reference

All endpoints accept and return JSON.

```
POST /api/odd_even         { "number": 42 }
POST /api/grade            { "marks": 87 }
POST /api/table            { "number": 7, "limit": 12 }
POST /api/pass_fail        { "subjects": [78, 45, 92] }
POST /api/leap_year        { "year": 2024 }
POST /api/factorial        { "number": 7 }
POST /api/prime            { "number": 97 }
POST /api/fibonacci        { "count": 10 }
POST /api/bmi              { "weight": 70, "height": 175 }
POST /api/simple_interest  { "principal": 10000, "rate": 8, "time": 3 }
POST /api/quadratic        { "a": 1, "b": -5, "c": 6 }
POST /api/temperature      { "value": 100, "unit": "C" }
```

---

## 🎨 Tech Stack
- **Backend**: Python 3 + Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Orbitron + Exo 2 (Google Fonts)
- **Animation**: CSS keyframes, Canvas API
- **Styling**: CSS custom properties (dark theme)

---

## 💡 Tips
- Press **Enter** inside any input field to trigger calculation
- Click the **?** button (bottom right) for in-app help
- Correct results trigger a **confetti animation** 🎉
- Hover over any card to see the glowing border animation
