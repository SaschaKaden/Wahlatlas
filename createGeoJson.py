import geojson
from geojson import FeatureCollection
from geojson import Feature
from geojson import Polygon
import json
from pyproj import  Transformer
import glob


transformer = Transformer.from_crs("epsg:3035", "epsg:4326")

for file_name in glob.iglob('results/*.json'):
    if "ENZ" not in file_name:
        continue
    print(file_name)

    with open(file_name) as json_file:
        data = json.load(json_file)

    features = []
    count = 0
    for row in data:
        if row[2] == "0":
            continue

        x1_min, y1_min = float(row[0]), float(row[1])
        x2_min, y2_min = transformer.transform(y1_min + 5, x1_min + 5)
        x2_max, y2_max = transformer.transform(y1_min + 245, x1_min + 245)
        features.append(Feature(geometry=Polygon(
            [[(y2_min, x2_min), (y2_min, x2_max), (y2_max, x2_max), (y2_max, x2_min), (y2_min, x2_min)]]), properties={
            "fill": row[2]}))

        if count % 100 == 0:
            print(count)
        count += 1

    collection = FeatureCollection(features)
    result_name = file_name[:len(file_name) - 9]
    with open(result_name + '.geojson', 'w') as outfile:
        geojson.dump(collection, outfile, sort_keys=True)
