 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -e L1-icache-load-misses ./mmt
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -e L1-icache-load-misses ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -M ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 5 ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf list
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -e all_l2_cache_misses ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -e l2_cache ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf list
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -e cache-misses,aligment-faults,L1-dcache-load-misses,L1-icache-load-misses,cache-misses ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -e cache-misses,alignment-faults,L1-dcache-load-misses,L1-icache-load-misses,cache-misses ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf list
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -e cache-misses,alignment-faults,L1-dcache-load-misses,L1-icache-load-misses,cache-misses ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf list
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -e cache-misses,L1-dcache-load-misses,L1-icache-load-misses,cache-references,L1-dcache-loads,L1-icache-loads ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 5 -e cache-misses,L1-dcache-load-misses,L1-icache-load-misses,cache-references,L1-dcache-loads,L1-icache-loads ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 5 -e cache-misses,L1-dcache-load-misses,L1-icache-load-misses,cache-references,L1-dcache-loads,L1-icache-loads ./mm
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 5 -e cache-misses,L1-dcache-load-misses,L1-icache-load-misses,cache-references,L1-dcache-loads,L1-icache-loads ./mmt
 nvim Makefile
 getconf LEVEL1_DCACHE_LINESIZE
 nvim Makefile
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf help stat
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x -r 5 -e cache-misses,L1-dcache-load-misses,L1-icache-load-misses,cache-references,L1-dcache-loads,L1-icache-loads ./mmt
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x test.txt -r 5 -e cache-misses,L1-dcache-load-misses,L1-icache-load-misses,cache-references,L1-dcache-loads,L1-icache-loads ./mmt
 ls
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x ; -r 5 -e cache-misses,L1-dcache-load-misses,L1-icache-load-misses,cache-references,L1-dcache-loads,L1-icache-loads ./mmt
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x ";" -r 5 -e cache-misses,L1-dcache-load-misses,L1-icache-load-misses,cache-references,L1-dcache-loads,L1-icache-loads ./mmt
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x ";" -r 5 -d ./mmt
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 5 -d ./mmt
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d ./mmt
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d ./mms
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d ./mm
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d -e L1-icache-loads./mm
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d -e L1-icache-loads ./mm
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d -d -e L1-icache-loads ./mm
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d -d -d -e L1-icache-loads ./mm
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d -d -d ./mm
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x ";" -r 1 -d -d -d ./mm
 sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -r 1 -d -d -d ./mm
