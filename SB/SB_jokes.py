#run $pip install pyjokes
import pyjokes

def random_joke():
    print(pyjokes.get_joke(language='en'))