class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        last_t = -1
        cars = sorted(list(zip(position, speed)), reverse=True)

        fleets = 0
        for car in cars:
            pos = car[0]
            speed = car[1]
            t = (target - pos) / speed

            if t > last_t:
                fleets += 1
                last_t = t
            
        return fleets
            

