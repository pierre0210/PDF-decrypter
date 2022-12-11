# PDF decrypter
just a python script for decrypting pdf file

requirements: PyPDF2, PyPDF2[crypto] (optional, for AES decryption)

```
usage: pdf-decrypter.py [-h] [-f [FILE ...]] [-d DIRECTORY] [-a] -p PASSWORD [PASSWORD ...] [--delete]

Decrypt pdf files.

optional arguments:
  -h, --help            show this help message and exit
  -f [FILE ...], --file [FILE ...]
                        paths to the pdf files
  -d DIRECTORY, --directory DIRECTORY
                        pdf files directory
  -a, --all             process all pdf files
  -p PASSWORD [PASSWORD ...], --password PASSWORD [PASSWORD ...]
                        pdf passwords
  --delete              delete original files after decrytion.
```