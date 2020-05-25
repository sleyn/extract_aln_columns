# extract_aln_columns
Extracts columns from alignment according to positions in the reference sequence.

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
  -p POS, --pos POS     Positions in the reference sequence separated by
                        comma.Alternatively - the path to the file with
                        positions written in one line separated by comma.
  -o OUT, --out OUT     Path to the output alignment file.
  -m OUT_FMT, --out_fmt OUT_FMT
                        Optional argumant. Specifies output format. Key words
                        are the same as in BioPython
                        (https://biopython.org/wiki/AlignIO). Default: fasta
```
