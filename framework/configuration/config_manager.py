from pathlib import Path
from typing import Any, Dict

import yaml


class ConfigManager:
    """
    Loads and manages framework configuration from YAML files.
    """

    def __init__(
        self,
        settings_path: str = "config/settings.yaml",
        domain_config_path: str = "config/domain_config.yaml",
    ) -> None:
        self.settings_path = Path(settings_path)
        self.domain_config_path = Path(domain_config_path)

        self.settings = self._load_yaml(self.settings_path)
        self.domain_config = self._load_yaml(self.domain_config_path)

    def _load_yaml(self, file_path: Path) -> Dict[str, Any]:
        if not file_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if data is None:
            return {}

        return data

    def get_active_domain(self) -> str:
        return self.settings.get("framework", {}).get("active_domain", "retail")

    def get_domain_settings(self, domain: str | None = None) -> Dict[str, Any]:
        selected_domain = domain or self.get_active_domain()
        domains = self.domain_config.get("domains", {})

        if selected_domain not in domains:
            raise ValueError(f"Domain not found in configuration: {selected_domain}")

        return domains[selected_domain]

    def get_database_path(self) -> str:
        return self.settings.get("database", {}).get("path", "database/analytics.duckdb")