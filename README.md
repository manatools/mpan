# mpan
ManaTools Launcher

## Requirements
python3-manatools

python3-xml

python3-yui

## Installation
The installation uses cmake. You can choose your build directory.
Presuming that you will use `build/` alongside `mpan/`,
from within `build` directory:

`cmake ../mpan`

for installation in `/usr/local`.

`cmake -DCMAKE_INSTALL_PREFIX=/usr ../mpan`

for installation in `/usr`.

Then:

`make install`

## Logging
Logging is included in the code. 
You can tune the level in /etc/mpan/mpan.yml with the entry `log_level`. The keywords are Python's standard (debug, info, ...)

