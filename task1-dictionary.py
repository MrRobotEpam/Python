class Dictionary:
    def __init__(self):
        self.entries = {}

    def newentry(self, word, definition):
        self.entries[word] = definition

    def look(self, word):
        if word in self.entries:
            return self.entries[word]
        else:
            return f"Can't find entry for {word}"
    
d = Dictionary()

d.newentry("Roses", "The best option for valentine's day")
d.newentry("Gardenians", "Popular for Weddings because of its association of love")
d.newentry("Peonies", "A sign of both honour and bashfulness")

print(d.look("Roses"))
print(d.look("Gardenians"))
print(d.look("Peonies"))
print(d.look("Tulips"))