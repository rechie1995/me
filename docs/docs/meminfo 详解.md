# cat /proc/meminfo 详解

`$cat /proc/meminfo`

```bash
MemTotal:           3910688 kB # 总内存
MemFree:             131356 kB # 空闲内存（MemTotal-MemFree=MemUsed）
MemAvailable:       1508860 kB # 可用内存 (MemAvailable=MemFree+Buffers+Cached)
Buffers:             284120 kB # 给文件的缓冲大小
Cached:             1348824 kB # 高速缓冲存储器使用的大小
SwapCached:             476 kB # 被高速缓冲存储使用的交换空间大小
Active:             2138244 kB # 活跃使用中的高速缓冲存储器的页面文件大小
Inactive:           1161944 kB # 不经常使用的高速缓冲存储器的页面文件大小
Active(anon):       1429752 kB # anon：不久
Inactive(anon):      376076 kB
Active(file):        708492 kB
Inactive(file):      785868 kB
Unevictable:          68732 kB
Mlocked:                128 kB
SwapTotal:          2097148 kB # 交换空间总大小
SwapFree:           2092284 kB # 空闲交换空间
Dirty:                  100 kB # 等待被写回到磁盘的大小
Writeback:                0 kB # 正在被写回的大小
AnonPages:          1735748 kB # 未映射的页的大小
Mapped:              612804 kB # 设备和文件等映射的大小
Shmem:               285620 kB
KReclaimable:        173304 kB
Slab:                285360 kB # 内核数据结构缓存的大小，可减少申请和释放内存带来的消耗
SReclaimable:        173304 kB
SUnreclaim:          112056 kB
KernelStack:          11856 kB
PageTables:           30000 kB
NFS_Unstable:             0 kB
Bounce:                   0 kB
WritebackTmp:             0 kB
CommitLimit:        4052492 kB
Committed_AS:       7222648 kB
VmallocTotal:   34359738367 kB # 虚拟内存大小
VmallocUsed:              0 kB # 已经被使用的虚拟内存大小
VmallocChunk:             0 kB
Percpu:                4864 kB
HardwareCorrupted:        0 kB
AnonHugePages:            0 kB
ShmemHugePages:           0 kB
ShmemPmdMapped:           0 kB
CmaTotal:                 0 kB
CmaFree:                  0 kB
HugePages_Total:          0
HugePages_Free:           0
HugePages_Rsvd:           0
HugePages_Surp:           0
Hugepagesize:          2048 kB
Hugetlb:                  0 kB
DirectMap4k:         255464 kB
DirectMap2M:        3813376 kB
```
