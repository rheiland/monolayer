# This script provides simple parameter exploration functionality. The script creates
# a new folder (subdirectory) for each set of parameters, makes changes to a default 
# configuration (.xml) file using specified parameter values (in an accompanying .txt file),
# copies the new config file into the new folder, then
# runs the simulation (in the background) which writes results into the new folder.
# 

import xml.etree.ElementTree as ET
from shutil import copyfile
import os
import sys
import subprocess

# print(len(sys.argv))
if (len(sys.argv) < 2):
  usage_str = "Usage: %s <exec_pgm>" % (sys.argv[0])
  print(usage_str)
  print("e.g.:  python param_sweep.py project")
  exit(1)
else:
   exec_pgm = sys.argv[1]

# background_str = " &"  # works on Unix
background_str = "  "  # works on Unix
if sys.platform == 'win32':
    background_str = ""


# xml_file_in = 'config/monolayer_gamma_beta.xml'
# xml_file_in = 'mono_gamma_beta.xml'
# xml_file_in = 'config/monolayer_11cells_symm_repuls_10.xml'
xml_file_in = 'config/param_sweep_11cells.xml'
xml_file_out = 'test.xml'
copyfile(xml_file_in, xml_file_out)
tree = ET.parse(xml_file_out)
xml_root = tree.getroot()
# first_time = True
output_dirs = []

#for repulse in [5,6,7,8,9,10,11,12,13]:  # column
run_count = 0
for repulse in [5,10,20]:  # column
    folder_name = f'output_optimize_11cells/out_run_{run_count:03d}'
    output_dirs.append(folder_name)
    if (not os.path.exists(folder_name)):
        print("--- mkdir ", folder_name)
        os.makedirs(folder_name)

    xml_file_out = os.path.join(folder_name, 'config.xml')  # copy config file into the output dir

    print('---write config file (and start sim): ', xml_file_out)
    # tree.write(xml_file_out)   # will create folder_name/config.xml
    log_file = folder_name + ".log"  
    log_file = f'output_optimize_11cells/out_run_{run_count:03d}.log'
    cmd =  exec_pgm + " " + xml_file_out + " > " + log_file + " " + background_str
    # print("----- cmd = ",cmd)
    # os.system(cmd)   # <------ Execute the simulation
    # subprocess.Popen([exec_pgm, xml_file_out])
    # with open(log_file,"w") as outf:
    #     subprocess.Popen([exec_pgm, xml_file_out],stdout=outf)

    try:
        xml_root.find('.//' + 'folder').text = str(folder_name)   # beware of rules folder!
    except:
        print("--- Error setting output folder")
        exit(-1)

    try:
        xml_root.find('.//' + 'cell_cell_repulsion_strength').text = str(repulse)
    except:
        print("--- Error setting repulsion")
        exit(-1)

    xml_file_out = os.path.join(folder_name, 'config.xml')  # copy config file into the output dir
    tree.write(xml_file_out)   # will create folder_name/config.xml

    print("----- cmd = ",cmd)
    os.system(cmd)   # <------ Execute the simulation

    run_count += 1

    # exit(-1)

print("\n ------\n Your output results will appear in these directories:\n   ",output_dirs)
print("and check for a .log file of each name for your terminal output from each simulation.\n")
