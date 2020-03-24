class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s1 = sum(distance[min(start, destination): max(start, destination)])
        s2 = sum(distance)
        return min(s1, s2-s1)       

