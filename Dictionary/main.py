import wikipedia
from googletrans import Translator

x =input(" What do you know ?")
data = wikipedia.page(x)

print(data.summary)

