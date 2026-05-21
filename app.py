from flask import Flask, render_template, request, jsonify
import math
import json

app = Flask(__name__)

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

# ─── API Endpoints ────────────────────────────────────────────────────────────

@app.route('/api/odd_even', methods=['POST'])
def odd_even():
    data = request.json
    n = int(data['number'])
    result = "Even ✨" if n % 2 == 0 else "Odd 🔥"
    color = "#00f5ff" if n % 2 == 0 else "#ff6b35"
    return jsonify({'result': result, 'color': color, 'number': n})

@app.route('/api/grade', methods=['POST'])
def grade():
    data = request.json
    marks = float(data['marks'])
    if marks >= 90:   grade, gpa, color = "A+ 🏆", "4.0", "#ffd700"
    elif marks >= 80: grade, gpa, color = "A 🌟", "3.7", "#00ff88"
    elif marks >= 70: grade, gpa, color = "B+ 💪", "3.3", "#00f5ff"
    elif marks >= 60: grade, gpa, color = "B 👍", "3.0", "#7b68ee"
    elif marks >= 50: grade, gpa, color = "C 📚", "2.0", "#ffa500"
    elif marks >= 40: grade, gpa, color = "D ⚠️", "1.0", "#ff6b35"
    else:             grade, gpa, color = "F ❌", "0.0", "#ff4757"
    status = "PASS 🎉" if marks >= 40 else "FAIL 💔"
    return jsonify({'grade': grade, 'gpa': gpa, 'status': status, 'marks': marks, 'color': color})

@app.route('/api/table', methods=['POST'])
def table():
    data = request.json
    n = int(data['number'])
    limit = int(data.get('limit', 12))
    rows = [{'i': i, 'result': n * i} for i in range(1, limit + 1)]
    return jsonify({'number': n, 'rows': rows})

@app.route('/api/pass_fail', methods=['POST'])
def pass_fail():
    data = request.json
    subjects = data['subjects']
    scores = [float(s) for s in subjects]
    avg = sum(scores) / len(scores)
    passed = sum(1 for s in scores if s >= 40)
    failed = len(scores) - passed
    overall = "PASS 🎉" if failed == 0 else "FAIL 💔"
    color = "#00ff88" if failed == 0 else "#ff4757"
    return jsonify({'average': round(avg, 2), 'passed': passed, 'failed': failed,
                    'overall': overall, 'color': color, 'scores': scores})

@app.route('/api/leap_year', methods=['POST'])
def leap_year():
    data = request.json
    year = int(data['year'])
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    result = f"🌿 {year} IS a Leap Year!" if is_leap else f"🍂 {year} is NOT a Leap Year"
    color = "#00ff88" if is_leap else "#ff6b35"
    days = 366 if is_leap else 365
    return jsonify({'result': result, 'is_leap': is_leap, 'color': color, 'days': days, 'year': year})

@app.route('/api/factorial', methods=['POST'])
def factorial():
    data = request.json
    n = int(data['number'])
    if n < 0:   return jsonify({'error': 'Negative numbers not allowed!'})
    if n > 20:  return jsonify({'error': 'Number too large (max 20)!'})
    result = math.factorial(n)
    steps = " × ".join(str(i) for i in range(n, 0, -1)) or "1"
    return jsonify({'result': result, 'steps': steps, 'number': n})

@app.route('/api/prime', methods=['POST'])
def prime():
    data = request.json
    n = int(data['number'])
    if n < 2:
        return jsonify({'is_prime': False, 'result': f'{n} is NOT Prime ❌', 'color': '#ff4757'})
    is_p = all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
    result = f"✨ {n} IS a Prime Number!" if is_p else f"❌ {n} is NOT Prime"
    color = "#ffd700" if is_p else "#ff4757"
    return jsonify({'is_prime': is_p, 'result': result, 'color': color, 'number': n})

@app.route('/api/fibonacci', methods=['POST'])
def fibonacci():
    data = request.json
    n = int(data['count'])
    if n > 30: return jsonify({'error': 'Max 30 terms!'})
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return jsonify({'sequence': seq, 'count': n, 'last': seq[-1] if seq else 0})

@app.route('/api/bmi', methods=['POST'])
def bmi():
    data = request.json
    weight = float(data['weight'])
    height = float(data['height']) / 100  # cm to m
    bmi_val = round(weight / (height ** 2), 2)
    if bmi_val < 18.5:   cat, color = "Underweight 🍃", "#00f5ff"
    elif bmi_val < 25:   cat, color = "Normal Weight ✅", "#00ff88"
    elif bmi_val < 30:   cat, color = "Overweight ⚠️", "#ffa500"
    else:                cat, color = "Obese 🚨", "#ff4757"
    return jsonify({'bmi': bmi_val, 'category': cat, 'color': color})

@app.route('/api/simple_interest', methods=['POST'])
def simple_interest():
    data = request.json
    p = float(data['principal'])
    r = float(data['rate'])
    t = float(data['time'])
    si = round((p * r * t) / 100, 2)
    total = round(p + si, 2)
    return jsonify({'si': si, 'total': total, 'principal': p, 'rate': r, 'time': t})

@app.route('/api/quadratic', methods=['POST'])
def quadratic():
    data = request.json
    a, b, c = float(data['a']), float(data['b']), float(data['c'])
    disc = b**2 - 4*a*c
    if disc > 0:
        x1 = round((-b + math.sqrt(disc)) / (2*a), 4)
        x2 = round((-b - math.sqrt(disc)) / (2*a), 4)
        result = f"Two real roots: x₁ = {x1}, x₂ = {x2}"
        color = "#00ff88"
    elif disc == 0:
        x = round(-b / (2*a), 4)
        result = f"One root: x = {x}"
        color = "#ffd700"
    else:
        real = round(-b / (2*a), 4)
        imag = round(math.sqrt(-disc) / (2*a), 4)
        result = f"Complex roots: {real} ± {imag}i"
        color = "#ff6b35"
    return jsonify({'result': result, 'discriminant': disc, 'color': color})

@app.route('/api/temperature', methods=['POST'])
def temperature():
    data = request.json
    value = float(data['value'])
    unit = data['unit']
    results = {}
    if unit == 'C':
        results = {'C': value, 'F': round(value * 9/5 + 32, 2), 'K': round(value + 273.15, 2)}
    elif unit == 'F':
        c = (value - 32) * 5/9
        results = {'C': round(c, 2), 'F': value, 'K': round(c + 273.15, 2)}
    else:
        c = value - 273.15
        results = {'C': round(c, 2), 'F': round(c * 9/5 + 32, 2), 'K': value}
    return jsonify({'results': results, 'from_unit': unit})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
