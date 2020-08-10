class Wire(object):
    """
    Wire that's mapped by the values that are passed in

    Args:
        values (list): List of directions for wires path
    """

    def __init__(self, values):
        current = [0, 0]
        self.points = set() # Every point in the wire will be kept here
        self.distances = {} # Keep track of the distances for each point
        distance = 0
        # Tuple with x,y index and value to increment by
        modify_map = {
            "R": (0, 1),
            "L": (0, -1),
            "U": (1, 1),
            "D": (1, -1),
        }
        for move in values:
            amount = int(move[1:])
            direction = move[0]
            for i in range(amount):
                modifier = modify_map[direction]
                current[modifier[0]] += modifier[1]
                self.points.add((current[0], current[1]))
                distance += 1
                self.distances[tuple(current)] = distance


def get_intersects(wire1, wire2):
    """Find intersect given 2 Wire objects"""
    intersects = []
    for point in wire1:
        if point in wire2:
            intersects.append(point)
    return intersects


def get_intersect_distances(wire1, wire2, intersects):
    """Finds intersect that's closest along the wire"""
    distances = []
    for i in intersects:
        distances.append(wire1.distances[i] + wire2.distances[i])
    return min(distances)


def get_closest(points):
    """Finds closest intersect"""
    results = []
    for point in points:
        results.append(sum(map(abs, point)))
    return min(results)


INPUT = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        INPUT.append(list(line.strip().split(',')))

wire1 = Wire(INPUT[0].copy())
wire2 = Wire(INPUT[1].copy())

# Part 1
result = get_intersects(wire1.points, wire2.points)
print(get_closest(result))

# Part 2
intersects = get_intersects(wire1.points, wire2.points)
result = get_intersect_distances(wire1, wire2, intersects)
print(result)
