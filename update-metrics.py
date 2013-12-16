#!/usr/bin/env python
from utils import build_metrics, build_diamond
if __name__ == '__main__':
    metrics = build_metrics()
    build_diamond(metrics)
