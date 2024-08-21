import arcpy
from arcpy import mp, da, management, env
from arcpy.mp import *
from arcpy.da import *
from arcpy.management import *


aprx = ArcGISProject("current")
env.workspace = r"X:\Dump\OSSG_DATA_230418\ORTHOPHOTO\ALL_ECW_MINNA\ORTHOPHOTO_NEW\ORTHOPHOTO_MINNA_ FULL INCLDIN DWG FILES\ECW"

d_frame = aprx.listMaps("Map")[0]
select_layer = d_frame.listLayers("sde_SDE_Index_grid")[0]
#print(select_layer)
        
print("Adding initiated")
with SearchCursor(select_layer, ("Tile_ID")) as cursor:
    count = 0
    for row in cursor:
        image_name = str(int(row[0]))+ ".ecw"
        if env.workspace:
            #[0:6]
            raster_layer = MakeRasterLayer(image_name,\
                                                      image_name[0:6])
            count += 1                                         
            for layer in  d_frame.listLayers():
                if layer.name == image_name[0:6]:
                    layer.visible = True                                          
            #count += 1
        processing = "." * count
        print(f"processing{processing}")
    name = "imagery" if count <= 1 else "imageries"
    print(f"{count} {processing} base {name} added")
d_frame.clearSelection()
