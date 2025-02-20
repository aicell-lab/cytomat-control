from cytomat_python.src.cytomat import Cytomat

c = Cytomat("COM4")

print("Current temperature:", c.climate_controller.current_temperature)

print("Plate on transfer station?", c.overview_status.transfer_station_occupied)

c.move_plate_from_transfer_station_to_slot(5)