import glob


class ThermalService():
    def __init__(self):
        pass

    async def get_temperature(self):
        file_list = glob.glob('/sys/class/thermal/thermal_zone*/temp')

        temp_array = []
        for file_path in file_list:
            with open(file_path, 'r', encoding="unicode") as file:
                temp_raw = file.read().strip()
                temp = float(temp_raw)/1000
                temp_array.append(temp)
                print(f"{file_path}: {temp:.3f} °C")

        return temp_array

thermal_services = ThermalService()
