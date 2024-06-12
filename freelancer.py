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
        return None

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
    freelancer_manager.create_freelancer(2, "Alice Doe", ["Java", "C++"], 60)

    # Finding freelancer by name
    print(freelancer_manager.find_freelancer_by_name("Ian Chege").id)

    # Updating freelancer
    freelancer_manager.update_freelancer(1, name="Ian Chege Jr.")
    print(freelancer_manager.find_freelancer_by_id(1).name)

    # Deleting freelancer
    freelancer_manager.delete_freelancer(2)
    print(freelancer_manager.list_freelancers())

    # Listing freelancer clients
    print(freelancer_manager.list_freelancer_clients(1))

