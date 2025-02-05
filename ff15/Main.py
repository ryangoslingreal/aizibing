#mainer for running the project
#calls 2 other functions
#1. the base NB
#2. the Selector
#run a comparison
from base_model import HeartDiseaseClassifier


cache_directory = r'D:\projects\python\selector_genetic_algorithm\cache'
classifier = HeartDiseaseClassifier(cache_dir=cache_directory)
trained_classifier = classifier.run()

