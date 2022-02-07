# extract_aln_columns
Extracts columns from alignment according to positions in the reference sequence.

Positions are specified by 1-base numbering according to a reference sequence.
They could be specified:
 * one by one: 1, 15, 35. Results in 3 positions.
 * by range: 1-10. Results in 10 positions 1,2,3,4,5,6,7,8,9,10.

The motivation for this script is to ease analysis of evolution of specific positions in the reference sequence. For example if you want to build a LOGO for critical residues in the active site.

## Dependencies
 - [BioPython](https://biopython.org/wiki/Download)

## Usage

```
usage: extract_subalignment.py [-h] [-a ALN] [-f FMT] [-r REF] [-p POS]
                               [-o OUT] [-m OUT_FMT]

arguments:
  -h, --help            show this help message and exit
  -a ALN, --aln ALN     Path to the alignment file.
  -f FMT, --fmt FMT     Optional argument. Specifies alignment format. Key
                        words are the same as in BioPython
                        (https://biopython.org/wiki/AlignIO). Default: fasta
  -r REF, --ref REF     Reference sequence ID in alignment.
  -p POS, --pos POS     Positions in the reference sequence or range of positions separated by
                        comma.Alternatively - a path to the file with
                        positions or range of positions written in one line separated by comma.
                        e.g. "1,2,4,6-10" will give 1,2,4,6,7,8,9,10 positons.
  -o OUT, --out OUT     Path to the output alignment file.
  -m OUT_FMT, --out_fmt OUT_FMT
                        Optional argumant. Specifies output format. Key words
                        are the same as in BioPython
                        (https://biopython.org/wiki/AlignIO). Default: fasta
```

## Output

Output is an alignment file with specified positions. Fasta format is default.
