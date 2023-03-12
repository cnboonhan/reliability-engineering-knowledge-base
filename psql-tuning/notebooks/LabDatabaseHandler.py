from faker import Faker
import psycopg2
from tqdm import tqdm
import time

class LabDatabaseHandler:
    def __init__(self):
        Faker.seed(0)
        self.conn = psycopg2.connect(
            host="postgresql.psql-tuning",
            database="postgres",
            user="postgres",
            password="postgres",
            port=5432)
        self.cur = self.conn.cursor()
        self.fake = Faker()
        self.conn.rollback()
        self.reset()
    
    def reset(self):
        self.fake.unique.clear()
        
    def tqdm(self, count):
        return tqdm(range(count), position=0, leave=True)
    
    def commit(self):
        self.conn.commit()
    
    def execute_and_commit(self, sql):
        time_taken = self.execute(sql)
        self.conn.commit()
        return time_taken
    
    def execute(self, sql):
        try:
            start_time = time.time()
            self.cur.execute(sql)
            seconds = time.time() - start_time
            return round(seconds*1000)  # milliseconds
        except Exception as e:
            print(e)
            self.conn.rollback()