import cv2
import imutils
import pytesseract
from four_point import four_point_transform


def scandoc(filename):
    image = cv2.imread(filename)
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    # resizing
    image = imutils.resize(image, height=500)
    # grayscale

    img = cv2.resize(image, (500, 700),
                     interpolation=cv2.INTER_NEAREST)
    cv2.imshow('normal', img)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smooth = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)

    # finding the contours

    cnts = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if (len(approx) == 4):
            screenCnt = approx
            break

    # bird eye view

    warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    (thresh, BW) = cv2.threshold(warped, 130, 255, cv2.THRESH_BINARY)

    # cv2.imshow("bird", BW)

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = BW

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    con = "OEM_TESSERACT_CUBE_COMBINED"
    boxes = pytesseract.image_to_data(img, lang="k_badini", config=con)
    y1 = 0
    tw = 0
    c = 1
    for a, b in enumerate(boxes.splitlines()):
        if a != 0:
            b = b.split()
            if len(b) == 12:

                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                if h > 20:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (50, 50, 255), 2)

                    if abs(y - y1) < 40:
                        print(b[11], end=' ')
                        c = c + 1
                        tw = tw + w

                    elif abs(y - y1) > 40:
                        tw = tw + w
                        # cv2.rectangle(img, (x-tw-(c*20) , y ), (x + w, y + h), (50, 255, 50), 2)
                        print("\n")
                        print(b[11], end=' ')
                        tw = w
                    y1 = y

    img = cv2.resize(img, (500, 700),interpolation=cv2.INTER_NEAREST)
    print("\n")
    #cv2.imshow('kurdish text', img)
    gray = cv2.resize(gray, (500, 700), interpolation=cv2.INTER_NEAREST)
    #cv2.imshow('kurdish gray', gray)
    edged = cv2.resize(edged, (500, 700), interpolation=cv2.INTER_NEAREST)
    #cv2.imshow('kurdish edge', edged)
    warped = cv2.resize(warped, (500, 700), interpolation=cv2.INTER_NEAREST)
    #cv2.imshow('kurdish warped', warped)
    BW = cv2.resize(BW, (500, 700), interpolation=cv2.INTER_NEAREST)
    cv2.imshow('kurdish BW', BW)
    cv2.waitKey(0)

    cv2.waitKey(0)

