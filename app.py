from flask import Flask, render_template, request

app = Flask(__name__)

def convert_temperature(value, unit):
    results = {}
    if unit == "celsius":
        results["Fahrenheit"] = (value * 9/5) + 32
        results["Kelvin"] = value + 273.15
    elif unit == "fahrenheit":
        celsius = (value - 32) * 5/9
        results["Celsius"] = celsius
        results["Kelvin"] = celsius + 273.15
    elif unit == "kelvin":
        celsius = value - 273.15
        results["Celsius"] = celsius
        results["Fahrenheit"] = (celsius * 9/5) + 32
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    converted = None
    if request.method == "POST":
        try:
            temp_value = float(request.form["temperature"])
            unit = request.form["unit"].lower()
            converted = convert_temperature(temp_value, unit)
        except ValueError:
            converted = {"Error": "Invalid input. Please enter a valid number."}
    return render_template("index.html", converted=converted)

if __name__ == "__main__":
    app.run(debug=True)
