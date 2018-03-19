# markerScanner.py
## Python3 Alternative to AMPHORA2 markerScanner.pl

Copyright 2018 by David Burks

markerScanner.py is meant as a replacement for the markerScanner perl script included with AMPHORA2.
More information about AMPHORA2 can be found at https://github.com/martinwu/AMPHORA2

Required Software:

     HMMER3 - http://hmmer.org/

Unlike the original markerScanner, this script does not require BioPerl for sequence output.  There is also no option for DNA input.  You may do this step prior to running the script, using any software of your choice.  This was originally performed using getorf from the EMBOSS suite in the perl script.

Running markerScanner.py

     markerScanner.py peptide-sequence-file
     
Options:

     -E: HMMER3 E-value Cutoff. Default: 1e-7
     -D: Domain of Input Proteome. Bacteria or Archaea. Default: Bacteria
     -M: Directory containing marker files. Default: ./Marker 






All marker files included with in this repo have been redistributed from AMPHORA2, under the GNU General Public License. If you intend to publish any work based on the AMPHORA2 pipeline, plesae use the following citation:

Wu M, Scott AJ. Phylogenomic analysis of bacterial and archaeal sequences with AMPHORA2. Bioinformatics 2012; 28(7):1033-1034.

Any inquiries regarding the AMPHORA2 pipeline, and not directly related to this python script, should be directed to Martin Wu at mw4yv@virigina.edu
