from faker import Faker
import psycopg2
from tqdm import tqdm
import time
import subprocess

class LabDatabaseHandler:
    class LabDatabaseHandlerExecutionResponse:
        def __init__(self, duration_ms):
            self.duration_ms = duration_ms
        
        def print_duration(self):
            return f"{self.duration_ms}ms"

    def __init__(self, 
                 pg_log_path='/var/lib/pgsql/data/userdata/pg_log',
                 pg_log_name='postgresql.log', 
                 report_path='.',
                 report_filename='pg_report.html'):
        Faker.seed(0)
        self.pg_log_path = pg_log_path
        self.pg_log_name = pg_log_name
        self.report_filename = report_filename
        self.report_path = report_path
        self.conn = psycopg2.connect(
            host="postgresql.psql-tuning",
            database="postgres",
            user="postgres",
            password="postgres",
            port=5432)
        self.cur = self.conn.cursor()
        self.fake = Faker()
        self.fake.unique.clear()
    
    def get_conn(self):
        return self.conn
    
    def reset_logs(self):
        f = open(f"{self.pg_log_path}/{self.pg_log_name}", "w")
        f.write("")
        f.close()
    
    def generate_db_report(self):
        subprocess.run(["pgbadger", 
                       f"{self.pg_log_path}/{self.pg_log_name}",
                       "-o",
                       self.report_filename])
        if self.report_path != '.':
            subprocess.run(["mv", self.report_filename, f"{self.report_path}/{self.report_filename}"])
        
    def tqdm(self, count):
        return tqdm(range(count), position=0, leave=True)
    
    def commit(self):
        self.conn.commit()
    
    def execute(self, sql, repeat=1):
        time_taken = self.execute_only(sql, repeat)
        self.conn.commit()
        return time_taken
    
    def execute_only(self, sql, repeat=1):
        try:
            repeat_results = []
            for i in range(repeat):
                start_time = time.time()
                self.cur.execute(sql)
                seconds = time.time() - start_time
                repeat_results.append(round(seconds*1000))
            time_taken = sum(repeat_results) / len(repeat_results)
            return self.LabDatabaseHandlerExecutionResponse(time_taken)
        except Exception as e:
            print(e)
            self.conn.rollback()