from flask import Flask, request, render_template
#from bioinformatics.reverse import reverse_comp  # Import the function
from bioinformatics.scripts import reverse_comp, gc_content, transcription, codon_frequency, translation, hamming, melting_temp, restriction, palindrome, orf_finder, primers, atomic_mass


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

# Tool page for GC content
@app.route('/tools/gc_content', methods=['GET', 'POST'])
def gc_content_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = gc_content(sequence)

    return render_template('gc_content.html', result=result, sequence=sequence)

# Tool page for Transcription
@app.route('/tools/transcription', methods=['GET', 'POST'])
def transcription_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = transcription(sequence)

    return render_template('transcription.html', result=result, sequence=sequence)



# Tool page for Codon Frequency
@app.route('/tools/codon', methods=['GET', 'POST'])
def codon_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = codon_frequency(sequence)

    return render_template('codon.html', result=result, sequence=sequence)

# Tool page for Codon Frequency
@app.route('/tools/translation', methods=['GET', 'POST'])
def translation_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = translation(sequence)

    return render_template('translation.html', result=result, sequence=sequence)


# Tool page for Hamming
@app.route('/tools/hamming', methods=['GET', 'POST'])
def hamming_tool():
    result = None
    sequence1 = ""
    sequence2 = ""

    if request.method == 'POST':
        sequence1 = request.form.get('sequence1', '').upper().strip()
        sequence2 = request.form.get('sequence2', '').upper().strip()

        if sequence1 and sequence2:
            result = hamming(sequence1, sequence2)

    return render_template('hamming.html', result=result, sequence1=sequence1, sequence2=sequence2)

# Tool page for Melting
@app.route('/tools/melting', methods=['GET', 'POST'])
def melting_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = melting_temp(sequence)

    return render_template('melting.html', result=result, sequence=sequence)

# Tool page for Restriction
@app.route('/tools/restriction', methods=['GET', 'POST'])
def restriction_tool():
    result = None
    sequence1 = ""
    sequence2 = ""

    if request.method == 'POST':
        sequence1 = request.form.get('sequence1', '').upper().strip()
        sequence2 = request.form.get('sequence2', '').upper().strip()   #### this is the expected recognition site

        if sequence1 and sequence2:
            result = restriction(sequence1, sequence2)

    return render_template('restriction.html', result=result, sequence1=sequence1, sequence2=sequence2)

# Tool page for Palindromes
@app.route('/tools/palindrome', methods=['GET', 'POST'])
def palindrome_tool():
    result = None
    sequence1 = ""
    sequence2 = ""

    if request.method == 'POST':
        sequence1 = request.form.get('sequence1', '').upper().strip()
        sequence2 = request.form.get('sequence2', '').strip()   #### This is the length of the palindrome

        if sequence1 and sequence2:
            sequence2 = int(sequence2)
            result = palidrome(sequence1, sequence2)

    return render_template('palindrome.html', result=result, sequence1=sequence1, sequence2=sequence2)



# Tool page for ORFS
@app.route('/tools/orfs', methods=['GET', 'POST'])
def orfs_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = orf_finder(sequence)

    return render_template('orfs.html', result=result, sequence=sequence)


# Tool page for Primers
@app.route('/tools/primers', methods=['GET', 'POST'])
def primers_tool():
    result = None
    sequence1 = ""
    sequence2 = ""

    if request.method == 'POST':
        sequence1 = request.form.get('sequence1', '').upper().strip()
        sequence2 = request.form.get('sequence2', '').upper().strip()   ### This is the primer length

        if sequence1 and sequence2:
            result = primers(sequence1, sequence2)

    return render_template('primers.html', result=result, sequence1=sequence1, sequence2=sequence2)



# Tool page for Mass calc
@app.route('/tools/mass', methods=['GET', 'POST'])
def mass_tool():
    result = None
    sequence = ""

    if request.method == 'POST':
        sequence = request.form.get('sequence', '').upper()
        if sequence:
            result = atomic_mass(sequence)

    return render_template('mass.html', result=result, sequence=sequence)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
