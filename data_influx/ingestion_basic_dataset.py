# set modules path
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from requests.api import head
import influxdb
from influxdb import InfluxDBClient, DataFrameClient
import pandas as pd


class BasicDatasetRead():
    def __init__(self, influx_setting, db_name, measurement_name):
        self.influx_setting = influx_setting
        self.db_name = db_name
        self.ms_name = measurement_name
        self.influxdb = InfluxDBClient(host=self.influx_setting.host_, port=self.influx_setting.port_, username=self.influx_setting.user_, password = self.influx_setting.pass_)
        self.influxdb.switch_database(self.db_name)
    
    def get_data_by_time(self, start_time, end_time):
        query_string = "select * from "+self.ms_name+" where time >= '"+start_time+"' and time <= '"+end_time+"'" 
        #select * from HS1 where time >= '2020-09-10T00:36:00Z' and time <= '2020-09-10T01:36:00Z
        df = pd.DataFrame(self.influxdb.query(query_string).get_points())
        return df

    def get_datafront_by_num(self, number):
        query_string = "SELECT * FROM " + self.ms_name +" LIMIT "+ number +""
        df = pd.DataFrame(self.influxdb.query(query_string).get_points())
        return df

    def get_dataend_by_num(self, number):
        query_string = "SELECT * FROM " + self.ms_name +" ORDER BY DESC LIMIT "+ number +""
        df = pd.DataFrame(self.influxdb.query(query_string).get_points())
        return df.sort_index(ascending=False)

    def get_datafront_by_duration(self, start_time, end_time):
        query_string = "select * from "+self.ms_name+" where time >= '"+start_time+"' and time <= '"+end_time+"'" 
        #select * from HS1 where time >= '2020-09-10T00:36:00Z' and time <= '2020-09-10T01:36:00Z
        df = pd.DataFrame(self.influxdb.query(query_string).get_points())
        return df


from KETIPreDataIngestion.KETI_setting import influx_setting_KETI as ins
test = BasicDatasetRead(ins, 'INNER_AIR', 'HS1')

print(test.get_data_by_time('2020-09-10T00:36:00Z', '2020-09-10T01:36:00Z'))
print(test.get_datafront_by_num('5'))
print(test.get_dataend_by_num('5'))




