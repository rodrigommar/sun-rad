import requests
import pandas as pd

class ConnectAPI:
    
    def __init__(self) -> None:
        
        self.url_base = 'https://apitempo.inmet.gov.br'
        self.token = None
        self.status = None
        
        
    # obtem estações do tipo automatico
    def get_stations_automatic(self):
        
        url = f'{self.url_base}/estacoes/T'
        response = requests.get(url)
        
        if self.test_conncetion(response):          
            data = response.json()           
            return data
        
    
    # obtem estações do tipo manual
    def get_stations_manual(self):
        
        url = f'{self.url_base}/estacoes/M'
        response = requests.get(url)
        
        if self.test_conncetion(response):          
            data = response.json()           
            return data


    # valida a conexão com API
    def test_conncetion(self, response):
        
        if response.status_code == 200:          
            return True
        
    
    # concatena as listas de dados JSON e retorna todas as estações do tipo automatico e manaual
    def get_all_stations(self):
        
        data = []
        datat = self.get_stations_automatic()
        datam = self.get_stations_manual()
        
        data.extend(datat)
        data.extend(datam)
        
        return data
        
        
        


if __name__ == '__main__':
    connect = ConnectAPI()
    
    data = connect.get_all_stations()
    
    df = pd.DataFrame(data)
    
    print(df.head())
    
    

