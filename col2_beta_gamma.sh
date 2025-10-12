python beta/plot_cell_scalars.py -o run02 -s beta_or_gamma -f -1 -a -x0 -500 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run07 -s beta_or_gamma -f -1 -a -x0 -500 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run12 -s beta_or_gamma -f -1 -a -x0 -500 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run17 -s beta_or_gamma -f -1 -a -x0 -500 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run22 -s beta_or_gamma -f -1 -a -x0 -500 -x1 1 -y0 0 -y1 500
python beta/plot_cell_scalars.py -o run22 -s beta_or_gamma -f -1 -a -x0 -600 -x1 1 -y0 0 -y1 600
montage -geometry +0+0 -tile 1x5  run22/keep.png run17/keep.png run12/keep.png run07/keep.png run02/keep.png  col2_beta_gamma_state_0-3.png

