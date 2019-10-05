# gpus_utilization
Check the GPUs status on multiple servers

## Simply run: 

➜  ~ python servers_gpus_tracer.py -sl dnn hmm malleus -u your_username -p your_password -v 0 

```js

GPUs on: dnn
==================================================

CUDA0 -- UTILIZATION: 78% MEMORY CONSUMPTION: 8985MiB / 10989MiB
CUDA1 -- UTILIZATION: 61% MEMORY CONSUMPTION: 8415MiB / 10986MiB
CUDA2 -- UTILIZATION: 97% MEMORY CONSUMPTION: 10733MiB / 10989MiB
CUDA3 -- UTILIZATION: 78% MEMORY CONSUMPTION: 7461MiB / 10989MiB

GPUs on: hmm
==================================================

CUDA0 -- UTILIZATION: 0% MEMORY CONSUMPTION: 12180MiB / 12206MiB
CUDA1 -- UTILIZATION: 0% MEMORY CONSUMPTION: 12144MiB / 12206MiB
CUDA2 -- UTILIZATION: 98% MEMORY CONSUMPTION: 9529MiB / 12206MiB
CUDA3 -- UTILIZATION: 0% MEMORY CONSUMPTION: 0MiB / 12206MiB

GPUs on: malleus
==================================================

CUDA0 -- UTILIZATION: 0% MEMORY CONSUMPTION: 0MiB / 12212MiB
CUDA1 -- UTILIZATION: 98% MEMORY CONSUMPTION: 10343MiB / 12212MiB
CUDA2 -- UTILIZATION: 0% MEMORY CONSUMPTION: 0MiB / 12212MiB
CUDA3 -- UTILIZATION: 0% MEMORY CONSUMPTION: 0MiB / 12212MiB
```
