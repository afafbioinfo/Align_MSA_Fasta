# Align_MSA_Fasta

This script allows to align fasta Multi-sequence-Alignement using Clustalw 
and generate .aln format file that are used as input for RNAalifold.

Fasta_MSA => The input is MSA in fasta format with 'txt' extension,  you can add many MSA for diffenet RNAs at once.
An example is provided for the input ( the ensemble of UTRs used in the 'EBOLA_UTRS_Prediction_Alignement_probing1M7-NMIA'
project).

To launch the script: python2.7 Align_MSA.py

The aligned sequences are stored at Fasta_MSA folder, both 'dnd' and 'aln' formats are generated. 
