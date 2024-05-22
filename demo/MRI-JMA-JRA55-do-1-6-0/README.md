MRI-JMA-JRA55-do-1-6-0
========

   Demo files to generate CMORized data for input4MIPs.


Contents
--------

   * mriJRA55-do-input.json

   * runCmorAllWrite-1-6-0-2024.py: Generate files for year 2024 of JRA55-do-v1.6.0.

   * runCmorAllWrite-1-6-0.py: Generate all files for JRA55-do-v1.6.0.

   * Tables: Copy of "../../Tables".
   
   * Before running runCmorAllWrite-1-6-0.py, make symbolic links to...

      - input_atmos ---> JRA55-do main data
      - input_suppl ---> JRA55-do supplemental data
      - input_clim  ---> JRA55-do climatological data
      - input_fx    ---> JRA55-do invariant data
      - input4MIPs  ---> CMORized data for input4MIPs
 

Usage Note
--------

   * Python scripts work with python 3.8.5 with CMOR 3.7.2.


Contact
--------

   * Hiroyuki Tsujino (JMA-MRI)
