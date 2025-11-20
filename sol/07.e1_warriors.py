class Warrior:
    def __init__(self, name: str, strength: int) -> None:
        self.name = name
        self.strength = strength


class Horde:
    def __init__(self, clans: dict[str, list[Warrior]]) -> None:
        self._clans = clans

    def clans(self) -> dict[str, list[Warrior]]:
        return self._clans

    def add_warrior(self, clan: str, warrior: Warrior) -> None:
        if clan not in self._clans:
            self._clans[clan] = [warrior]
        else:
            self._clans[clan].append(warrior)

    def validate_clan_strength(self, required: int) -> bool:
        for d, ws in self._clans.items():
            total = 0
            for w in ws:
                total += w.strength
            if total <= required:
                return False
        return True
