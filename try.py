from cytomat import Cytomat

c = Cytomat("COM4")

print("Plate on transfer station?", c.overview_status.transfer_station_occupied)
c.plate_handler.move_plate_from_transfer_station_to_slot(5)