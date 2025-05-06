# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
class Maincruft (ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land=Mapmanager()
        base.camLens.setFov(90)
        sharik=Hero((50,50,5),self.land)

ok=Maincruft()
ok.run()
