# monolayer
Monolayer OpenVT reference model using PhysiCell

This repository simulates a growing monolayer model as part of the OpenVT project.

To begin, we model a simple relaxation model of 11 compressed cells in a horizontal line.
```
make -j2
make load PROJ=relaxation_11cells
make
cp project project_11cells     # Windows shell may not have the "cp" command to copy
python ~/git/studio_dev/bin/studio.py -c config/relax_11cells.xml -e project_11cells
project_11cells config/relax_11cells.xml >relax_11cells.out
grep reach relax_11cells.out   # grep probably won't be on a Windows shell
# ---- custom_function: Width reached 90% , t= 88.7
```
Therefore we use 88.7 mins as the PhysiCell time to reach 90% relaxation width, i.e., the leftmost cell is at x= -45 and rightmost at x=45. And 88.7 will become the cell cycle duration for the full monolayer model.
