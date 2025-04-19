# Football Player Tracking using OpenCV and Python

This project demonstrates a basic method for tracking football players in a video using **OpenCV** and **Python**. It leverages **color segmentation** in the HSV colour space to identify and track players based on the colours of their kits.

---

## 🎯 Objective

To detect and track football players in video footage using classical computer vision techniques — specifically **HSV filtering** — without relying on deep learning.

---

## 🛠️ Technologies Used

- Python
- OpenCV
- HSV colour space filtering / colour segmentation

---

## 🛠️ Python Libraries Used

- OpenCV
- Numpy

---

## ⚙️ How It Works

1. Convert the video frame from BGR to HSV colour space.
2. Define HSV range(s) for the specific colours of players' kits.
3. Create masks to isolate those colours.
4. Use contours or bounding boxes to detect and track the players.
5. Display tracking overlays on the original video.

---

## ⚠️ Limitations

- **Manual Adjustment**: Parameter must be changed for diffrent clip.
- **Lighting Sensitivity**: HSV filtering can be affected by lighting changes and shadows.
- **Same Kit Colours**: Difficult to differentiate between teams wearing similar colours.
- **No Deep Learning**: No player re-identification or advanced object detection.
- **Camera Angles**: Method may fail if the perspective shifts or the players are too far.

---

## 🚀 Future Improvements

- Integrate YOLO or another object detection model for robust tracking.
- Handle overlapping players with better segmentation or tracking algorithms.

---

## 📸 Sample Output

![Demo pic](/home/israth/Documents/Code/Python/var-football/sample.png)

---

## 🧠 Author

[isrxth](https://github.com/isrxth)


