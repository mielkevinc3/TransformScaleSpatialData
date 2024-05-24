from shapely.geometry import Point


def scale_data(data, xfactor, yfactor=None, point=None):
    scaled_data = data.copy()

    xfactor = float(xfactor)
    if point is not None and type(point) != Point:
        point = Point(point)

    if yfactor is None:
        yfactor = xfactor

    if point is None:
        center = data.dissolve().centroid[0]
        scaled_data.geometry = data.scale(xfactor, yfactor, origin=center)
    else:
        scaled_data.geometry = data.scale(xfactor, yfactor, origin=point)

    return scaled_data


def scale_multiple_data(datalist, xfactor, yfactor=None, scalecenter=None, point=None):
    center = None

    if scalecenter is not None:
        center = datalist[scalecenter].dissolve().centroid[0]
    elif point is not None:
        center = Point(point)
    else:
        return []

    scaled_data_list = []
    for data in datalist:
        data = scale_data(data, xfactor, yfactor=yfactor, point=center)
        scaled_data_list.append(data)

    return scaled_data_list
