import pandas as pd
def load_and_process(url_or_path_to_csv_file):

        df1 = (
              pd.read_csv(url_or_path_to_csv_file)    
              .drop(['No.','Insolation Flux', 'Equilibrium Temperature'], axis=1)
             .rename(columns={'Planet Host': 'Host Star of Planet', 'Orbital Period Days':'Orbital Period in Days'}) 
            .dropna(axis=0)
            )
        
        return df1