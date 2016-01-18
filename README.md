#readme-get
readme-get is a simple tool to download a specific project version from readme.io

##Why?
readme.io is great, but there is no way to diff different document versions.
This tool downloads a whole project so you can use typical tools to see differences.

##Whats missing?
Currently there is not a published API, so this is strictly a readonly tool. If
an API becomes advailable in the future sync may be a posibility.

##Installation
```
git clone https://github.com/kevinmeziere/readme-cli.git
python setup.py install
```

##Sample Usage
```
./readme-get project-fifo v0.7.1 --threads 16
./readme-get project-fifo v0.7.2 --threads 16
cd ~/readme-get/project-fifo/
diff -qr v0.7.1 v0.7.2
```

##Hint
By clicking the gear (upper right) and then "Switch to raw mode" you can paste
the contents of any downloaded file. This makes it easy to copy pages to a newer
version.


##Known issues
Currently only tested on two column theme. Because readme-get is just scraping
the generated html it may break on other layouts. Another side affect of this is
that if the page layout changes the script may not find the right divs/classes/ect.
