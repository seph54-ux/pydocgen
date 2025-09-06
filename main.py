from flask import Flask, render_template, send_file, redirect, url_for, flash
from docx import Document
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configure to disable browser caching
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

def create_scope_and_limitations_doc():
    """Create the Word document and return the file path"""
    # Create a new Document
    doc = Document()

    # Title
    doc.add_heading('Scope and Limitations', level=1)

    # Scope Section
    doc.add_heading('Scope', level=2)
    doc.add_paragraph(
        "This study focuses on the design, development, and deployment of a Smart Coin-Operated Water Dispenser powered by IoT technology. "
        "The scope of the project includes:"
    )
    doc.add_paragraph(
        "1. Automated Dispensing Mechanism – Development of a coin-based activation system that allows users to select between normal temperature water and chilled water, with accurate dispensing volume per coin inserted.\n"
        "2. IoT Integration – Implementation of a centralized admin dashboard that displays real-time data such as water level, chilled water temperature, and coin box capacity. The dashboard also provides push notifications for system alerts (low water, full coin box, or temperature malfunction).\n"
        "3. User Interface – Provision of a simple and intuitive interface (buttons and display screen) to guide users throughout the process of coin insertion, selection, and water dispensing.\n"
        "4. Safety and Maintenance Features – Real-time monitoring and alert system for operational reliability, including warnings for low water supply and a nearly full coin box, supported by sensors like ultrasonic sensors, thermistors, and load cells.\n"
        "5. Testing and Validation – System calibration for dispensing accuracy, reliability tests of components (ESP32, solenoid valves, pumps, sensors), and evaluation of performance based on user satisfaction, efficiency, and cost-effectiveness."
    )

    # Limitations Section
    doc.add_heading('Limitations', level=2)
    doc.add_paragraph(
        "Despite its capabilities, the study is bounded by the following limitations:"
    )
    doc.add_paragraph(
        "1. Coin-Based Payment Only – The system accepts physical coins as the only form of payment. Other payment modes (e.g., QR code, RFID, or mobile payment) are not included in this prototype.\n"
        "2. Single-Source Input – The machine is designed to operate with a single main water jug/reservoir at a time. It does not automatically refill from external pipelines or other water sources.\n"
        "3. Chilled Water Limitation – Cooling is limited to the use of a chilled storage container, monitored by a thermistor. Advanced cooling systems (e.g., compressor-based refrigeration) are not part of this study.\n"
        "4. Capacity Constraints – The dispensing limit is defined per coin transaction (e.g., up to ₱10 worth of water per dispense). Larger dispensing volumes or bulk transactions are outside the scope.\n"
        "5. Operational Range of Sensors – The accuracy of water level (ultrasonic sensor), coin box weight (load cell), and temperature (thermistor) may vary under real-world conditions such as vibration, uneven coin stacking, or fluctuating room temperature.\n"
        "6. Network Dependency – The IoT dashboard requires a stable internet connection for real-time monitoring. In areas with poor connectivity, remote access and notifications may be delayed or unavailable.\n"
        "7. Prototype Stage – The project is developed as a prototype for academic purposes. Long-term durability, large-scale deployment, and commercial-grade optimization (e.g., energy efficiency, tamper-proof design, water filtration integration) are not fully addressed in this study."
    )

    # Create static directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Save document to static folder so it can be served
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Scope_and_Limitations_{timestamp}.docx"
    file_path = os.path.join('static', filename)
    doc.save(file_path)
    
    return file_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate_document():
    try:
        file_path = create_scope_and_limitations_doc()
        filename = os.path.basename(file_path)
        flash(f'Document "{filename}" generated successfully!', 'success')
        return redirect(url_for('index', download_file=filename))
    except Exception as e:
        flash(f'Error generating document: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join('static', filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True, download_name=filename)
        else:
            flash('File not found!', 'error')
            return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error downloading file: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
