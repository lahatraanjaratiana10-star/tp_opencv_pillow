from PIL import Image

# Ouvrir l'image officielle
im = Image.open("hopper.ppm")

# Afficher le format, la taille et le mode de l'image
print(im.format, im.size, im.mode)

# Ouvrir l'image avec le visualiseur par défaut du système
im.show()