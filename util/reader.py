import numpy as np
import cv2
from PIL import ImageGrab
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from enum import Enum



class SinusType(Enum):
    UNDEFINED = 0
    KET = "KET"  # Konservativ-Etablierte
    LIB = "LIB"  # Liberal-Intellektuelle
    PER = "PER"  # Performer
    EPE = "EPE"  # Expeditive
    PRA = "PRA"  # Adaptiv-Pragmatische
    SQK = "SQK"  # Sozialökologische
    PRE = "PRE"  # Prekäre
    BUM = "BUM"  # Bürgerliche Mitte
    TRA = "TRA"  # Traditionelle
    HED = "HED"  # Hedonisten


def read_sinus():
    frame = np.array(ImageGrab.grab(bbox=(1657, 360, 1907, 400)).convert('RGB'))
    # cv2.imshow("frame", frame)
    # cv2.waitKey(15)
    text = pytesseract.image_to_string(frame).lower()

    if "konservativ" in text:
        return SinusType.KET
    elif "liberal" in text:
        return SinusType.LIB
    elif "performer" in text:
        return SinusType.PER
    elif "expeditive" in text:
        return SinusType.EPE
    elif "adaptiv" in text:
        return SinusType.PRA
    elif "sozial" in text:
        return SinusType.SQK
    elif "prekär" in text:
        return SinusType.PRE
    elif "mitte" in text:
        return SinusType.BUM
    elif "trad" in text:
        return SinusType.TRA
    elif "hedonist" in text:
        return SinusType.HED
    else:
        return SinusType.UNDEFINED


def read_pixel():
    # check that pixel exists
    frame = np.array(ImageGrab.grab(bbox=(1780, 195, 1830, 210)).convert('RGB'))
    cv2.imshow("frame", frame)
    cv2.waitKey(15)
    text = pytesseract.image_to_string(frame, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    text = text.replace("\f", "")
    if not text or "f" in text:
        return 0

    frame2 = np.array(ImageGrab.grab(bbox=(1830, 325, 1900, 345)).convert('RGB'))
    cv2.imshow("frame", frame2)
    cv2.waitKey(15)
    text = pytesseract.image_to_string(frame2, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    if not text:
        return 0

    return float(text)


def read_potential():
    frame = np.array(ImageGrab.grab(bbox=(1818, 348, 1855, 360)).convert('RGB'))
    # cv2.imshow("frame", frame)
    # cv2.waitKey(15)
    text = pytesseract.image_to_string(frame, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    if not text:
        return 0

    return int(str(int(text))[:2])
