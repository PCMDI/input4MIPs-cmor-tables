MRI-JMA-JRA55-do-1-5-0
========

   Generate CMORized data for input4MIPs.


Contents
--------

   * mriJRA55-do-input.json

   * runCmorAllWrite-1-5-0.py: Generate all files for JRA55-do-v1.5.0.

   * runCmorAllWrite-1-5-0-update.py: Update only recent years for JRA55-do-v1.5.0.

   * Tables: Copy of "../../Tables".
   
   * Before running runCmorAllWrite-1-5-0.py, make symbolic links to...

      - input_atmos ---> JRA55-do main data
      - input_suppl ---> JRA55-do supplemental data
      - input_clim  ---> JRA55-do climatological data
      - input_fx    ---> JRA55-do invariant data
      - input4MIPs  ---> CMORized data for input4MIPS
 

Usage Note
--------

   * Python scripts work with python 3.8 with CMOR 3.6.0.


Contact
--------

   * Hiroyuki Tsujino (JMA-MRI)
