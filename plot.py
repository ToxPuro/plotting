import matplotlib.pyplot as plt
import numpy as np

range_start = 0
range_end = 3000
#range_start = 580
#range_end   = 620
#dat = np.genfromtxt("timings.dat",delimiter='\n')[range_start:range_end]
#dat_with_copy = np.genfromtxt("copy-timings.dat",delimiter='\n')[range_start:range_end]
#dat_with_diags = np.genfromtxt("diag-timings.dat",delimiter='\n')[range_start:range_end]
#plt.plot(dat,label="Asynchronous reading")
#plt.plot(dat_with_copy,label="Synchronous reading")
#plt.plot(dat_with_diags,label="Synchronous diagnostics")
#plt.legend()
#plt.show()

baseline = [
            3.5170062E-03,
            3.5176045E-03,
            3.4946721E-03,
            3.4389018E-03
           ]

baseline_32 =  [
                3.5370062E-03,
                3.4388073E-03,
                3.3578466E-03,
                3.3372277E-03
            ]


serial = [
            1.1143036E-02,
            7.2842154E-03,
            5.3587960E-03,
            4.4212573E-03
        ]

serial_32 = [
            1.1143036E-02,
            7.2842154E-03,
            5.3587960E-03,
            4.4212573E-03
        ]

concurrent = [
            5.7326189E-03,
            4.5975052E-03,
            4.0018811E-03,
            3.7223265E-03
           ]

concurrent_32 = [
            5.7959138E-03,
            4.5289290E-03,
            3.9222300E-03,
            3.6126114E-03
           ]

no_copy = [
            3.4941598E-03,
            3.4539288E-03,
            3.4264653E-03,
            3.4140956E-03
          ]

no_copy_32 = [
            3.4202493E-03,
            3.3408666E-03,
            3.3608666E-03,
            3.3108666E-03
          ]
cadences = [25,50,100,200]

plt.plot(cadences,baseline,label="Asynchronous diagnostics")
plt.plot(cadences,baseline_32,label="Asynchronous diagnostics on 32 nodes")
plt.plot(cadences,concurrent,label="Synchronous diagnostics")
plt.plot(cadences,concurrent_32,label="Synchronous diagnostics on 32 nodes")
plt.plot(cadences,serial,label="Serial diagnostics")
plt.plot(cadences,serial_32,label="Serial diagnostics on 32 nodes")
plt.plot(cadences,no_copy,label="Asynchronous reading")
plt.plot(cadences,no_copy_32,label="Asynchronous reading on 32 nodes")
plt.legend()
plt.ylim(ymin=0)
plt.show()
