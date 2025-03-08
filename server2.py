import os
import time
import cv2
import easyocr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pymongo import MongoClient
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


detected_plates_folder = "detected_plates"
os.makedirs(detected_plates_folder, exist_ok=True)

# MongoDB connection
client = MongoClient("MONGO URL")  # Update with your DB URI
db = client["traffic_violation_db"]  # Database name
collection = db["vehicle_owners"]  # Collection name

def extract_number_plate(image_path):
    reader = easyocr.Reader(['en'])
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = reader.readtext(gray)
    
    plate_number = ""
    for (bbox, text, prob) in results:
        if len(text) > 4: 
            plate_number = text
            break
    
    return plate_number

def check_plate_and_notify(plate_number):
    owner_data = collection.find_one({"plate_number": plate_number})
    
    if owner_data:
        owner_email = owner_data["email"]
        owner_name = owner_data["name"]
        
        print(f"Owner found: {owner_name}, Sending email to: {owner_email}")
        send_email(owner_email, plate_number)
    else:
        print("Number plate not found in database.")

def send_email(to_email, plate_number):
    sender_email = "sender@email.com"  # Replace with your Gmail
    sender_password = "password"  # Replace with the App Password

    subject = "Traffic Violation Penalty Notice"
    body = f"""
    Dear Vehicle Owner,

    Your vehicle with plate number {plate_number} has violated a traffic rule. 
    A penalty receipt has been generated. Please check your account for details.

    Regards,
    Traffic Department
    """

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print(f"✅ Email sent successfully to {to_email}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            time.sleep(1)  # Allow file to be fully saved
            plate_number = extract_number_plate(event.src_path)
            if plate_number:
                print(f"Extracted Plate Number: {plate_number}")
                with open(os.path.join(detected_plates_folder, "plates.txt"), "a") as f:
                    f.write(f"{plate_number}\n")
                check_plate_and_notify(plate_number)
            else:
                print("No valid number plate detected.")

if __name__ == "__main__":
    folder_to_watch = "captured_images"
    os.makedirs(folder_to_watch, exist_ok=True)
    
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()
    
    print(f"Monitoring folder: {folder_to_watch} for new images...")
    
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()