import cv2
import numpy as np

vid_path = "/home/israth/Documents/Code/Python/var-football/footbl_cam-2.mp4"
cap = cv2.VideoCapture(vid_path)

# window settings
cv2.namedWindow("YOLO Output", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("YOLO Output", 1280, 720) 
x, y, w, h = 0, 50, 1920, 1080  # (left, top, width, height)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
g_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    #h_frame, w_frame, _ = frame.shape
    #crop_width = 1514
    #cropped = frame[y:min(y+h, h_frame), w_frame-crop_width:w_frame]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_g = np.array([35, 40, 40])
    u_g = np.array([85, 255, 255])
    mask_1 = cv2.inRange(hsv, l_g, u_g)
    mask_invert_1 = cv2.bitwise_not(mask_1)
    cl_m1 = cv2.morphologyEx(mask_invert_1, cv2.MORPH_OPEN, kernel=kernel)
    m1 = cv2.dilate(cl_m1, kernel=g_kernel, iterations=2)
    #res = cv2.bitwise_and(pic, pic, mask=m1)

    l_f = np.array([49, 90, 180])
    u_f = np.array([61, 189, 255])
    mask_2 = cv2.inRange(hsv, l_f, u_f)
    cl_m2 = cv2.morphologyEx(mask_2, cv2.MORPH_OPEN, kernel=kernel2)
    m2 = cv2.dilate(cl_m2, kernel=g_kernel, iterations=2)

    contours1, _ = cv2.findContours(m1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(m2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours1:
        area = cv2.contourArea(cnt)
        if area < 50:
            continue  # Skip small noise

        if area > 4000:
            continue

        xbox, ybox, wbox, hbox = cv2.boundingRect(cnt)
        aspect_ratio = float(wbox) / hbox

        # Skip overly thin or wide shapes (likely lines or merged blobs)
        if aspect_ratio < 0.2 or aspect_ratio > 2.5:
            continue

        # Optional: Use perimeter to remove odd shapes
        #perimeter = cv2.arcLength(cnt, True)
        #if perimeter < 100:
        #    continue           
        cv2.rectangle(frame, (xbox, ybox), (xbox + wbox, ybox + hbox), (0, 255, 0), 2)

    for cnt in contours2:
        area = cv2.contourArea(cnt)
        #if area < 300:
        #    continue  # Skip small noise

        xbox, ybox, wbox, hbox = cv2.boundingRect(cnt)
        aspect_ratio = float(wbox) / hbox

        # Skip overly thin or wide shapes (likely lines or merged blobs)
        #if aspect_ratio < 0.2 or aspect_ratio > 2.5:
        #    continue

        # Optional: Use perimeter to remove odd shapes
        #perimeter = cv2.arcLength(cnt, True)
        #if perimeter < 100:
        #    continue
            
        cv2.rectangle(frame, (xbox, ybox), (xbox + wbox, ybox + hbox), (0, 255, 0), 2)


    cv2.imshow("YOLO Output", frame)
    #cv2.imshow("YOLO Output", mask)
    #cv2.imshow("YOLO Output", hsv)
    #cv2.imshow("YOLO Output", res)
    #cv2.imshow("YOLO Output", grown)
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()  