# Fracture Detection
## Install Python Packages
```
poetry add tqdm
poetry add rich
```
## Prepare Dataset
rename files and copy into dataset<br>
crop scaphoid image
|Origin Directory|Dataset Directory|
|-|-|
|data/scaphoid_detection/images|dataset/scaphoid_detection/images|
|data/scaphoid_detection/annotations|dataset/scaphoid_detection/annotations|
||dataset/fracture_detection/images|
|data/fracture_detection/annotations|dataset/fracture_detection/annotations|
```
python rename.py
```
