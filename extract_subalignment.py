from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse
import os
import re

# input: reference ID
#        list of positions in reference sequence separated by comma

parser = argparse.ArgumentParser(description='Tool to extract alignemt on the selected positions '
                                             'according to reference.')
parser.add_argument('-a', '--aln', help='Path to the alignment file.')
parser.add_argument('-f', '--fmt', default='fasta', help='Optional argument. Specifies alignment format. '
                                                         'Key words are the same as in BioPython '
                                                         '(https://biopython.org/wiki/AlignIO). Default: fasta')
parser.add_argument('-r', '--ref', help='Reference sequence ID in alignment.')
parser.add_argument('-p', '--pos', type=str, help='Positions in the reference sequence separated by comma.'
                                                  'Alternatively - the path to the file with positions written in one '
                                                  'line separated by comma.')
parser.add_argument('-o', '--out', help='Path to the output alignment file.')
parser.add_argument('-m', '--out_fmt', default='fasta', help='Optional argumant. Specifies output format. '
                                                             'Key words are the same as in BioPython '
                                                             '(https://biopython.org/wiki/AlignIO). Default: fasta')
args = parser.parse_args()


def return_range(string):
    if re.match(r'^\d+$', string):
        return [int(string)]
    range_detect = re.match(r'^(\d+)-(\d+)$', string)
    if range_detect:
        return [x for x in range(int(range_detect[1]), int(range_detect[2]) + 1)]


with open(args.aln, 'r') as aln_file:
    aln = AlignIO.read(aln_file, args.fmt)

    # read reference sequence
    for record in aln:
        # dictionary translating reference coordinates to alignment coordinates
        ref_pos = dict()

        if record.id == args.ref:
            i = 0
            ref_i = 1

            while i < len(record.seq):
                if record.seq[i] == '-':
                    i += 1
                    continue
                else:
                    ref_pos[ref_i] = i
                    ref_i += 1
                    i += 1
            break

    positions = list()
    if os.path.exists(args.pos):
        with open(args.pos, 'r') as pos_file:
            positions = [return_range(pos) for pos in pos_file.readline().strip().split(',')]
    else:
        positions = [return_range(pos) for pos in args.pos.split(',')]

    # flatten list
    positions = [pos for element in positions for pos in element]

    # prepare alignment positions
    aln_pos = [ref_pos.get(rpos, None) for rpos in positions]

    # extracted records
    e_records = []

    for record in aln:
        seq = ''.join([record.seq[apos] for apos in aln_pos])
        e_records.append(SeqRecord(Seq(seq), id=record.id, description=''))

    aln_extract = AlignIO.MultipleSeqAlignment(e_records)

    with open(args.out, 'w') as out_file:
        AlignIO.write(aln_extract, out_file, args.out_fmt)
