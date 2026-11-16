import matplotlib
matplotlib.use('Agg') # I put it in backend
import argparse
import os
import numpy as np

from sodetlib.det_config import DetConfig
from sodetlib.operations import uxm_setup


if __name__ == '__main__':
    cfg = DetConfig()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--bands', nargs='+', type=int,
        help='input bands to tune as ints, separated by spaces. Must be in '
             'range [0,7]. Defaults to tuning all bands.')

    args = cfg.parse_args(parser)
    S = cfg.get_smurf_control(dump_configs=True)

    if args.bands is None:
        args.bands = []
        bays = S.which_bays()
        if 0 in bays:
            args.bands.extend([0,1,2,3])
        if 1 in bays:
            args.bands.extend([4,5,6,7])

    uxm_setup.setup_tune(S, cfg, args.bands)
