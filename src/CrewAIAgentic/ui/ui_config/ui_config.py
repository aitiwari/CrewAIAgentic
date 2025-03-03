import yaml

class Config:
    def __init__(self, config_path="./src/CrewAIAgentic/ui/ui_config/ui_config.yaml"):
        # Load configuration from the YAML file
        with open(config_path, "r") as file:
            self.config_data = yaml.safe_load(file)

    def get_page_title(self):
        return self.config_data.get("page_title", "Default Title")

    def get_llm_options(self):
        return self.config_data.get("llm_options", [])

    def get_usecase_options(self):
        return self.config_data.get("usecase_options", [])

    def get_groq_model_options(self):
        return self.config_data.get("groq_model_options", [])
