from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_value = request.form['value']
        print("input_value in /", input_value)
        return redirect('/result?value=' + input_value)
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    input_value = request.args.get('value')
    if input_value is None:
        return redirect('/')

    labeled_values = [('Value', input_value)]
    return render_template('result.html', labeled_values=labeled_values)


if __name__ == '__main__':
    app.run(debug=True)
