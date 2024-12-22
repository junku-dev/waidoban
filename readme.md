# waidoban
Reduce file sizes to make storage easier on ereaders.

## About
Waidoban is essentially a "wrapper" CLI for qpdf and ghostscript.
Waidoban is not a fully featured "wrapper", it's just some python code to interface with these libraries to make editing files easier.

## Use Case
Often times when I get ebooks I get them in bulk and I want to compress or edit them in similar ways so doing each individually felt too time consuming, especially in the case of manga where there can be a ton of volumes.

## Dependencies
### Python Dependencies

*install python libraries in a virtual-environment.*
*if a command looks incorrect please open a new issue.*

```
pip3 install PyPDF2
```

PyPDF2 is used to read file metadata.
In waidoban it is used to collect the total number of pages in a pdf.

## Other Dependencies

debian/ubuntu:

```
sudo apt install ghostscript && sudo apt install qpdf
```

arch:

```
sudo pacman -S ghostscript && sudo pacman -S qpdf
```

fedora:

```
sudo sudo dnf install ghostscript && sudo sudo dnf install qpdf
```

- ghostscript - postscript language and pdf file interpreter used to compress and optimize pdfs

- qpdf - program and C++ library for manipulating and transforming pdf files.

## Optional Install Script
### init.sh

Included will be an 'init.sh' bash script which can be used to install all dependencies.
The script will check if you have already created a virtual env for python and install python dependencies as well as ghostscript and qpdf. It will make also make 'run.sh' executable. Do so at your own risk, it might be better for your use case to install everything manually.

init.sh needs to be executable.

```
chmod +x init.sh
```

### run.sh
A bash script that starts the virtual env and then runs the program via ```python3 main.py```.

## Limitations
To keep it simple, pdfs are normally compressed. There are methods to decompress and then recompress to get the optimal quality and file size, however in the case of pdf files that are comprised of images, it is not that simple. If you are trying to compress pdf files of your manga the reduction in file size may leave a lot to be desired. These files may already be as optimized as possible at their current level of quality. This is where ```ghostscript``` comes into play as ```ghostscript``` can be used to manipulate the images in the pdf files. Images can be reformated using ```-dPDFSETTINGS=/{argument}```. This flag can be used to reformat images with different dpi's to assist with reducing file sizes. 

The following options exist:

- screen: 72dpi ideal for small ereaders and smartphones
- ebook: 150dpi - ideal for tablets, larger ereader, web apps
- prepess: 300dpi - maximum quality with little compromise ideal for storage

File sizes will decrease at the cost of quality. Depending on your device, changes in quality will be less noticable.