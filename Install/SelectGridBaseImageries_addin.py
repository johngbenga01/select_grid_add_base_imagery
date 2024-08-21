import arcpy
from arcpy import mapping, da, env, management
import pythonaddins

class ButtonClassBaseImageries(object):
    """Implementation for SelectGridBaseImageries_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = mapping.MapDocument("current")
        env.workspace = r"X:\Dump\OSSG_DATA_230418\ORTHOPHOTO\ALL_ECW_MINNA\ORTHOPHOTO_NEW\ORTHOPHOTO_MINNA_ FULL INCLDIN DWG FILES\ECW"

        d_frame = mapping.ListDataFrames(mxd)[0]
        select_layer = mapping.ListLayers(mxd, "sde_SDE_Index_grid")[0]
        
        print("Adding initiated")
        with da.SearchCursor(select_layer, ("Tile_ID")) as cursor:
            count = 0
            for row in cursor:
                image_name = str(int(row[0]))+ ".ecw"
                if not arcpy.Exists(image_name[0:6]):
                    raster_layer = management.MakeRasterLayer(image_name, image_name[0:6])
                    count += 1
                processing = "." * count
                print("processing{}".format(processing))
            name = "imagery" if count <= 1 else "imageries"
            print("{} .......{} base {} added".format(count, processing, name))
        d_frame.zoomToSelectedFeatures()


class ButtonClassSelectGrid(object):
    """Implementation for SelectGridBaseImageries_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = mapping.MapDocument("current")
        reference_layer = mapping.ListLayers(mxd)[0]
        print("Selection Initiated")
        management.SelectLayerByLocation("sde_SDE_Index_grid", "INTERSECT",\
                                         reference_layer)
        count = management.GetCount("sde_SDE_Index_grid")
        print("All intersecting grids with layer selected...{} selected".format(count))
