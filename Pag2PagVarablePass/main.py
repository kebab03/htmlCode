from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def perform_algebraic_operation(value):
    # Perform your algebraic operation here
    result = value * 2
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_value = int(request.form['value'])
        result = perform_algebraic_operation(input_value)
        return redirect(url_for('result', result=result))
    return render_template('index.html')

@app.route('/result/<result>')
def result(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
