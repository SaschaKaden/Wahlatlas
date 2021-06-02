from enum import Enum
import pyautogui


def scraping_page(x_start, x_end, y_start, y_end, count):
    for y in range(y_start, y_end, 40):
        for x in range(x_start, x_end, 40):  # start by 320 or 80
            pyautogui.click(x, y)
            pyautogui.hotkey('ctrl', 's')
            pyautogui.typewrite(str(count))
            count += 1
            pyautogui.press('enter')
    return count


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


def identify_sinus(text):
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


def read_pixel(text):
    if not text or text == '':
        return 0

    try:
        return float(text)
    except:
        print("error")
        return 0


def read_potential(text):
    if not text or text == '':
        return 0

    try:
        return int(str(int(text))[:2])
    except:
        print("error")
        return 0
