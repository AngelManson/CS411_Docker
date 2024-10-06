from typing import Any, Optional

from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:

    def __init__(self,
                migration_id: int,
                migration_path: MigrationPath,
                current_location: str,
                current_date: str,
                duration: Optional[int] = None) -> None:   #fix this
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.duration = duration
        self.current_date = current_date
        self.current_location = current_location
        

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
    
    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass