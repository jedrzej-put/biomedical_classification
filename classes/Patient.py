import sys

from pathlib import Path
from classes.PieceImageData import PieceImageData
import os
from tqdm import *
import pandas as pd


class Patient:
    def __init__(self, path_main_dir: Path):
        self.path_main_dir = path_main_dir
        self.patient_name = self.path_main_dir.split('\\')[-1]
        self._class = 1 if self.patient_name.startswith('Sick') else 0
    
    def __repr__(self):
        return repr(f"Patient name: {self.patient_name}, class: {self._class}")
    
    def load_data(self):
        pieces_image_data = [PieceImageData(os.path.join(self.path_main_dir, piece_image_dir), self._class) for piece_image_dir in tqdm(os.listdir(self.path_main_dir))]
        class_data = [self._class] * len(os.listdir(self.path_main_dir))
        patient_name_data = [self.patient_name for i in range(len(os.listdir(self.path_main_dir)))]
        pieces_image_path_data = [f"{self.patient_name}{piece_image_dir}" for piece_image_dir in os.listdir(self.path_main_dir)]
        data = {
            "piece_image_dir": [self.path_main_dir.split('T')[-1]],
            "cells": [pd.DataFrame.from_dict({
                "patient_name": patient_name_data,
                "piece_image_path": pieces_image_path_data,
                # "class": class_data,
                "cells_data": [piece_image_data.cells for piece_image_data in pieces_image_data]})],
            "dendrities": [pd.DataFrame.from_dict({
                "patient_name": patient_name_data,
                "piece_image_path": pieces_image_path_data,
                # "class": class_data,
                "dendrities_data": [piece_image_data.dendrities for piece_image_data in pieces_image_data]})],
            "secondary_dendrities": [pd.DataFrame.from_dict({
                "patient_name": patient_name_data,
                "piece_image_path": pieces_image_path_data,
                # "class": class_data,
                "secondary_dendrities_data": [piece_image_data.secondary_dendrities for piece_image_data in pieces_image_data]})],
            "summary_image": [pd.DataFrame.from_dict({
                "patient_name": patient_name_data,
                "piece_image_path": pieces_image_path_data,
                "class": class_data,
                "summary_image_data": [piece_image_data.summary_image for piece_image_data in pieces_image_data]})],
        }
        
        
        self.data = pd.DataFrame(data=data)
    
    
