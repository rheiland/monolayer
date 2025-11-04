python beta/plot_cell_scalars.py -o run26 -s a_i -f -1 -a -x0 -500 -x1 500 -y0 -500 -y1 500
python beta/plot_cell_scalars.py -o run27 -s a_i -f -1 -a -x0 -500 -x1 500 -y0 -500 -y1 500
python beta/plot_cell_scalars.py -o run28 -s a_i -f -1 -a -x0 -500 -x1 500 -y0 -500 -y1 500
python beta/plot_cell_scalars.py -o run29 -s a_i -f -1 -a -x0 -500 -x1 500 -y0 -500 -y1 500
python beta/plot_cell_scalars.py -o run30 -s a_i -f -1 -a -x0 -500 -x1 500 -y0 -500 -y1 500
montage -geometry +0+0 -tile 5x1  run26/keep.png run27/keep.png run28/keep.png run29/keep.png run30/keep.png  row_gamma_07.png

