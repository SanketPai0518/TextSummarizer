from TXT_SUMMARIZER.config.configuration import ConfigurationManager
from TXT_SUMMARIZER.conponents.model_evaluation import ModelEvaluation
from TXT_SUMMARIZER.logging.__innit__ import logger




class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()