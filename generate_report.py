import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

INPUT_FILE = 'weather_data.json'
OUTPUT_FILE = 'weather_report.pdf'

def load_data():
    with open(INPUT_FILE, 'r') as f:
        return json.load(f)

def generate_pdf(data):
    c = canvas.Canvas(OUTPUT_FILE, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, y, "Weather Summary Report")
    y -= 40

    c.setFont("Helvetica", 12)

    for city, info in data.items():
        main = info.get("main", {})
        rain = info.get("rain", {})
        wind = info.get("wind", {})
        clouds = info.get("clouds", {})

        c.drawString(50, y, f"📍 City: {city}")
        y -= 20
        c.drawString(70, y, f"Temperature: {main.get('temp', 0)} °C")
        y -= 20
        c.drawString(70, y, f"Humidity: {main.get('humidity', 0)}%")
        y -= 20
        c.drawString(70, y, f"Rainfall (1h): {rain.get('1h', 0)} mm")
        y -= 20
        c.drawString(70, y, f"Pressure: {main.get('pressure', 0)} hPa")
        y -= 20
        c.drawString(70, y, f"Wind Speed: {wind.get('speed', 0)} m/s")
        y -= 20
        c.drawString(70, y, f"Cloudiness: {clouds.get('all', 0)}%")
        y -= 30

        if y < 100:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)

    c.save()
    print(f"✅ Report saved as '{OUTPUT_FILE}'")

if __name__ == "__main__":
    data = load_data()
    generate_pdf(data)
