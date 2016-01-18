#readme-get
readme-get is a simple tool to download a specific project version from readme.io

##Why?
readme.io is great, but there is no way to diff different document versions.
This tool downloads a whole project so you can use typical tools to see differences.

##Whats missing?
Currently there is not a published API, so this is strictly a readonly tool. If
an API becomes advailable in the future sync may be a posibility.

##Sample Usage
```
./readme-get project-fifo v0.7.1 --threads 16
./readme-get project-fifo v0.7.2 --threads 16
cd ~/readme-get/project-fifo/
diff -qr v0.7.1 v0.7.2
```