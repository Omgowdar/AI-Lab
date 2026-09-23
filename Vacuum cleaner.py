class VacuumCleanerAgent:
    def __init__(self):
        self.location = "A"

    def act(self, environment):
        status = environment[self.location]

        if status == "Dirty":
            print(f"Location {self.location} is dirty -> Suck")
            environment[self.location] = "Clean"

        elif self.location == "A":
            print("Location A is clean -> Move Right")
            self.location = "B"

        else:
            print("Location B is clean -> Move Left")
            self.location = "A"


# Take input from user
a = input("Is location A dirty or clean? ").capitalize()
b = input("Is location B dirty or clean? ").capitalize()

environment = {
    "A": a,
    "B": b
}

agent = VacuumCleanerAgent()

print("\n--- Vacuum Cleaner Agent ---")

for _ in range(4):
    agent.act(environment)
    print("Environment:", environment)
