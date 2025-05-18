from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("runs/classify/train3/weights/best.pt")  # Path to your best weights

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to match training size if needed
    resized = cv2.resize(frame, (224, 224))

    # Run classification
    results = model(resized)

    # Extract top predicted class
    prediction = results[0].probs.top1
    label = model.names[prediction]

    # Draw label on screen
    cv2.putText(frame, f"Prediction: {label}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show webcam
    cv2.imshow("ASL Prediction", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
