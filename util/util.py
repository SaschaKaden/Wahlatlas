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


def get_saxony_coords():
    lon_start = 1316856.9993981898
    lat_start = 6457531.171883571
    lon_end = 1669386.9500434147
    lat_end = 6742784.414390394
    return [lon_start, lat_start, lon_end, lat_end]


def get_leipzig_coords():
    lon_start = 1359199.5737884492
    lat_start = 6659855.796186928
    lon_end = 1400216.4904978247
    lat_end = 6701596.540838233
    return [lon_start, lat_start, lon_end, lat_end]


def get_dresden_coords():
    lon_start = 1509215.8590818818
    lat_start = 6612468.938934873
    lon_end = 1509215.8590818818
    lat_end = 6612468.938934873
    return [lon_start, lat_start, lon_end, lat_end]


def write_file(file_name, cells):
    print(len(cells))
    json_str = jsonpickle.encode(cells)
    text_file = open(file_name, "w")
    text_file.write(json_str)
    text_file.close()
    if len(cells) == 1:
        print(jsonpickle.encode(cells))

