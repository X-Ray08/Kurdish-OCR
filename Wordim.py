import cv2
import pytesseract


def imscn(filename):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(filename)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    con = "OEM_TESSERACT_CUBE_COMBINED"
    boxes = pytesseract.image_to_data(img, lang="k_badini", config=con)
    y1 = 0
    tw = 0
    c = 1

    with open('OCR_Result.txt.txt', 'w') as f:
        f.write('Create a new text file!')
    for a, b in enumerate(boxes.splitlines()):
        if a != 0:
            b = b.split()
            if len(b) == 12:

                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                if h > 20:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (50, 50, 255), 2)

                    if abs(y - y1) < 40:
                        print(b[11], end=' ')
                        #f.write('hi')
                        c = c + 1
                        tw = tw + w

                    elif abs(y - y1) > 40:
                        # tw = tw + w
                        # cv2.rectangle(img, (x-tw-(c*20) , y ), (x + w, y + h), (50, 255, 50), 2)
                        print("\n")
                        # file.write("\n")
                        print(b[11], end=' ')
                        # file.write(b[11], end=' ')
                        tw = w
                    y1 = y
    print("\n")
    cv2.imshow('kurdish text', img)
    cv2.waitKey(0)
