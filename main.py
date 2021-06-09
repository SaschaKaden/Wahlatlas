from util import reader
from util.cell import Cell
import jsonpickle
from bs4 import BeautifulSoup
import glob
import requests
import numpy as np
import time


read_htmls = False
cookies = {'PHPSESSID': '41d5jkn0hn5fsm25mn8jut90f3', 'SimpleSAML': 'a765cf9dcf00ff6629d93a0f0e3ba238', 'SimpleSAMLAuthToken': '_0898fdba20d9f49ec061dfc3a85ba5bd2c1a7b23ad'}
lon_start = 1316856.9993981898
lat_start = 6457531.171883571
lon_end = 1669386.9500434147
lat_end = 6742784.414390394

# lon_start = 1432201.0657676156
# lat_start = 6587513.529834197
# lon_end = 1438328.6526260807
# lat_end = 6593988.164781701

cells = []
lon_range = np.arange(lon_start, lon_end, 1000).tolist()
lat_range = np.arange(lat_start, lat_end, 1000).tolist()
count = 0

lt_obj = {'lon': 0,
         'lat': 0,
         'relation': 'grid.grid100m',
         'grid': 'grid100m',
         'election_m': 'statistik.d_lt_sn_19_grid100m',
         'election_o': 'statistik.d_lt_sn_19'}
bt_obj = {'lon': 0,
          'lat': 0,
          'relation': 'grid.grid100m',
          'grid': 'grid100m',
          'election_m': 'statistik.d_bt_de_17_grid100m',
          'election_o': 'statistik.d_bt_de_17'}

for lon in lon_range:
    print("iteration number: ", count, " of ", len(lon_range))
    count += 1
    for lat in lat_range:
        lon_val = str(lon)
        lat_val = str(lat)
        lt_obj['lon'] = lon_val
        lt_obj['lat'] = lat_val
        bt_obj['lon'] = lon_val
        bt_obj['lat'] = lat_val

        bt = requests.post('https://gruene.wahlatlas.eu/php/get_results.php', cookies=cookies, data=bt_obj)
        lt = requests.post('https://gruene.wahlatlas.eu/php/get_results.php', cookies=cookies, data=lt_obj)
        extra = requests.post('https://gruene.wahlatlas.eu/php/get_extra_infos.php', cookies=cookies, json={'lon': lon, 'lat': lat, 'relation': 'grid.grid100m'})

        cell = Cell(lon, lat)
        if bt is not None:
            try:
                bt_json = bt.json()
                cell.gru_bt = bt_json['p_zs_gru_percent']
                pixel = bt_json['wahlberechtigte']
                if pixel is not None:
                    cell.pixel = pixel
            except:
                pass
        if lt is not None:
            try:
                cell.gru_lt = lt.json()['p_zs_gru_percent']
            except:
                pass
        if extra is not None:
            try:
                extra_json = extra.json()
                sinus = extra_json['sinus'][0].get('sinus_sn')
                if sinus is not None:
                    cell.sinus = sinus
                potential = extra_json['pot_21'][0].get('bt_21_potential')
                if potential is not None:
                    cell.potential = potential
                potential_scale = extra_json['pot_21'][0].get('bt_21_pot_scale')
                if potential_scale is not None:
                    cell.potential_scale = potential_scale
            except:
                pass
        cells.append(cell)

    print(len(cells))
    jsonStr = jsonpickle.encode(cells)
    text_file = open("Output.json", "w")
    text_file.write(jsonStr)
    text_file.close()



