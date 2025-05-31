""""
DNA Sequence Analyzer
This project involves creating a program that can analyze DNA sequences. 
1. Read DNA sequences from a fasta file or accept user input.
Calculate basic statistics like GC content and sequence length.
Find and count specific nucleotide patterns or motifs.
Transcribe DNA to RNA.
Translate RNA to amino acid sequences.
Enter multiple DNA sequences and find common motifs between the sequences
Make a hidden MARKOV model
DNA Sequence Analyzer
Core Features to Implement:
Start with basic sequence operations - reading FASTA files, calculating GC content (percentage of G and C nucleotides), and finding complement/reverse complement sequences. Then add sequence validation to check for invalid nucleotides and basic pattern matching to find specific motifs or restriction enzyme sites.
Intermediate Challenges:
Build a codon translator that converts DNA to amino acid sequences using the genetic code. Add reading frame analysis to find all possible protein sequences in different frames. Create a simple mutation detector that compares two sequences and identifies differences.
Advanced Extensions:
Implement ORF (Open Reading Frame) finding to locate potential genes, add basic sequence alignment for comparing related sequences, or create a primer design tool for PCR applications.
"""
import argparse

#Take user input of a DNA sequence
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(lines)
        print(len(lines))


def main():
    parser = argparse.ArgumentParser(prog="DNA Sequence Analyzer",
                                     description="Analyze DNA sequences from a FASTA file or user input.")
    parser.add_argument('-f','--file',type=str, help="Path to the FASTA file containing DNA sequences.")
    parser.add_argument('-i','--input',action='strore_true', help="Accept user input for DNA sequence.")
    args = parser.parse_args()

if __name__ == "__main__":
    main()



#     file_path = input("Enter the path to the FASTA file: ")
#     read_fasta(file_path)
    

# dna_seq = input("Enter a DNA sequence: ")
# print(dna_seq)

# #Count number of times A,C,G,T occur in the DNA sequence
# count_A = 0
# count_C = 0
# count_G = 0
# count_T = 0

# for nuc in dna_seq:
#     if nuc == 'A':
#         count_A += 1
#     elif nuc == 'C':
#         count_C += 1
#     elif nuc == 'G':        
#         count_G += 1
#     elif nuc == 'T':
#         count_T += 1
# print(count_A, count_C, count_G, count_T)