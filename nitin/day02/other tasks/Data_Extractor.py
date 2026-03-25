import csv 
import json

class DataExtractor:
    def __init__(self,filepath):
        self.filepath = filepath
    
    def read_csv(self):
        try:
            with open(self.filepath,'r') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            print("file Does not exist")
            return []
        

    def read_json(self):
        try:
            with open(self.filepath,'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("FIle not found")
            return {}
csv_extractor = DataExtractor("/Users/nitinbhatia/Documents/DE-Daily-Tasks-Startapps-/nitin/day02/other tasks/posts_with_comment_counts.csv")
data = csv_extractor.read_csv        