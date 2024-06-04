from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class RetoTec(BaseSegDataset):
    METAINFO = dict(
        classes=('urban_land', 'agriculture_land', 'rangeland', 'forest_land', 'water', 'barren_land',
                 'unknown'),
        palette=[[0, 255, 255], [255, 255, 0], [255, 0, 255], [0, 255, 0],
                 [0, 0, 255], [255, 255, 255], [0, 0, 0],
                 ])
    
    class_dict={
                "1": "urban_land",
                "2": "agriculture_land",
                "3": "rangeland",
                "4": "forest_land",
                "0": "water",
                "5": "barren_land",
                "6": "unknown",
                }
    color_map = [
            [0, 255, 255], [255, 255, 0], [255, 0, 255], [0, 255, 0],
            [0, 0, 255], [255, 255, 255], [0, 0, 0],
            ]

    def __init__(self,
                 img_suffix='_sat.jpg',
                 seg_map_suffix='_mask.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)