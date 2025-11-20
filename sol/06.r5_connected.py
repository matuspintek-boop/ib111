def all_connected(stops: dict[str, list[str]]) -> bool:
    for stop in stops.keys():
        stack = [stop]
        reachable = {stop}
        while stack:
            for current in stops[stack.pop()]:
                if current not in reachable and current != stop:
                    reachable.add(current)
                    stack.append(current)
        if stops.keys() != reachable:
            return False
    return True
