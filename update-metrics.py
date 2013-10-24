#!/usr/bin/env python
from utils import logging, build_metrics, build_diamond
if __name__ == '__main__':
    logging.info('build metrics...')
    metrics = build_metrics()
    logging.info('build diamond...')
    build_diamond(metrics)
