import cv2

fingertips = [(100, 200), (300, 150), (250, 350), (400, 300), (150, 400)]

screen_height = 1080
screen_width = 1920

finger_fold_status = []

for fingertip in fingertips:
    x = fingertip[0]
    y = fingertip[1]

    x = int(x * screen_width)
    y = int(y * screen_height)

    cv2.circle(image, (x, y), 10, (255, 0, 0), -1)

    if x < previous_x:
        cv2.circle(image, (x, y), 10, (0, 255, 0), -1)
        finger_fold_status.append(True)
    else:
        finger_fold_status.append(False)

    previous_x = x

if all(finger_fold_status):
    if fingertips[0][1] < fingertips[1][1]:
        print("LIKE")
        cv2.putText(image, "LIKE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        print("DISLIKE")
        cv2.putText(image, "DISLIKE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Fingertips", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
