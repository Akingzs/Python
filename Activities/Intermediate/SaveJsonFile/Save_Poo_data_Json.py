import os
import json

class Carro():
    """A class to represent a car."""
    
    def __init__(self, nome, cor, ano):
        """Initialize car with name, color, and year."""
        self.nome = nome
        self.cor = cor
        self.ano = ano

    def to_json(self, path, filename):
        """
        Save the car's attributes to a JSON file.
        
        Parameters:
        path (str): The directory path where the file will be saved.
        filename (str): The name of the file.
        """
        # Create the directory if it doesn't exist
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as e:
                print(f"Creation of the directory {path} failed: {e}")
                return
        
        # Create the full file path
        file_path = os.path.join(path, filename)
        
        # Write the dictionary to the file
        try:
            with open(file_path, 'w') as file:
                json.dump(vars(self), file)
        except IOError as e:
            print(f"Writing to the file {file_path} failed: {e}")

    @staticmethod
    def call_json(file_path):
        with open(file_path,'r') as file:
            retorno = json.load(file)
        return retorno

def main():
    celta = Carro('Celta', 'black', 2010)
    fox = Carro('Fox', 'red', 2005)

    PATH_DIR1 = r'C:\Users\arthur.oliveira\OneDrive\Study\Python - Course\Python\Activities\SaveJsonFile'
    FILENAME1 = r'Celta_Save_Poo_data_Json.json'

    celta.to_json(PATH_DIR1, FILENAME1)

    # Save Fox 
    PATH_DIR2 = r'C:\Users\arthur.oliveira\OneDrive\Study\Python - Course\Python\Activities\SaveJsonFile'
    FILENAME2 = r'Fox_Save_Poo_data_Json.json'

    fox.to_json(PATH_DIR2, FILENAME2)


if __name__ == '__main__':
    main()