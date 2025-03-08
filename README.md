# Traffic Violation Detection System

## Overview
The **Traffic Violation Detection System** is an IoT and ML-based project that detects red light violations using an **ESP32-CAM module** and an **IR sensor**. When a vehicle crosses a red light, the **ESP32-CAM** captures an image and sends it to a **PHP server**. The image is then processed using **OpenCV (cv2)** to extract the vehicle's license plate. The extracted number plate is matched with records in a **MongoDB database**, and if a match is found, a **fine receipt is sent to the offender's email**.

## Features
- Captures an image when a vehicle crosses a red light.
- Sends the image to a **PHP server**.
- Extracts the **license plate** using **OpenCV (cv2)**.
- Matches the extracted plate with a **MongoDB database**.
- Sends an email with the **fine receipt** if a match is found.
- Stores violation records in the **database**.

## Components Used
- **ESP32-CAM Module**
- **IR Sensor**
- **PHP Server** (Handles image storage and database interaction)
- **Python Server** (Processes images and extracts license plates)
- **MongoDB** (Stores vehicle details and violation records)

## Installation & Setup
### 1. Install Required Software
Ensure you have the following installed on your system:
- **XAMPP** (to run the PHP server and MySQL for local database interaction)
- **Python** (for image processing)
- **MongoDB** (for storing vehicle and violation details)
- **Arduino IDE** (for programming ESP32-CAM)

### 2. Setup the PHP Server
1. Install **XAMPP** and start **Apache & MySQL**.
2. Place the PHP files inside `htdocs` (e.g., `C:\xampp\htdocs\TrafficViolation`).
3. Create a database in **MongoDB** for vehicle records.

### 3. Setup the Python Server
1. Install required Python libraries:
   ```sh
   pip install opencv-python numpy pymongo flask requests
   ```
2. Run the Python server before starting anything else:
   ```sh
   python server2.py
   ```

### 4. Upload the Arduino Code to ESP32-CAM
1. Connect ESP32-CAM to your computer via FTDI.
2. Open the Arduino IDE and upload the provided sketch.
3. **Edit the IP address** in the Arduino code to match the connected network (since the project is not hosted online).
4. Once uploaded, restart ESP32-CAM.

### 5. View Captured Images & Violations
1. Ensure the **PHP server** is running.
2. Open a browser and navigate to:
   ```sh
   http://localhost/TrafficViolation/index.php
   ```
3. You should see the captured images and violation details.

## Usage Workflow
1. The **IR sensor** detects when a vehicle crosses the red light.
2. The **ESP32-CAM** captures an image and sends it to the **PHP server**.
3. The **Python server** processes the image, extracts the **number plate**, and checks the **MongoDB database**.
4. If a match is found, a **fine receipt** is sent via email to the vehicle owner.
5. The violation details are stored in the **database** and can be viewed via `index.php`.

## Important Notes
- The **Python server must be started before running the PHP server**.
- The **ESP32-CAM should have the correct IP address** matching the local network.
- MongoDB should be set up correctly with **vehicle data** for proper matching.
- Use `index.php` in the browser to **view captured images and violations**.

## Future Improvements
- Host the project online for remote monitoring.
- Implement **real-time SMS notifications** for violations.
- Enhance **license plate recognition accuracy** with advanced ML models.

## License
This project is open-source and can be modified for educational and research purposes.

---
### Developed by Adnan Ahmad

