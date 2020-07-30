for debian10


install

```bash
sudo apt install python3-pip
pip3 install pelican bs4 typogrify markdown ghp-import
git checkout backend
git submodule update --init --recursive
```
compile

```bash
make html
make serve   # for local test
make github  # publish to github pages
```
