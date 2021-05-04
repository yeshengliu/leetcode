class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        roomVisited = set()
        keys = []
        
        # Enter room 0
        roomVisited.add(0)
        for k in rooms[0]:
            keys.append(k)
        
        while keys:
            # use the first key to unlock the door
            key = keys.pop(0)
            # check if the room is already visited
            if key in roomVisited:
                continue
            else:
                roomVisited.add(key)
                for k in rooms[key]:
                    keys.append(k)
        
        return len(roomVisited) == len(rooms)

