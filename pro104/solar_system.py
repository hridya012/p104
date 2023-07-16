import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
            img,
            "Sun",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color=(255,0,0),
            )

cv2.putText(
            img,
            "Mercury",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.25,
            color=(0,0,255),
            )

cv2.putText(
            img,
            "Venus",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.25,
            color=(0,0,255),
            )

cv2.putText(
            img,
            "Earth",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.25,
            color=(0,0,255),
            )

cv2.putText(
            img,
            "mars",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.25,
            color=(0,0,255),
            )

cv2.putText(
            img,
            "Jupitet",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.25,
            color=(0,0,255),
            )

cv2.putText(
            img,
            "Saturn",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.25,
            color=(0,0,255),
            )

cv2.putText(
            img,
            "Uranus",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.25,
            color=(0,0,255),
            )

cv2.putText(
            img,
            "Neptune",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.25,
            color=(0,0,255),
            )

cv2.imshow("output",img)

cv2.waitKey(0)

