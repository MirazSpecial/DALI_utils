#!/usr/bin/python

import os
import sys

our_benchmarks = [
    'CastGPU',
    'CoinFlipGPU',
    'ColorTwistGPU',
    'CopyGPU',
    'CropMirrorNormalizeX',
    'FlipGPU',
    'GaussianBlurGPU',
    'MaxGPU',
    'MinGPU',
    'NormalDistributionX',
    'NormalDistribution_NonUniform',
    'OneHotGPU',
    'ShapesGPU',
    'ReshapeGPU',
    'ResizeGPU',
    'SliceGPU',
    'TransposeGPU',
    'UniformGPU',  # There are some problems with that
]

for bench in sys.argv[1:]:
    if bench not in our_benchmarks:
        print(f'Unrecognized benchmark name: {bench}')
        exit(1)

benchmarks = our_benchmarks if len(sys.argv) == 1 else sys.argv[1:]
for bench in benchmarks:
    os.system(f'./build/dali/python/nvidia/dali/test/dali_benchmark.bin '
              f'--benchmark_out=/home/public/benchmarks/results/{bench}_result.json '
              f'--benchmark_out_format=json '
              f'--benchmark_filter=OperatorBench/{bench}')

