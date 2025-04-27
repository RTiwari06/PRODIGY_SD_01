from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_temperature():
    celsius = fahrenheit = kelvin = None
    if request.method == 'POST':
        temp = float(request.form.get('temperature'))
        unit = request.form.get('unit')

        if unit == 'celsius':
            celsius = temp
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
        elif unit == 'fahrenheit':
            fahrenheit = temp
            celsius = (temp - 32) * 5/9
            kelvin = (temp - 32) * 5/9 + 273.15
        elif unit == 'kelvin':
            kelvin = temp
            celsius = temp - 273.15
            fahrenheit = (temp - 273.15) * 9/5 + 32

    return render_template('index.html', celsius=celsius, fahrenheit=fahrenheit, kelvin=kelvin)

if __name__ == "__main__":
    app.run(debug=True)
