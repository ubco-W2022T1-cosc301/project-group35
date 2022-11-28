import pandas as pd
def changedata(url_or_path_to_csv_file):

        dfchange = (
              pd.read_csv(url_or_path_to_csv_file)    
              .drop(['No.','Insolation Flux', 'Equilibrium Temperature','Discovery Facility','Discovery Year'], axis=1)
             .rename(columns={'Num Stars': 'No Of Stars', 'Planet Host': 'Host Star of Planet(s)'}) 
            .dropna(axis=0)
            )
        
        return dfchange
    
    