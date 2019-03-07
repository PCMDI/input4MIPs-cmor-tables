MRI-JMA-JRA55-do-v1-4-0
========

   Demo scripts to generate CMORized data of JRA55-do version 1.4.0 for input4MIPs


Contents
--------

   * mriJRA55-do-input.json

   * runCmorAllWrite-1-4-0.py: Generate all relevant files of JRA55-do-v1.4.0

   * Tables: Copy of ../../Tables


Usage Note
--------

   * issue the following command:
      - $ source activate cmor340
      - $ ./runCmorAllWrite-1-4-0.py

   * Following directories (Symbolic Links) are needed.
      - input_atmos ---> JRA55-do main data 
      - input_suppl ---> JRA55-do supplemental data
      - input4MIPs  ---> Output CMORized files


Contact
--------

   * Hiroyuki Tsujino (JMA-MRI)
