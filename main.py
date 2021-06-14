from util import util
from util import reader
from util.cell import Cell
import requests


cookies = {'PHPSESSID': 'rgvmdhbkctthhrjmat9i9votjd', 'SimpleSAML': 'e588cb50c555f3028f222d7f1c14d65a',
           'SimpleSAMLAuthToken': '_962023b7a721c684e722d00ba3eb6dcc72d6fa8bf4'}
grid_size = 250
bt_obj, extra_obj = util.get_req_objects(grid_size)


def collect(name, lon_lat_values):
    cells = []
    count = 0
    lon_range, lat_range = util.generate_ranges(lon_lat_values, grid_size)

    print(name)
    for lon in lon_range:
        print("iteration number: ", count, " of ", len(lon_range), " |  current cell size: ", len(cells))
        count += 1
        for lat in lat_range:
            bt_obj['lon'] = str(lon)
            bt_obj['lat'] = str(lat)
            extra_obj['lon'] = str(lon)
            extra_obj['lat'] = str(lat)

            bt = requests.post('https://gruene.wahlatlas.eu/php/get_results.php', cookies=cookies, data=bt_obj)
            extra = requests.post('https://gruene.wahlatlas.eu/php/get_extra_infos.php', cookies=cookies,
                                  json=extra_obj)
            cells.append(reader.create_cell(lon, lat, bt, extra))

        util.write_file(name + ".json", cells)


collect("results/bautzen", util.get_bautzen_coords())
# collect("results/chemnitz", util.get_chemnitz_coords())
# collect("results/dresden", util.get_dresden_coords())
collect("results/erzgebirge", util.get_erzgebirge_coords())
collect("results/goerlitz", util.get_goerlitz_coords())
collect("results/landkreis leipzig", util.get_landkreis_leipzig_coords())
collect("results/leipzig", util.get_leipzig_coords())
collect("results/meissen", util.get_meissen_coords())
collect("results/mittelsachsen", util.get_mittelsachsen_coords())
collect("results/nordsachsen", util.get_nordsachsen_coords())
collect("results/saechsische schweiz", util.get_saechsische_schweiz_coords())
collect("results/vogtland", util.get_vogtland_coords())
collect("results/zwickau", util.get_zwickau_coords())
