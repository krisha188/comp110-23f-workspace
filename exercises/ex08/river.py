"""File to define River class."""
__author__ = "730656379"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Simulates what happens in the river!"""
    
    day: int
    bears: list[int]
    fish: list[int]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """If fish or bears are too old they will die."""
        i = 0
        fishh: list[Fish] = []
        bearr: list[Bear] = []
        while i < len(self.fish):
            if self.fish[i].age <= 3:
                fishh.append(self.fish[i])
            i += 1
        self.fish = fishh
        i = 0
        while i < len(self.bears):
            if self.bears[i].age <= 5:
                bearr.append(self.bears[i])
            i += 1
        self.bears = bearr
        return None
    
    def remove_fish(self, amount: int):
        """Removes the certain amount of fish given."""
        for i in range(amount):
            if self.fish:
                self.fish.pop(0)
        return None

    def bears_eating(self):
        """Simulates a bear eating a fish."""
        for i in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                i.eat(3)
        return None
    
    def check_hunger(self):
        """If the bear starves of hunger it dies."""
        i = 0
        bearr = self.bears
        while i < len(self.bears):
            if self.bears[i].hunger_score < 0:
                bearr.pop(i)
            i += 1
        self.bears = bearr
        return None
        
    def repopulate_fish(self):
        """Fish reproduce!"""
        num_fish = len(self.fish)
        new_fish = num_fish // 2
        new = Fish()
        for i in range(new_fish):
            self.fish.append(new)
            self.fish.append(new)
            self.fish.append(new)
            self.fish.append(new)
        return None
    
    def repopulate_bears(self):
        """Bears reproduce!"""
        num_bears = len(self.bears)
        new_bears = num_bears // 2
        bear = Bear()
        for i in range(new_bears):
            self.bears.append(bear)
        return None
    
    def view_river(self):
        """Shows the fish and bear population for a certain day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates a week in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
            
