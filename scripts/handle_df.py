from connect_API import ConnectAPI
import pandas as pd


def create_df(data):
    data =  pd.DataFrame(data)   
    return  data



def create_df_list(lista):
    data = pd.DataFrame(lista)
    return data



def create_df_csv(csv_file):
    data = pd.read_csv(csv_file)
    return data



def create_df_json(json_file):
    data = pd.read_json(json_file)
    return data



if __name__== '__main__':
    
    cnx = ConnectAPI()
    data = cnx.get_all_stations()
    
    df = create_df(data)
    print(df)
