class car:
    def __init__(self, name, color, launch_year):
        self.name = "swift"
        self.color = "red"
        self._launch_year = 2024

    def get_launch_year(self):
        return self._launch_year

    def set_launch_year(self, year):
        self._launch_year = year
