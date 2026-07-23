from framework.configuration import ConfigManager
from framework.pipeline import PipelineEngine


class FrameworkRunner:
    """
    Orchestrates the execution of the Enterprise AI Analytics Framework.
    """

    def __init__(self) -> None:
        self.config = ConfigManager()
        self.active_domain = self.config.get_active_domain()
        self.domain_settings = self.config.get_domain_settings()
        self.database_path = self.config.get_database_path()

    def run(self) -> None:
        print("Enterprise AI Analytics Framework")
        print("----------------------------------")
        print(f"Active domain: {self.active_domain}")
        print(f"Dataset path: {self.domain_settings['dataset']['path']}")
        print(f"Database path: {self.database_path}")
        print("----------------------------------")

        pipeline = PipelineEngine(
            active_domain=self.active_domain,
            domain_settings=self.domain_settings,
            database_path=self.database_path,
        )

        pipeline.execute()