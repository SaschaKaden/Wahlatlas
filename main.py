from util import util
from util import reader
from util.cell import Cell
import requests

cookies = {'PHPSESSID': '41d5jkn0hn5fsm25mn8jut90f3', 'SimpleSAML': '7826ce32eec0f34f8186179b79fb1cb2',
           'SimpleSAMLAuthToken': '_d35fb8d8a02652c56de3538e844e0c20c5b2463ef9'}
grid_size = 250

cells = []
count = 0

bt_obj, extra_obj = util.get_req_objects(grid_size)

lon_range, lat_range = util.generate_ranges(util.get_dresden_coords(), grid_size)
for lon in lon_range:
    print("iteration number: ", count, " of ", len(lon_range))
    count += 1
    for lat in lat_range:
        bt_obj['lon'] = str(lon)
        bt_obj['lat'] = str(lat)
        extra_obj['lon'] = str(lon)
        extra_obj['lat'] = str(lat)

        bt = requests.post('https://gruene.wahlatlas.eu/php/get_results.php', cookies=cookies, data=bt_obj)
        extra = requests.post('https://gruene.wahlatlas.eu/php/get_extra_infos.php', cookies=cookies, json=extra_obj)
        cells.append(reader.create_cell(lon, lat, bt, extra))

    util.write_file("Dresden.json", cells)


cells.clear()
lon_range, lat_range = util.generate_ranges(util.get_leipzig_coords(), grid_size)
for lon in lon_range:
    print("iteration number: ", count, " of ", len(lon_range))
    count += 1
    for lat in lat_range:
        bt_obj['lon'] = str(lon)
        bt_obj['lat'] = str(lat)
        extra_obj['lon'] = str(lon)
        extra_obj['lat'] = str(lat)

        bt = requests.post('https://gruene.wahlatlas.eu/php/get_results.php', cookies=cookies, data=bt_obj)
        extra = requests.post('https://gruene.wahlatlas.eu/php/get_extra_infos.php', cookies=cookies, json=extra_obj)
        cells.append(reader.create_cell(lon, lat, bt, extra))

    util.write_file("Leipzig.json", cells)

