class rideMatch:
    def __init__(self):
        self.drivers = {}
        self.rider = {}
    
    def addDriver(self, driver_id, driver_loc):
        self.drivers[driver_id] = driver_loc
    
    def addRider(self, rider_id, rider_loc):
        self.rider[rider_id] = rider_loc
    
    def matchRider(self):
        if not self.rider or not self.drivers:
            return "No match found"
        
        # get first rider
        rider_id, rider_loc = next(iter(self.rider.items()))

        # Find closet driver
        min_distance = float('inf')
        match_driver = None
        
        # Fiind nearest driver
        for d_id, d_loc in self.drivers.items():
              distance = abs(d_loc - rider_loc)
              if distance < min_distance:
                  min_distance = distance
                  match_driver = d_id
        
        #remove rider
        if match_driver:
            del self.rider[rider_id] 
            del self.drivers[match_driver]
            return (rider_id, match_driver)

system = rideMatch()
system.addDriver("D1", 10)
system.addDriver("D2", 20)
system.addRider("R1", 18)

print(system.matchRider())  # Output: ("R1", "D2")