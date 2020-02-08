import TareasCSVToBD
import SendTaskToTrello
import SimpleIcsToCSV
SimpleIcsToCSV.convert_ics_to_csv()
TareasCSVToBD.LoadCSVTasktoDB()
SendTaskToTrello.send_task_to_trello()
