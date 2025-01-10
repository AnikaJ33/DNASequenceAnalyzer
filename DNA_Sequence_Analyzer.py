""""
DNA Sequence Analyzer
This project involves creating a program that can analyze DNA sequences. 
1. Read DNA sequences from a file or accept user input.
Calculate basic statistics like GC content and sequence length.
Find and count specific nucleotide patterns or motifs.
Transcribe DNA to RNA.
Translate RNA to amino acid sequences.
Enter multiple DNA sequences and find common motifs between the sequences
Make a hidden MARKOV model
"""

#Take user input of a DNA sequence
dna_seq = input("Enter a DNA sequence: ")
print(dna_seq)

#Count number of times A,C,G,T occur in the DNA sequence
count_A = 0
count_C = 0
count_G = 0
count_T = 0

for nuc in dna_seq:
    if nuc == 'A':
        count_A += 1
    elif nuc == 'C':
        count_C += 1
    elif nuc == 'G':        
        count_G += 1
    elif nuc == 'T':
        count_T += 1
print(count_A, count_C, count_G, count_T)