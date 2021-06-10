from util import util
from util import reader
from util.cell import Cell
import jsonpickle
import requests

cookies = {'PHPSESSID': '41d5jkn0hn5fsm25mn8jut90f3', 'SimpleSAML': '7826ce32eec0f34f8186179b79fb1cb2',
           'SimpleSAMLAuthToken': '_d35fb8d8a02652c56de3538e844e0c20c5b2463ef9'}
grid_size = 500

cells = []
count = 0

lon_range, lat_range = util.generate_ranges(util.get_leipzig_coords(), grid_size)
bt_obj, lt_obj, extra_obj = util.get_req_objects(grid_size)

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
        extra_obj['lon'] = lon_val
        extra_obj['lat'] = lat_val

        bt = requests.post('https://gruene.wahlatlas.eu/php/get_results.php', cookies=cookies, data=bt_obj)
        lt = requests.post('https://gruene.wahlatlas.eu/php/get_results.php', cookies=cookies, data=lt_obj)
        extra = requests.post('https://gruene.wahlatlas.eu/php/get_extra_infos.php', cookies=cookies, json=extra_obj)

        cells.append(reader.create_cell(lon, lat, bt, lt, extra))

    print(len(cells))
    jsonStr = jsonpickle.encode(cells)
    text_file = open("Output.json", "w")
    text_file.write(jsonStr)
    text_file.close()
