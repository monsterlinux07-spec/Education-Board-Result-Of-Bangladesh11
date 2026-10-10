from flask import Flask, render_template, request

app = Flask(__name__)

# রেজাল্ট ও ডকুমেন্টের ডাটাবেজ
results_db = {
    "325531": {
        "reg": "1310384293/2019-20",
        "exam": "HSC",
        "year": "2021",
        "board": "Dhaka",
        "documents": [
            {"title": "HSC Academic Certificate", "file": "certificate.png"},
            {"title": "HSC Academic Marksheet", "file": "marksheet.png"}
        ]
    },
    "387889": {
        "reg": "1610597071/2016",
        "exam": "JSC",
        "year": "2016",
        "board": "Dhaka",
        "documents": [
            {"title": "JSC Academic Certificate", "file": "jsc_certificate.png"},
            {"title": "JSC Academic Marksheet", "file": "jsc_marksheet.png"}
        ]
    },
    "325532": {
        "reg": "1310384294/2019-20",
        "exam": "HSC",
        "year": "2021",
        "board": "Dhaka",
        "documents": [
            {"title": "HSC Academic Certificate", "file": "certificate_anzuman.png"},
            {"title": "HSC Academic Marksheet", "file": "marksheet_anzuman.png"}
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        roll = request.form.get('roll', '').strip()
        reg = request.form.get('reg', '').strip()
    else:
        roll = request.args.get('roll', '').strip()
        reg = request.args.get('reg', '').strip()
    
    student_data = None
    
    # ইনপুট করা রোল অনুযায়ী ডাটা খোঁজা
    if roll in results_db:
        student_data = results_db[roll]

    return render_template('result.html', roll=roll, reg=reg, student=student_data)

if __name__ == '__main__':
    app.run(debug=True)
