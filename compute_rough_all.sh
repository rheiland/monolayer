rm results.csv
echo "N,R,A,C,w,g" > results.csv
python analysis/get_cells_csv.py run01_nbrs
analysis/metrics cells.csv >> results.csv
python analysis/get_cells_csv.py run02_nbrs
analysis/metrics cells.csv >> results.csv
python analysis/get_cells_csv.py run03_nbrs
analysis/metrics cells.csv >> results.csv
python analysis/get_cells_csv.py run04_nbrs
analysis/metrics cells.csv >> results.csv
python analysis/get_cells_csv.py run05_nbrs
analysis/metrics cells.csv >> results.csv
