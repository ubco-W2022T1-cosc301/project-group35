def change_and_drop(url_or_path_to_csv_file):

        df5 = (
              pd.read_csv(url_or_path_to_csv_file)    
              .drop(['Insolation Flux', 'Equilibrium Temperature', 'Eccentricity','Spectral Type','Gaia Magnitude'], axis=1)  
            .dropna(axis=0)
            .sort_values(['Discovery Year'], ascending=False)
            )
        
        return df5