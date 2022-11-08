import pandas as pd
import numpy as np
def change_and_drop(url_or_path_to_csv_file):

        df5 = (
              pd.read_csv(url_or_path_to_csv_file)    
              .drop(['Insolation Flux', 'Equilibrium Temperature'], axis=1)  
            .dropna(axis=0)
            )
        
        return df5