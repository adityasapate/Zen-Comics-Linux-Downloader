# Zen-Comics-Linux-Downloader

####Pre-requisites: 
Beautiful soup
```x-sh
sudo apt-get install python-beautifulsoup
```

The following script downloads all the zenpencils comics from issue 1-161. After 161, they have changed the naming url format.

```python
python zenpencils.py
```

The following command will create a folder called "ZenComics" and download the files in the folder. The files also contain the footer and few other images (4-5 images). It is advised to remove those images after download.



