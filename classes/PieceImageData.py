from pathlib import Path
import pandas as pd
import os

class PieceImageData(object):
    def __init__(self, path_piece_image_dir, _class: Path):
        self.cells =  pd.read_csv(os.path.join(path_piece_image_dir, 'Tab_cells.csv'), delimiter=',')
        self.dendrities =  pd.read_csv(os.path.join(path_piece_image_dir, 'Tab_dendrites.csv'), delimiter=',')
        self.secondary_dendrities =  pd.read_csv(os.path.join(path_piece_image_dir, 'Tab_secondary_dendrities.csv'), delimiter=',')
        self.summary_image =  pd.read_csv(os.path.join(path_piece_image_dir, 'Tab_image.csv'), delimiter=',')
        
        for v in [self.cells, self.dendrities, self.secondary_dendrities, self.summary_image]:
            v.insert(0,"class", _class)
            v.insert(1,"patient_path", path_piece_image_dir.split('T')[-1])


