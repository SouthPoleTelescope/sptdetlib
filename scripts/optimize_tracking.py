from sodetlib.operations import tracking
from sodetlib.det_config import DetConfig
import numpy as np
import argparse
import pysmurf.client
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


if __name__ == '__main__':
    cfg = DetConfig()
    parser = argparse.ArgumentParser()
    parser.add_argument('--bands', '-b', nargs='*', type=int, required=True,
                        help='bands (must be in range [0,7])')
    parser.add_argument('--plot', '-p', action='store_true',
                        help='Make channel tracking plots')
    args = cfg.parse_args(parser)
    S = cfg.get_smurf_control(dump_configs=True)
    tracking.setup_tracking_params(S, cfg, bands=args.bands, show_plots=args.plot)
