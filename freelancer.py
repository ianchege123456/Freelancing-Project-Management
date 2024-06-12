class Freelancer:
    def __init__(self, id, name, skills, hourly_rate):
        self.id = id
        self.name = name
        self.skills = skills
        self.hourly_rate = hourly_rate
        self.clients = []

class FreelancerManager:
    def __init__(self):
        self.freelancers = []

    def list_freelancers(self):
        return self.freelancers

    def find_freelancer_by_id(self, freelancer_id):
        for freelancer in self.freelancers:
            if freelancer.id == freelancer_id:
                return freelancer
        return None

    def find_freelancer_by_name(self, freelancer_name):
        for freelancer in self.freelancers:
            if freelancer.name == freelancer_name:
                return freelancer
        return None

    def create_freelancer(self, id, name, skills, hourly_rate):
        if self.find_freelancer_by_id(id):
            raise ValueError("Freelancer with this ID already exists.")
        freelancer = Freelancer(id, name, skills, hourly_rate)
        self.freelancers.append(freelancer)
        return freelancer

    def update_freelancer(self, freelancer_id, name=None, skills=None, hourly_rate=None):
        freelancer = self.find_freelancer_by_id(freelancer_id)
        if freelancer:
            if name:
                freelancer.name = name
            if skills:
                freelancer.skills = skills
            if hourly_rate:
                freelancer.hourly_rate = hourly_rate
            return freelancer
        raise ValueError("Freelancer with this ID does not exist.")

    def delete_freelancer(self, freelancer_id):
        freelancer = self.find_freelancer_by_id(freelancer_id)
        if freelancer:
            self.freelancers.remove(freelancer)
            return True
        return False

    def list_freelancer_clients(self, freelancer_id):
        freelancer = self.find_freelancer_by_id(freelancer_id)
        if freelancer:
            return freelancer.clients
        return None

# Example usage:
if __name__ == "__main__":
    freelancer_manager = FreelancerManager()

    # Creating freelancers
    freelancer_manager.create_freelancer(1, "Ian Chege", ["Python", "JavaScript"], 50)
    freelancer_manager.create_freelancer(2, "Eric Smith", ["Java", "C++"], 60)

    try:
        # Creating freelancer with duplicate ID (should raise ValueError)
        freelancer_manager.create_freelancer(1, "Duplicate Ian", ["Python"], 70)
    except ValueError as e:
        print(e)

       # Finding freelancer by name
    ian_chege = freelancer_manager.find_freelancer_by_name("Ian Chege")
    if ian_chege:
        print("Ian Chege found with ID:", ian_chege.id)

    # Updating freelancer
    updated_freelancer = freelancer_manager.update_freelancer(1, name="Ian Chege Jr.", hourly_rate=55)
    if updated_freelancer:
        print("Updated freelancer:", updated_freelancer.name, updated_freelancer.hourly_rate)

    # Deleting freelancer
    if freelancer_manager.delete_freelancer(2):
        print("Freelancer deleted.")

    # Listing freelancer clients
    ian_chege_clients = freelancer_manager.list_freelancer_clients(1)
    if ian_chege_clients:
        print("Ian Chege's clients:", ian_chege_clients)
    else:
        print("Ian Chege has no clients.")

