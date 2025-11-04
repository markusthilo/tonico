# tonico
Read binary file and generate human readable output

### Usage:

python tonico.py [-h] [-e STRING] [-o FILE] FILE

### Options:

-h, --help : show this help message and exit

-e, --encodings STRING : Encodings to try (e.g. ascii,cp1252,utf-8 - comma, no spaces, this is the default is "ascii,cp1252,utf-8")

-o, --out FILE : File to store output as CSV/TSV

### Example:
```
python tonico.py -o output.csv input.raw
```
### GPL-3
