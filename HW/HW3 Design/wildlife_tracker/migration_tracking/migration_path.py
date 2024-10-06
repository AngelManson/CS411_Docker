from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self,
                path_id: int,
                destination: Habitat,
                species: str, 
                start_date: str,
                start_location: Habitat,
                status: str = "Scheduled") -> None:   #fix this 
        self.path_id = path_id
        self.species = species
        self.start_date = start_date
        self.start_location = start_location
        self.status = status
        self.destination = destination

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass
    
    def get_migration_path_details(path_id) -> dict:
        pass
