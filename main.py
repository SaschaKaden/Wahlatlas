from util import reader
from util import util
from util.cell import Cell
import jsonpickle
import pyautogui
from bs4 import BeautifulSoup
import glob

show_mouse_pos = False
through_atlas = False
read_htmls = True

if __name__ == "__main__":
    print("Datei wurde direkt aufgerufen und die Main wird ausgeführt")
else:
    print("Datei wurde als Modul aufgerufen")

if show_mouse_pos:
    pos = pyautogui.position()
    while(True):
        new_pos = pyautogui.position()
        if new_pos != pos:
            print(new_pos)
        pos = new_pos

if through_atlas:
    count = 0
    x_start = 80
    x_end = 1610
    y_start = 110
    y_end = 200  # 1080
    pyautogui.PAUSE = 0.8

    count = reader.scraping_page(x_start, x_end, y_start, y_end, count)
    pyautogui.click(x_end, y_end)
    pyautogui.dragTo(x_start, y_end, 2, button='left')
    count = reader.scraping_page(x_start, x_end, y_start, y_end, count)
    pyautogui.click(x_start, y_end)
    pyautogui.dragTo(x_start, y_start, 2, button='left')
    count = reader.scraping_page(x_start, x_end, y_start, y_end, count)
    pyautogui.click(x_start, y_start)
    pyautogui.dragTo(x_end, y_start, 2, button='left')
    count = reader.scraping_page(x_start, x_end, y_start, y_end, count)

if read_htmls:
    cells = []
    filenames = glob.glob("C:/Users/sascha/Downloads/wahlatlas/*.html")
    for filename in filenames:
        html_file = open(filename, "r")
        html_data = html_file.read()
        html_file.close()

        soup = BeautifulSoup(html_data, 'html.parser')
        pixel_span = soup.find("span", id="hoverWahlberechtigtePixel")
        potential_span = soup.find("span", id="hoverPotentialScore21wk")
        sinus_span = soup.find("span", id="hoverPotentialSinus")
        id_span = soup.find("span", id="quelle")
        table = soup.find("table", id="partiesTable")
        if pixel_span.text != "":
            for row in table.findAll('tr'):
                td_tags = row.find_all('td')
                if len(td_tags) > 0:
                    if "GR" in td_tags[0].get('title'):
                        gruene_pixel = td_tags[1].contents[1]

        if id_span is None:
            continue
        cell = Cell(id_span.string[11:])
        cell.x = float(id_span.string.split("E", 1)[1])  # E is x
        cell.y = float(id_span.string.split("N", 1)[1].split("E", 1)[0])  # N is y

        if pixel_span.string is None or len(pixel_span.string) == 0:
            cells.append(cell)
            continue

        cell.pixel = float(pixel_span.string[35:])
        cell.sinus = reader.identify_sinus(sinus_span.string)
        cell.potential = float(potential_span.string[30:].replace(',', '.'))
        cells.append(cell)

    jsonStr = jsonpickle.encode(cells)
    text_file = open("Output.json", "w")
    text_file.write(jsonStr)
    text_file.close()
    print(jsonStr)



