#!/usr/bin/python

import os
import sys

our_benchmarks = [
    'CastGPU',
    'CoinFlipGPU',
    'ColorTwistGPU',  # Duplicate
    'CopyGPU',
    'CropMirrorNormalizeX',  # Duplicate
    'FlipGPU',
    'GaussianBlurGPU',
    'MaxGPU',
    'MinGPU',
    'NormalDistributionX',  # Duplicate
    'NormalDistribution_NonUniform',  # Duplicate
    'OneHotGPU',
    'ShapesGPU',
    'ReshapeGPU',
    'ResizeGPU',
    'SliceGPU',
    'TransposeGPU',
    'UniformGPU',  # There are some problems with that
]

if len(sys.argv) == 1:  # Zero arguments run all benchmarks
    for bench in our_benchmarks:
        os.system(f'/home/public/benchmark.sh /home/public/benchmarks/results/{bench}_result.json json OperatorBench/{bench}')

for bench in sys.argv[1:]:
    if bench not in our_benchmarks:
        print(f'Unrecognized benchmark name: {bench}')
        exit(1)

for bench in sys.argv[1:]:
    os.system(f'/home/public/benchmark.sh /home/public/benchmarks/results/{bench}_result.json json OperatorBench/{bench}')
