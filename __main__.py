import argparse

import transformation
import filehandling
import scaling


def init_argparser():
    parser = argparse.ArgumentParser(description='Scale spatial date')
    parser.add_argument('-i', dest='input_files', required=True, type=str,
                        help='input file holding spatial data')
    parser.add_argument('-o', dest='output_files', required=True, type=str,
                        help='destination of scaled spatial data')
    parser.add_argument('-x', dest='xfactor', required=True, type=float,
                        help='factor for scaling x axis')
    parser.add_argument('-y', dest='yfactor', required=False, type=float,
                        help='factor for scaling y axis')
    parser.add_argument('-c', dest='center', required=False, type=str,
                        help='center for scaling')
    parser.add_argument('-b', dest='bbox', required=False, type=str,
                        help='list of coordinates for bounding box in the shape minx, miny, maxx, maxy')
    parser.add_argument('-sc', dest='scale_center', required=False, type=int,
                        help='scale center for scaling multiple dataframes')
    return parser


def main():
    parser = init_argparser()
    args = parser.parse_args()

    input_files = args.input_files.split(',')
    output_files = args.output_files.split(',')

    data_frames = []
    for input_file in input_files:
        data_frames.append(filehandling.read_file(input_file))

    if args.bbox:
        bbox = args.bbox.split(',')
        for index, data_frame in enumerate(data_frames):
            data_frames[index] = transformation.cutout(data_frame, bbox)

    center = None
    if args.center:
        center = args.center.split(',')

    if len(data_frames) > 1:
        data_frames = scaling.scale_multiple_data(data_frames, args.xfactor, yfactor=args.yfactor, scalecenter=args.scale_center, point=center)
    else:
        data_frames = [scaling.scale_data(data_frames[0], args.xfactor, yfactor=args.yfactor, point=center)]

    for index, output_file in enumerate(output_files):
        filehandling.write_file(output_file, data_frames[index])


if __name__ == '__main__':
    main()
