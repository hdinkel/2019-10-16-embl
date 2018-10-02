#!env python

"""
Python script to count the number of aminoacids per sequence in a FASTA file
"""

import sys

sequence_length = 0
fasta_sequence_lengths = []

fasta_filename = sys.argv[1]

with open(fasta_filename, 'r') as fastafile:
    for line in fastafile.readlines():
        if line.startswith('>'):
            if sequence_length:
                fasta_sequence_lengths.append(sequence_length)
            sequence_length = 0
        else:
            sequence_length += len(line.strip())
    fasta_sequence_lengths.append(sequence_length)

print(sorted(fasta_sequence_lengths))
