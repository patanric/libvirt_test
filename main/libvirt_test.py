import libvirt

conn = libvirt.openReadOnly('qemu:///system')
if conn is None:
    print('Failed to open connection to qemu:///system')
    exit(1)
else:
    nodeinfo = conn.getInfo()
    print('Model: ' + str(nodeinfo[0]))
    print('Memory size: ' + str(nodeinfo[1]) + ' MB')
    print('Number of CPUs: ' + str(nodeinfo[2]))
    print('MHz of CPUs: ' + str(nodeinfo[3]))
    print('Number of NUMA nodes: ' + str(nodeinfo[4]))
    print('Number of CPU sockets: ' + str(nodeinfo[5]))
    print('Number of CPU cores per socket: ' + str(nodeinfo[6]))
    print('Number of CPU threads per core: ' + str(nodeinfo[7]))

    numnodes = nodeinfo[4]
    memlist = conn.getCellsFreeMemory(0, numnodes)
    cell = 0
    for cellfreemem in memlist:
        print('Node ' + str(cell) + ': ' + str(cellfreemem) + ' bytes free memory')
        cell += 1

    print conn.getType()
    print conn.getFreeMemory()
    print conn.getHostname()
    print conn.getMaxVcpus(None)
    print conn.getLibVersion()
    print conn.getURI()

    stats = conn.getCPUStats(0)
    print("kernel: " + str(stats['kernel']))
    print("idle: " + str(stats['idle']))
    print("user: " + str(stats['user']))
    print("iowait: " + str(stats['iowait']))

    print conn.listNetworks()

conn.close()
exit(0)