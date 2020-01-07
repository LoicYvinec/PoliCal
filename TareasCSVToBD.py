import TareaClass
import csv
import connectSQLite
import create_subject
import configuration
from datetime import datetime


def LoadCSVTasktoDB():
    with open(configuration.get_file_location('calendar.csv')) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif len(row) > 9 and not line_count == 0:
                # print(len(row))
                create_subject.create(row[9][3:9])
                sbjID = connectSQLite.getSubjectID(row[9][3:9])
                # print(row[0])
                # Siempre se extraera la fecha aun cuando pueda tener un
                # formato YMDTXXX
                task = TareaClass.Tarea(
                    row[1], row[2], row[3], datetime.strptime(row[7][0:8], '%Y%m%d'), sbjID)
                sql = connectSQLite.saveTask(task)
                # print("Las tareas nuevas se agregaron a la BD")
                sql.connection.close()
