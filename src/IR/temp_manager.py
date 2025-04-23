
class TempManager:
    def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0

    def new_temp(self):
        name = f"t{self.temp_counter}"
        self.temp_counter += 1
        return name

    def new_label(self, prefix="label"):
        name = f"{prefix}_{self.label_counter}"
        self.label_counter += 1
        return name

