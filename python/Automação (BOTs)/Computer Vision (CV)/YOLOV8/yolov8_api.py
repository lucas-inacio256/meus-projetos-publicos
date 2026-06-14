from ultralytics import YOLO
import torch
import cv2

class YoloAPI():
    
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f'Usando: {self.device}')

        self.model = None

    def load_model(self, model='yolov8s.pt'):
        
        self.model = YOLO(model).to(self.device)
        self.model.fuse()

    def predict(self, frame):
        
        results = self.model(frame, self.device)
        
        return results

    def plot_bboxes(frame, results, confidence=0.75):
        for result in results:
            for box in result.boxes:
                
                try:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                except:
                    continue

                conf = box.conf[0].item()
                
                if conf >= confidence:
                    
                    label = f'{result.names[int(box.cls[0])]} ({conf:.2f})'

                    frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    frame = cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        return frame
