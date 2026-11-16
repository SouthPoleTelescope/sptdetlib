import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pysmurf.client
import argparse
import numpy as np

from sodetlib.det_config import DetConfig
from sodetlib.operations.squid_curves import take_squid_curve


if __name__=='__main__':
    cfg = DetConfig()
    parser = argparse.ArgumentParser()
    parser.add_argument('--bands', '-b', type=int, nargs = '+',
						required=True,
                        help='band (must be in range [0,7])')
    parser.add_argument('--wait-time', type=float,default=0.1,
                        help='Time to wait between flux steps in seconds.')
    parser.add_argument('--Npts',type=int,default = 3,
                        help='Number of points to average')
    parser.add_argument('--frac-full-scale-max',type=float, default=0.3,
                        help='Max value of fraction full scale to use.')
    parser.add_argument('--Nsteps',type=int,default=500,
                        help='Number of points in your squid curve.')
    args = cfg.parse_args(parser)
    S = cfg.get_smurf_control(dump_configs=True)
    take_squid_curve(
        S, cfg, bands=args.bands, wait_time=args.wait_time, Npts=args.Npts,
        frac_full_scale_max=args.frac_full_scale_max, Nsteps=args.Nsteps,
    )
