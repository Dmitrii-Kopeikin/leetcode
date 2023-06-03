from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.average_time_db = defaultdict(lambda: defaultdict(list))
        self.in_progress_db = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_progress_db[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.in_progress_db:
            station_in, time = self.in_progress_db.pop(id)
            time = t - time
            self.average_time_db[station_in][stationName].append(time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (sum(self.average_time_db[startStation][endStation])
                / len(self.average_time_db[startStation][endStation]))
