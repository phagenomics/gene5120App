from flask import Flask, request, render_template
from bioinformatics.reverse import reverse_comp  # Import the function

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Tool page for Reverse Complement
@app.route('/tools/reverse_complement', methods=['GET', 'POST'])
def reverse_complement_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = reverse_comp(sequence)

    return render_template('reverse_complement.html', result=result, sequence=sequence)

# Tool page for Reverse Complement
@app.route('/tools/gc_content', methods=['GET', 'POST'])
def gc_content_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = reverse_comp(sequence)

    return render_template('gc_content.html', result=result, sequence=sequence)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
