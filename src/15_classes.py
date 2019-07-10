# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class Latlon:     
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(Latlon):
    """
    This is a waypoint class that stores name, lat, and lon
    """
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def print_name(self):
        print(self.name)
        """
        This method will print the name of the Object
        """
    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, difficulty, size):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
g = Geocache("name", 12, 24, 34, 56)

print(f"{g.name}, {g.difficulty}, {g.size}, {g.lat}, {g.lon}")
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
new_waypoint = Waypoint('Catacombs', 41.70505, -121.51521)
print(new_waypoint)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
