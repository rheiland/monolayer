
import subprocess
import os
import glob
import time

output_dirs = [] 
max_runs = 5
max_runs = 10
max_runs = 25
for idx in range(1,max_runs+1):
    output_dirs.append(f"run{idx:02d}")
print(output_dirs)

# all_frames = []
count = 0
# python beta/plot_cell_scalars.py run16 RdBu -1 1
# Usage:  args = output_dir colorbar_name frame show_colorbar [xmin xmax ymin ymax]
for outdir in output_dirs:
    file_pattern = outdir + "/" + "*.xml"
    xml_files = glob.glob(file_pattern)
    xml_files.sort()
    last_file = xml_files[-1]
    # print("last file= ",last_file)
    print("last index= ",last_file[-12:-4])
    current_frame = int(last_file[-12:-4])
    # print("svg_files= ",svg_files)
    # all_frames.append(svg_files[-1])
    cmd = ["python"]
    cmd.append("beta/plot_cell_scalars.py")
    cmd.append(outdir)
    cmd.append("RdBu")
    cmd.append("-1")
    cmd.append("1")
    cmd.append("-600")
    cmd.append("600")
    cmd.append("-600")
    cmd.append("600")
    print(cmd)
    p = subprocess.run(cmd)

print("\nTo assemble the montage, run:")
print("montage -geometry +0+0 -tile 5x1 run01/keep.png run02/keep.png run03/keep.png run04/keep.png run05/keep.png row1.png")
print("\nRf. beta/montage_rows.sh\n")
