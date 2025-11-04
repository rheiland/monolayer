
import sys,pathlib
from pyMCDS_cells import pyMCDS_cells
import matplotlib.pyplot as plt

out_dir = "./output_monolayer"
out_dir = "./output"

#out_dir = "../PhysiCell/output_monolayer_pressure_set_behavior"
t=[]
tumor_diam=[]

cell_radius = 5.0

# fig, ax = plt.subplots()

# ------- 1st plot all computed values (at every 10 hours)
hr_delta = 1
for idx in range(1,2, hr_delta):
    xml_file = "output%08d.xml" % idx
    print("xml_file= ",xml_file)

    try:
        # mcds = pyMCDS(xml_file, out_dir)   # reads BOTH cells and substrates info
        mcds = pyMCDS_cells(xml_file, out_dir)   # reads BOTH cells and substrates info
    except:
        break
    # cell_ids = mcds.data['discrete_cells']['ID']
    print(mcds.data['discrete_cells'].keys())
    cells_x = mcds.data['discrete_cells']['position_x']
    cells_y = mcds.data['discrete_cells']['position_y']

    print("cells_x= ",cells_x)
    # print("cells_y= ",cells_y)

    print("cells_x/cell_radius= ",cells_x/cell_radius)

    current_time = mcds.get_time()
    # print('time (min)= ', current_time )
    # print('time (hr)= ', current_time/60. )
    # print('time (day)= ', current_time/1440. )
    print("# cells= ",cells_x.shape[0])
    # diam = cells_x.max() - cells_x.min()
    # print("monolayer diam= ",diam)

    # t.append(current_time/1440.)  # to get days
    # t.append(current_time/88.7)  # recall the 88.7 mins (the 90% width of 11 cells) = 1 T unit 
    # tumor_diam.append(diam/5.0)      # calibrate space units by dividing by cell radius
    # sub_intern.append(sintern)
    # sub_conc.append(sconc)