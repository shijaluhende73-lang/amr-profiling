# AMR Profiling

A Python workflow for inspecting public bacterial reference genomes and screening them for explicit antimicrobial resistance (AMR) markers.

## Overview

Antimicrobial resistance is a major global threat to infectious disease control. This project uses NCBI reference genomes of five clinically important bacteria, verifies their identity from their FASTA headers, and screens them for explicit resistance keywords with a Python script. It serves as a first-pass baseline that can be extended to sequence-level AMR gene detection.

## Genomes Analysed

| Organism | Strain | NCBI Assembly | Sequence ID |
|---|---|---|---|
| *Escherichia coli* | K-12 substr. MG1655 | GCF_000005845.2 | NC_000913.3 |
| *Salmonella enterica* subsp. *enterica* serovar Typhimurium | LT2 | GCF_000006945.2 | NC_003197.2 |
| *Staphylococcus aureus* subsp. *aureus* | NCTC 8325 | GCF_000013425.1 | NC_007795.1 |
| *Proteus mirabilis* | HI4320 | GCF_000069965.1 | NC_010554.1 |
| *Klebsiella pneumoniae* subsp. *pneumoniae* | HS11286 | GCF_000240185.1 | NC_016845.1 |

The set covers four Gram-negative Enterobacterales and one Gram-positive pathogen.

## Repository Structure

| File / Folder | Purpose |
|---|---|
| `data/` | Genome data files |
| `inspect_headers.py` | Prints the primary FASTA header of each genome file to confirm organism, strain, and sequence identity |
| `inspect_genomes.py` | Inspects the genome files |
| `screen_amr.py` | Screens genome headers for explicit resistance-related keywords and prints a summary |

## Workflow

1. **Header verification:** `inspect_headers.py` confirms that each file contains the expected organism and strain.
2. **AMR marker screening:** `screen_amr.py` analyses each genome file and reports whether explicit resistance keywords are present in the primary headers.

## Usage

Run the scripts from the project folder:

```bash
git clone https://github.com/shijaluhende73-lang/amr-profiling.git
cd amr-profiling

python inspect_headers.py
python screen_amr.py
```

## Results

`inspect_headers.py` confirmed the organism and strain of all five genome files, each described as a complete genome or complete sequence.

`screen_amr.py` found **no explicit resistance keywords in the primary headers of any of the five genomes**.

| Genome | Resistance keywords in primary header |
|---|---|
| *E. coli* K-12 MG1655 | None found |
| *S. enterica* Typhimurium LT2 | None found |
| *S. aureus* NCTC 8325 | None found |
| *P. mirabilis* HI4320 | None found |
| *K. pneumoniae* HS11286 | None found |

## Interpretation

This result is consistent with how NCBI reference headers are written: they describe the organism, strain, and assembly status, not gene content. The negative result therefore does **not** show that these organisms lack resistance genes, and it should not be read as evidence of antibiotic susceptibility. It also does not test whether the script can detect a marker when one is present.

## Limitations

- The screen examines only the primary FASTA headers. It does not search the nucleotide sequences for AMR genes.
- Only one genome per species was included, so the results do not represent the diversity within each species.
- Gene presence, even when detected, indicates resistance potential and not confirmed phenotypic resistance.

## Future Work

- Add sequence-level AMR gene detection using a curated database such as CARD, ResFinder, or NCBI AMRFinderPlus.
- Screen additional genomes, including multidrug-resistant clinical isolates.

## Author

**Shija S. Luhende**
BSc Biotechnology and Bioinformatics, University of Dodoma (UDOM), Tanzania

## Acknowledgements

Genome data from the National Center for Biotechnology Information (NCBI).
