MRI-JMA-JRA55-do-1-3-2
========

   Demo scripts to generate CMORized data of JRA55-do version 1.3.2 for input4MIPs


Contents
--------

   * mriJRA55-do-input.json

   * runCmorRunoffWrite-1-3-2.py: Generate runoff files of JRA55-do-v1.3.2

   * Tables: Copy of ../../Tables


Usage Note
--------

   * issue the following command:
      - $ source activate cmor340
      - $ ./runCmorRunoffWrite-1-3-2.py

   * Following directories (Symbolic Link) are needed.
      - input_atmos ---> JRA55-do main data 
      - input_suppl ---> JRA55-do supplemental data
      - input4MIPs  ---> Output CMORized 


Contact
--------

   * Hiroyuki Tsujino (JMA-MRI)
