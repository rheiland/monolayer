python beta/plot_cell_scalars.py -o run05 -s beta_or_gamma -f -1 -a -x0 -500 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run10 -s beta_or_gamma -f -1 -a -x0 -500 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run15 -s beta_or_gamma -f -1 -a -x0 -500 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run20 -s beta_or_gamma -f -1 -a -x0 -600 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run25 -s beta_or_gamma -f -1 -a -x0 -600 -x1 1 -y0 0 -y1 500
montage -geometry +0+0 -tile 1x5  run25/keep.png run20/keep.png run15/keep.png run10/keep.png run05/keep.png  col5_beta_gamma_state_0-3.png

