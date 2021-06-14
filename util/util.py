import numpy as np
import jsonpickle


def get_req_objects(grid_size):
    grid_string = 'grid100m'
    if grid_size == 250:
        grid_string = 'grid250m'
    elif grid_size == 500:
        grid_string = 'grid500m'
    elif grid_size == 1000:
        grid_string = 'grid1km'

    bt_obj = {'lon': 0,
              'lat': 0,
              'relation': 'grid.' + grid_string,
              'grid': grid_string,
              'election_m': 'statistik.d_bt_de_17_' + grid_string,
              'election_o': 'statistik.d_bt_de_17'}
    extra_obj = {'lon': 0, 'lat': 0, 'relation': 'grid.' + grid_string}

    return bt_obj, extra_obj


def generate_ranges(coords, grid_size):
    lon_range = np.arange(coords[0], coords[2], grid_size).tolist()
    lat_range = np.arange(coords[1], coords[3], grid_size).tolist()
    return lon_range, lat_range


def write_file(file_name, cells):
    json_str = jsonpickle.encode(cells)
    text_file = open(file_name, "w")
    text_file.write(json_str)
    text_file.close()
    if len(cells) < 300:
        print(jsonpickle.encode(cells))


def get_saxony_coords():
    lon_start = 1316856.9993981898
    lat_start = 6457531.171883571
    lon_end = 1669386.9500434147
    lat_end = 6742784.414390394
    return [lon_start, lat_start, lon_end, lat_end]


def get_bautzen_coords():
    lon_start = 1530408.5731876793
    lat_start = 6624697.1064542495
    lon_end = 1630715.4782373249
    lat_end = 6721306.06108732
    return [lon_start, lat_start, lon_end, lat_end]


def get_chemnitz_coords():
    lon_start = 1414711.1114666688
    lat_start = 6575748.737780195
    lon_end = 1456958.0699797836
    lat_end = 6607093.255386701
    return [lon_start, lat_start, lon_end, lat_end]


def get_dresden_coords():
    lon_start = 1507035.5222253099
    lat_start = 6609272.8889279235
    lon_end = 1558905.4554693517
    lat_end = 6655722.634736986
    return [lon_start, lat_start, lon_end, lat_end]


def get_erzgebirge_coords():
    lon_start = 1383174.226327758
    lat_start = 6511125.101217608
    lon_end = 1506776.9510640113
    lat_end = 6592571.786010457
    return [lon_start, lat_start, lon_end, lat_end]


def get_goerlitz_coords():
    lon_start = 1604719.7398826904
    lat_start = 6588359.913962918
    lon_end = 1676962.428313011
    lat_end = 6731629.668662473
    return [lon_start, lat_start, lon_end, lat_end]


def get_landkreis_leipzig_coords():
    lon_start = 1343506.5426666068
    lat_start = 6616199.538414121
    lon_end = 1447066.1650854826
    lat_end = 6707094.748803448
    return [lon_start, lat_start, lon_end, lat_end]


def get_leipzig_coords():
    lon_start = 1359199.5737884492
    lat_start = 6659855.796186928
    lon_end = 1400216.4904978247
    lat_end = 6701596.540838233
    return [lon_start, lat_start, lon_end, lat_end]


def get_meissen_coords():
    lon_start = 1462054.5012762595
    lat_start = 6621718.27581512
    lon_end = 1543972.4069357722
    lat_end = 6703475.872461603
    return [lon_start, lat_start, lon_end, lat_end]


def get_mittelsachsen_coords():
    lon_start = 1399210.43472016
    lat_start = 6552836.992578498
    lon_end = 1521193.976061173
    lat_end = 6665381.854865649
    return [lon_start, lat_start, lon_end, lat_end]


def get_nordsachsen_coords():
    lon_start = 1353248.4189839286
    lat_start = 6651813.542354944
    lon_end = 1353248.4189839286
    lat_end = 6651813.542354944
    return [lon_start, lat_start, lon_end, lat_end]


def get_saechsische_schweiz_coords():
    lon_start = 1501488.9457561404
    lat_start = 6566568.525927757
    lon_end = 1600565.3720997765
    lat_end = 6638363.037770972
    return [lon_start, lat_start, lon_end, lat_end]


def get_vogtland_coords():
    lon_start = 1319966.8600706875
    lat_start = 6473903.767187593
    lon_end = 1407795.4795588881
    lat_end = 6566997.317544295
    return [lon_start, lat_start, lon_end, lat_end]


def get_zwickau_coords():
    lon_start = 1356821.376150203
    lat_start = 6539236.772964913
    lon_end = 1427728.6442192234
    lat_end = 6606863.646864961
    return [lon_start, lat_start, lon_end, lat_end]
