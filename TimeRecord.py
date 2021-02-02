import configparser
import MySQLdb
from datetime import date, datetime



class TimeRecord:
    def __init__(self, path = '../MFRC522-python/credential.ini'):
        config = configparser.ConfigParser()
        config.read(path)
        db_conf = config['DB']
        
        self.Info = db_conf
  
    def connect_db(self):
        connect_parameters = self.Info
        #print(connect_parameters)
        conn = MySQLdb.connect(connect_parameters.get('DB_HOST'), connect_parameters.get('DB_USER'),
                     connect_parameters.get('DB_PASSWORD'),connect_parameters.get('DB_NAME'))
        #cursor = conn.cursor()
        return conn
    
    
    def get_startTime(self, staffID, today):
       
        conn = self.connect_db()
        cursor = conn.cursor()
       
        command = "SELECT * FROM ssd_workingtime WHERE (staffID = '%s' and WorkDate = '%s')" % (str(staffID),today)
        cursor.execute(command)
        #cursor.fetchone()
        try:
            result = cursor.fetchone()
            startTime = result[4]
            #sTime = datetime.strftime(str(cursor.fetchone()[4]), '%H:%M:%S.%f')
            #startTime = datetime.strptime(str(sTime), '%H:%M:%S.%f')
            dataID = result[0]
            #print(type(startTime))
            print(result)
            return startTime, dataID
        
        except TypeError:
            pass

    
    def add_startTime(self, staffID, today, currentTime):
        conn = self.connect_db()
        cursor = conn.cursor()
        command  = "INSERT INTO ssd_workingtime(staffID, WorkDate, Starttime, Duration_hours) VALUES (%s, %s, %s, 0.00)" 
        data = (staffID, today, currentTime)
        cursor.execute(command, data)
        conn .commit()
        conn.close()
        
    def update_endTime_duration(self, dataID, now, duration):
        conn = self.connect_db()
        cursor = conn.cursor()
        commend = "UPDATE ssd_workingtime SET Endtime = '%s', Duration_hours= '%s'" %(now, duration)+ " WHERE id = '%s' "% dataID
        cursor.execute(commend)
        conn.commit()
        conn.close()
        
    def calculate_duration(self, startTime_tuple, now):
        """
         clacuate the duration of working hourse for each staff, and call function 'update_endTime_duration()' to record the duration
         hourse and end time into DB 
    
        """
        startTime_object = datetime.strptime(str(startTime_tuple[0]), '%H:%M:%S.%f')
        duration = format(((now - startTime_object).seconds)/3600, '.2f') #change to hours -
        self.update_endTime_duration(startTime_tuple[1], now, duration)
        
        return duration
        
    
    
     
