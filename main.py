from docx import Document

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

# Save document
file_path = "/mnt/data/Scope_and_Limitations.docx"
doc.save(file_path)

file_path
