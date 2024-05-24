import geopandas


def read_file(file_name):
    df = geopandas.read_file(file_name)
    return df


def write_file(file_name, df):
    df.to_file(f'./out/{file_name}.json', driver='GeoJSON')
