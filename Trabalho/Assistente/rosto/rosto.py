import pyglet

animation = pyglet.image.load_animation('falando.gif')
animation2 = pyglet.image.load_animation('piscando.gif')
animation3 = pyglet.image.load_animation('erro.gif')
animSprite = pyglet.sprite.Sprite(animation)
animSprite2 = pyglet.sprite.Sprite(animation2)
animSprite3 = pyglet.sprite.Sprite(animation3)

w = animSprite.width
h = animSprite.height

window = pyglet.window.Window(width = w, height = h, fullscreen = True)

r, g, b, alpha = 0.5, 0.5, 0.8, 0.5

pyglet.gl.glClearColor(r, g, b, alpha)


@window.event
def on_draw():
    window.clear()
    animSprite.draw()


pyglet.app.run()
