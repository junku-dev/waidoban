# waidoban
Reduce file sizes to make storage easier on eReaders.

## About
Waidoban gets its name from the japanese word "waidoban" which means "wide version". The term is associated with special releases of popular manga series that get re-released in larger format.
The larger format allows for more chapters to be condensed into one volume decreasing storage needed to keep the entire series. This is why I used the name. Waidoban fits HQ PDFs into a smaller file. 

Waidoban is essentially a "wrapper" CLI for qpdf and ghostscript.
Waidoban is not a fully featured "wrapper", it's just some python code to interface with these libraries to make editing files easier.

## Use Case
Often times when I get ebooks I get them in bulk and I want to compress or edit them in similar ways so doing each individually felt too time consuming, especially in the case of manga where there can be a ton of volumes.

### Options
1. Optimize PDF Images - optimize images in pdfs to reduce file size
2. Compress PDFs - compress pdf documents to reduce file size
3. Cut Pages - make a copy with a specified page range
4. Help

<a href="https://junku-dev.github.io/waidoban_results/" target="_blank">waidoban results</a>

## Limitations
To keep it simple, pdfs are normally compressed. There are methods to decompress and then recompress to get the optimal quality and file size, however in the case of pdf files that are comprised of images, it is not that simple. If you are trying to compress pdf files of your manga the reduction in file size may leave a lot to be desired. These files may already be as optimized as possible at their current level of quality. This is where ```ghostscript``` comes into play as ```ghostscript``` can be used to manipulate the images in the pdf files. Images can be reformated using ```-dPDFSETTINGS=/{argument}```. This flag can be used to reformat images with different dpi's to assist with reducing file sizes. 

The following options exist:

- screen: 72dpi ideal for small e-readers and smartphones
- ebook: 150dpi - ideal for tablets, larger e-reader, web apps
- prepress: 300dpi - maximum quality with little compromise ideal for storage

File sizes will decrease at the cost of quality. Depending on your device, changes in quality will be less noticable.
For example, I use a nook glowlight 4 to read manga and 150dpi looked amazing and 72dpi looked very good. 72dpi also produces optimal file sizes as my ereader only has 32GB of storage.
Quality is less of a concern in my case because the nook glowlight 4 uses e-ink and it only has a 4 inch screen. 72dpi is perfectly acceptable on the nook glowlight 4.

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