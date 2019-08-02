def sort_on(t):
    return t.name

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}
        self.race_time = 0

    def add_time(self, sport, time):
        self.times[sport] = time
        self.race_time += time

    def get_time(self, sport):
        return self.times[sport]

    def __eq__(self, other):
        return self.race_time == other.race_time

    def __gt__(self, other):
        return self.race_time > other.race_time

    def __str__(self):
        l = []
        l.append("Name: {}".format(self.name))
        l.append("ID: {}".format(self.tid))
        l.append("Race time: {}".format(self.race_time))
        return "\n".join(l)

class Triathlon(object):

    def __init__(self):
        self.triathlon = {}

    def add(self, triathlete):
        self.triathlon[triathlete.tid] = triathlete

    def remove(self, tid):
        del self.triathlon[tid]

    def best(self):
        return min(self.triathlon.values())

    def worst(self):
        return max(self.triathlon.values())

    def lookup(self, tid):
        if tid in self.triathlon:
            return self.triathlon[tid]
        else:
            return None

    def __str__(self):
        r = ["{}".format(t) for t in sorted(self.triathlon.values(), key=sort_on)]
        return "\n".join(r)
