#CA Assignment 1 - Config file
#Name - Aditya Saini
#Roll number - 2018125
#Branch - B.Tech ECE

import m5

#Importing the BaseCache from m5.objects
from m5.objects import Cache

#Defining the arguments for L2 cache for manually specifying the size and associations
import argparse
parser = argparse.ArgumentParser(description = 'Changing the assoc & size of L2 cache')
parser.add_argument("--l2_size", type=str, nargs = '?', default = '256kB', help = "Size of the L2 cache")
parser.add_argument("--l2_assoc", type=int, nargs='?', default = 4, help = "Number of Associations of the L2 cache")
args, unknown = parser.parse_known_args()
print(args)

#Defining the L1 Cache
class L1Cache(Cache):
    assoc = 2
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def connectCPU(self, cpu):
        raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.slave

#Defining the L1 instruction cache
class L1ICache(L1Cache):
    size = '16kB'

    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port

#Defining the L1 data cache
class L1DCache(L1Cache):
    size = '16kB'

    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port

#Defining the L2 cache
class L2Cache(Cache):
    size = '256kB'
    assoc = 4
    def __init__(self, size, assoc):
        super(Cache,self).__init__()
        self.size = size
        self.assoc = assoc
    tag_latency = 10
    data_latency = 10
    response_latency = 10
    mshrs = 20
    tgts_per_mshr = 12
    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.master
    def connectMemSideBus(self, bus):
        self.mem_side = bus.slave


#Importing all the SimObjects
from m5.objects import *

#System object will be our parent SimObject
system = System()

#Setting up the clock
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

#Adding CPU - TimingSimpleCPU : Executes each instrution in a single clock cycle to execute
system.cpu = TimingSimpleCPU()

#Adding sytem-wide memory bus
system.membus = SystemXBar()

#Instantiating the caches
system.cpu.icache = L1ICache()
system.cpu.dcache = L1DCache()

#Connecting the cpu to cache ports
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

#Connecting the L1 caches to L2 caches using an L2 bus
system.l2bus = L2XBar()

system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

#Instantiating the L2 cache and connecting it to the L2Bus and the memory bus
system.l2cache = L2Cache(args.l2_size, args.l2_assoc)

system.l2cache.connectCPUSideBus(system.l2bus)
system.l2cache.connectMemSideBus(system.membus)

#Initializing some imp controllers like Interrupt ports, Peripheral Input/Output Controller (PIO)
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master

system.system_port = system.membus.slave

#Creating a memry controller & connecting it to membus
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

#Starting/Instantiating a process
process = Process()

#Executing Susan in SE mode
process.cmd = ['MiBench/automotive/susan/susan','MiBench/automotive/susan/input_small.pgm','MiBench/automotive/susan/output_small.smoothing.pgm']
system.cpu.workload = process
system.cpu.createThreads()

#Beginning execution
root = Root(full_system=False, system=system)
m5.instantiate()

#Beginning simulation
print("Beginning simulation for L2 cache size = ", str(system.l2cache.size)," and L2 cache associations = ",system.l2cache.assoc)
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'
              .format(m5.curTick(), exit_event.getCause()))
