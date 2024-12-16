# Cram
make my ebooks smaller cause I like to read manga and HQ scans are too damn big for my simple little ereader.

## About
Cram is essentially a "wrapper" CLI for qpdf and ghostscript. 
Cram is not a fully featured "wrapper", it's just some python code to interface with these libraries so that I could easily edit files in bulk.
Often times when I get ebooks I get them in bulk and I want to compress or edit them in similar ways so doing each individually felt too time consuming, especially in the case of manga where there can be a ton of volumes.

## Dependencies
### python dependencies
```
pip3 install PyPDF2
```

PyPDF2 is used to read file metadata.
In Cram it is used to collect the number of pages easily.

### Apps

debian/ubuntu:

```
sudo apt install ghostscript
sudo apt install qpdf
```
