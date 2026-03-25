#Q create data extractor class to read CSV and JSON files
import csv
import json

class DataExtractor:
    # Method to read CSV file
    def read_csv(self, file_path):
        data = []
        
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
                    
        except Exception as e:
            print("Error reading CSV:", e)
        
        return data

    # Method to read JSON file
    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
            
        except Exception as e:
            print("Error reading JSON:", e)