from typing import Any, List, Optional

from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

age: Optional[int] = None
animal_id: int
animals: dict[int, Animal] = {}
animals: List[int] = []
current_date: str
current_location: str
destination: Habitat
duration: Optional[int] = None
environment_type: str
geographic_area: str
habitat_id: int
habitats: dict[int, Habitat] = {}
health_status: Optional[str] = None
migration_id: int
migration_path: MigrationPath
migrations: dict[int, Migration] = {}
path_id: int
paths: dict[int, MigrationPath] = {}
size: int
species: str
species: str
start_date: str
start_location: Habitat
status: str = "Scheduled"


def assign_animals_to_habitat(animals: List[Animal]) -> None:   #done
    pass

def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:  #done
    pass

def cancel_migration(migration_id: int) -> None:        #done
    pass

def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:     #done
    pass

def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None: #done
    pass

def get_animal_by_id(animal_id: int) -> Optional[Animal]:   #done
    pass

def get_animal_details(animal_id) -> dict[str, Any]:    #done
    pass

def get_animals_in_habitat(habitat_id: int) -> List[Animal]: #why is this in habitat (when it has a habitat id)
    pass

def get_habitat_by_id(habitat_id: int) -> Habitat: #done
    pass

def get_habitat_details(habitat_id: int) -> dict:   #why does this one have an id??? (its in habitat)
    pass

def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]: #done
    pass

def get_habitats_by_size(size: int) -> List[Habitat]: #done
    pass

def get_habitats_by_type(environment_type: str) -> List[Habitat]: #done
    pass

def get_migration_by_id(migration_id: int) -> Migration:    #done
    pass

def get_migration_details(migration_id: int) -> dict[str, Any]: #done
    pass

def get_migration_path_by_id(path_id: int) -> MigrationPath: #done
    pass

def get_migration_paths() -> list[MigrationPath]:   #done
    pass

def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:    #done
    pass

def get_migration_paths_by_species(species: str) -> list[MigrationPath]:    #done
    pass

def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:  #done
    pass

def get_migrations() -> list[Migration]:    #done
    pass

def get_migrations_by_current_location(current_location: str) -> list[Migration]:   #done
    pass

def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:    #done
    pass

def get_migrations_by_start_date(start_date: str) -> list[Migration]:   #done
    pass

def get_migrations_by_status(status: str) -> list[Migration]:   #done
    pass

def get_migration_path_details(path_id) -> dict:    #done
    pass

def register_animal(animal: Animal) -> None:    #done
    pass

def remove_animal(animal_id: int) -> None:      #done
    pass

def remove_habitat(habitat_id: int) -> None:    #done
    pass

def remove_migration_path(path_id: int) -> None:       #done
    pass

def schedule_migration(migration_path: MigrationPath) -> None:  #done
    pass

def update_animal_details(animal_id: int, **kwargs: Any) -> None:     #done
    pass

def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:  #done
    pass

def update_migration_details(migration_id: int, **kwargs: Any) -> None:     #done
    pass

def update_migration_path_details(path_id: int, **kwargs) -> None:      #done
    pass