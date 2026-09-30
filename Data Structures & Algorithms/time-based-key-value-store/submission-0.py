class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d.keys():
            self.d[key].append((value, timestamp))
        else:
            self.d[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        item = self.d[key]
        timestamp_prev = -1
        l, r = 0, len(item) - 1

        while l <= r:
            m = (l + r) // 2
            if timestamp == item[m][1]:
                return item[m][0]

            if timestamp < item[m][1]:
                r = m - 1
            else:
                timestamp_prev = max(timestamp_prev, m)
                l = m + 1
        
        return "" if timestamp_prev == -1 else item[timestamp_prev][0]