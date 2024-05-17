from shapely.geometry import box, Polygon


def cutout(data, coords):
    bounding_box = box(float(coords[0]), float(coords[1]), float(coords[2]), float(coords[3]))
    shape = Polygon(bounding_box)

    cutout_data = data[data.geometry.within(shape)]

    return cutout_data
