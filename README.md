# TNT
1. Modified Garnet code to be integrated into the gem5 simulator which can be accessed at: https://www.gem5.org/
2. Ligra benchmarks and inputs are available in the repo
3. Synthetic benchmarks are available within gem5
4. Sample ligra command line is: ./build/RISCV/gem5.fast -d m5out ./configs/example/se.py -c ./my_benchmarks/ligra/bin/riscv/BFS-Bitvector -o "-n 64 ./my_benchmarks/ligra/input/rMatGraph_J_5_100 " -n 64 --num-dirs=64 --topology=Mesh_XY  --mesh-rows=8 --cpu-type=DerivO3CPU --caches --l2cache --ruby --network=garnet2.0 --cpu-clock=2GHz --sys-clock=2GHz --num-l2caches=64 --l1d_size=32kB --l2_size=1MB --mem-size=1GB   > ./dump
5. Plots generation with data are part of the repo

