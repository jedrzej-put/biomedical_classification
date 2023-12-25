import sys

import pandas as pd
from classes.Patient import Patient
from typing import List

class Dataset:
    def __init__(self, patients: List[str] | List[Patient]):
        if all(isinstance(x, str) for x in patients):
            self.patients = [Patient(patient) for patient in patients]
        elif all(isinstance(x, Patient) for x in patients):
            self.patients = patients
        else:
            raise ValueError("Invalid arguments")
    
    def load_data(self):
        for patient in self.patients:
            patient.load_data()

            
    
    def _concat_data(self, attribute):
        return pd.concat([patient.data[attribute] for patient in self.patients])
    
    def concat_data(self):
        for attribute in ['cells', 'dendrities', 'secondary_dendrities', 'summary_image']:
            self.__setattr__(attribute, pd.concat(self._concat_data(attribute).ravel()))

    def concat_data_level_piece(self):
        for attribute in ['cells', 'dendrities', 'secondary_dendrities', 'summary_image']:
            self.__setattr__(attribute, pd.concat(self._concat_data(attribute).ravel()))










