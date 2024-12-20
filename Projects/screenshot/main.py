import pyscreenshot

# screen
image = pyscreenshot.grab()
image.show()
image.save("screenshot.png")

# window
window_image = pyscreenshot.grab(bbox=(10,10,500,500))
window_image.show()
window_image.show("window_image.pdf")