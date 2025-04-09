
class TempManager:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def new_label(self, base="label"):
        label = f"{base}_{self.label_count}"
        self.label_count += 1
        return label
