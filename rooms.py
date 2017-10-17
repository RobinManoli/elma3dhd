import pygame, os, random
import dialog

# when importing, set game as gui.game = game
game = None

class Room():
    def __init__(self, filename="", apples=[], flowers=[], wr=None, wrholder=''):
        self.filename = filename
        self.apples = apples
        self.got_apples = []
        self.flowers = flowers
        self.hoyling = False
        self.hoyls = 0
        self.wr = wr
        self.wrholder = wrholder
        self.pr = None
        self.blink = True

        self.image = None
        self.entities = []
        if filename:
            self.image = pygame.image.load(os.path.join("levels", self.filename))
            self.image.convert()

    def hoyl_start(self):
        self.hoyling = True
        self.got_apples = []

    def hoyl_stop(self):
        self.hoyling = False
        #self.got_apples = []

    def apple_clicked(self, apple):
        self.got_apples.append(apple)

    def flower_clicked(self, flower=None, cheat=False):
        if not self.wr:
            return
        if len(self.apples) == len(self.got_apples) or cheat:
            self.hoyls += 1 # count here so that cheating counts
            # lev finished
            self.hoyling = False
            if not self.pr:
                # first play
                self.pr = self.wr + self.wr * 1.2 + self.wr * random.random()
            else:
                # "höyl until" improve time
                self.pr = self.pr - random.random() * (self.pr - self.wr)
                #self.pr = time if time < self.pr else self.pr
                if "%.2f" % self.pr == "%.2f" % self.wr and not random.randint(0,4):
                    # new wr
                    self.wr = self.wr - random.random()/(self.hoyls)
                    self.pr = self.wr
                #print(self.wr, self.pr)

    def render(self):
        self.blink = not self.blink
        if self.image:
            game.screen.blit(self.image, (0,0))

        if self.wr:
            if self.pr != self.wr:
                game.gui.message("WR: %.2f %s" % (self.wr, self.wrholder), 10, 360, color=game.draw.black)
            else:
                game.gui.message("WR: %.2f [¿]" % (self.wr), 10, 360, color=game.draw.black)
        if self.pr:
            if self.pr != self.wr:
                game.gui.message("PR: %.3f" % self.pr, 666, 360, color=game.draw.black)
            else:
                game.gui.message("PR: WR!", 666, 360, color=game.draw.black)

        for apple in self.apples:
            x, y = apple
            width = 20
            height = 20
            if not self.hoyling or self.blink or apple in self.got_apples:
                pygame.draw.rect(game.screen, game.draw.black, (x,y,width,height), 0)

        for flower in self.flowers:
            x, y = flower
            width = 20
            height = 20
            if not self.hoyling or self.blink:
                pygame.draw.rect(game.screen, game.draw.blue, (x,y,width,height), 0)

        for entity in self.entities:
            if entity.visible or game.show_everything:
                if entity.label:
                    game.gui.label(entity.label, entity.x, entity.y)
                if entity.filename:
                    text_width, text_height = entity.label_size()
                    rect = entity.image.get_rect()
                    width = rect[2] - rect[0]
                    height = rect[3] - rect[1]
                    x = entity.x + text_width/2 - width/2
                    y = entity.y - height - 5
                    game.screen.blit(entity.image, (x, y))
            if entity.dialog:
                entity.dialog.render()

class Entity():
    "An interactive game object"
    def __init__(self, x=100, y=100, label="", filename="", width=0, height=0, visible=True, clickable=False, entry=None, dialog=None, level=None):
        self.x = x
        self.y = y
        self.label = label
        self.filename = filename
        self.image = None
        #self.width = width
        #self.height = height
        self.visible = visible
        self.clickable = clickable
        self.entry = entry
        self.level = level
        self.dialog = dialog
        if dialog:
            dialog.entity = self
    
        if filename:
            self.image = pygame.image.load(os.path.join("sprites", self.filename))
            self.image.convert()
            #print( self.image.get_rect() )
            
    def label_size(self):
        return game.font.size(self.label)

    def bbox(self):
        text_width, text_height = self.label_size()
        if not self.image:
            return (self.x, self.y, self.x + text_width, self.y + text_height)

        rect = self.image.get_rect()
        width = rect[2] - rect[0]
        height = rect[3] - rect[1]
        x = self.x + text_width/2 - width/2
        y = self.y - height - 5
        x2 = x + max((width, text_width))
        y2 = y + height + text_height + 5
        return (x, y, x2, y2)

    def clicked(self, event):
        if game.current_dialog and game.current_dialog.line and game.current_dialog != self.dialog:
            # dialog is already displayed, do not display this one or go into other room or start hoyling
            return
        #if self.dialog and (not game.current_dialog or not game.current_dialog.line or game.current_dialog == self.dialog):
        if self.dialog:
            if event.button == 1:
                self.dialog.next()
            elif event.button == 3:
                self.dialog.prev()

        if self.entry:
            game.room = self.entry

        if self.level:
            self.level.hoyl_start()

class Level():
    pass

# ROOMS
world = Room()
warmup = Room(filename="warmup.jpg", apples=[(738,257)], flowers=[(17,339)], wr=13.97, wrholder='bene [dat]')
flattrack = Room(filename="flattrack.jpg", apples=[], flowers=[(87,150)], wr=14.88, wrholder='ded [SPEED]')
slesk = Room(filename="slesk.jpg", apples=[(89,46),(290,26)], flowers=[(87,150)], wr=111.11, wrholder='SoC [trailbike lgr]')
nekitbattle = Room(filename="nekitbattle.jpg", apples=[(210,266),(330,230),(471,162),(574,114),(637,78),(697,47)], flowers=[(746,13)], wr=222.22, wrholder='Nekit [¿]')
mopolauta = Room()
irc = Room()
elmaland = Room(filename="elmaland.png")
nabland = Room(filename="nabland.png", apples=[(174,285)], wr=26.38, wrholder='BarTek [CF]')
miranda = Room(filename="miranda.jpg")

# WORLD
worldWarmup = Entity(label="Warm Up", x=100, y=100, clickable=True, filename="warmup.png", entry=warmup)
worldFlattrack = Entity(label="Flat Track", x=80, y=200, visible=False, filename="flattrack.png", entry=flattrack)
worldSlesk = Entity(label="Slesk", x=80, y=300, visible=False, filename="slesk.jpg", entry=slesk)
worldMopolauta = Entity(label="mopolauta", x=250, y=30, visible=False, entry=mopolauta)
worldIrc = Entity(label="irc", x=250, y=70, visible=False, entry=irc)
worldNekitbattle = Entity(label="Nekit Battle", x=100, y=400, visible=False, filename="nekitbattle.png", entry=nekitbattle)
worldElmaland = Entity(label="Elmaland", x=100, y=540, visible=False, filename="elmaland.jpg", entry=elmaland)
worldNabland = Entity(label="Nabland", x=250, y=540, visible=False, filename="nabland.jpg", entry=nabland)
worldMiranda = Entity(label="ɐpuɐɹᴉW", x=0, y=570, visible=False, filename="miranda.gif", entry=miranda)
worldLost29= Entity(label="Lost 29", x=250, y=110, visible=False, clickable=True, dialog=dialog.lost29)
worldLost54= Entity(label="Lost 54", x=240, y=243, visible=False, clickable=True, dialog=dialog.lost54)
worldLost55= Entity(label="Lost 55", x=706, y=25, visible=False, clickable=True, dialog=dialog.lost55)
worldLostinf= Entity(label="Lost ∞", x=550, y=90, visible=False, dialog=dialog.lostinf)
worldMind = Entity(label="Mind", x=550, y=330, visible=False, filename="mind.jpg", dialog=dialog.mind1)
worldBalazs = Entity(label="Balazs", x=550, y=590, visible=False, filename="balazs.jpg", dialog=dialog.balazs1)
world.entities.append( worldWarmup )
world.entities.append( worldFlattrack )
world.entities.append( worldSlesk )
world.entities.append( worldMopolauta )
world.entities.append( worldIrc )
world.entities.append( worldNekitbattle )
world.entities.append( worldElmaland )
world.entities.append( worldNabland )
world.entities.append( worldMiranda )
world.entities.append( Entity(label="Elma RPG 3D HD Real-Time Physics Solver", x=10, y=600, clickable=False) )
world.entities.append( Entity(label="- Solving any set of tightly coupled non-linear differential equations", x=10, y=620, clickable=False) )
world.entities.append( worldLost29 )
world.entities.append( worldLost54 )
world.entities.append( worldLost55 )
world.entities.append( worldLostinf )
world.entities.append( worldMind )
world.entities.append( worldBalazs )

# WARMUP
warmupZyntifox = Entity(label="zyntifox", x=600, y=600, clickable=True, filename="zyntifox.png", dialog=dialog.zyntifox1)
warmupPlay = Entity(label="play", x=100, y=100, filename="apple.png", visible=False, level=warmup)
warmup.entities.append( warmupZyntifox )
warmup.entities.append( warmupPlay )

# FLAT TRACK
flattrackZyntifox = Entity(label="zyntifox", x=600, y=600, clickable=True, filename="zyntifox.png", dialog=dialog.zyntifox6)
flattrackElg = Entity(label="elg", x=100, y=600, filename="elg.jpg", dialog=dialog.elg1, visible=False)
flattrackPlay = Entity(label="play", x=100, y=100, clickable=True, filename="apple.png", level=flattrack)
flattrack.entities.append( flattrackZyntifox )
flattrack.entities.append( flattrackElg )
flattrack.entities.append( flattrackPlay )

# SLESK
sleskSkintor = Entity(label="skint0r", x=600, y=600, clickable=True, filename="skint0r.png", dialog=dialog.skintor1)
sleskPlay = Entity(label="play", x=600, y=100, clickable=True, filename="apple.png", level=slesk)
slesk.entities.append( sleskSkintor )
slesk.entities.append( sleskPlay )

# MOPOLAUTA
mopolautaInt04 = Entity(label="What is forth internl! - Juski", x=30, y=190, clickable=True, dialog=dialog.mopolauta1)
mopolautaXiit = Entity(label="Jeu cane xiit - berh", x=30, y=230, visible=False, dialog=dialog.mopolauta2)
mopolautaTt = Entity(label="How to tt? - Thorze", x=30, y=270, visible=False, dialog=dialog.mopolauta3)
mopolautaXiit2 = Entity(label="Jeu cane xiit - berh", x=30, y=230, visible=False, dialog=dialog.mopolauta4)
mopolauta.entities.append( mopolautaInt04 )
mopolauta.entities.append( mopolautaXiit )
mopolauta.entities.append( mopolautaTt )
mopolauta.entities.append( mopolautaXiit2 )

# IRC
ircAcross = Entity(label="#across", x=30, y=100, clickable=True, dialog=dialog.across1)
ircEol = Entity(label="#irc_eol", x=30, y=140, visible=False, dialog=dialog.eol1)
ircAbula = Entity(label="Abula", x=30, y=180, visible=False, dialog=dialog.abulaIrc1)
ircAbula2 = Entity(label="Abula", x=30, y=180, visible=False, dialog=dialog.abulaIrc2)
ircAbula3 = Entity(label="Abula", x=30, y=180, visible=False, dialog=dialog.abulaIrc3)
ircKopaka = Entity(label="Kopaka", x=30, y=220, visible=False, dialog=dialog.kopaka1)
ircZweq = Entity(label="ZWEQ", x=30, y=260, visible=False, dialog=dialog.zweq1)
ircBerh = Entity(label="berh", x=30, y=300, visible=False, dialog=dialog.berhIrc1)
ircRibot = Entity(label="ribot", x=30, y=340, visible=False, dialog=dialog.ribotIrc1)
irc.entities.append( ircAcross )
irc.entities.append( ircEol )
irc.entities.append( ircAbula )
irc.entities.append( ircAbula2 )
irc.entities.append( ircAbula3 )
irc.entities.append( ircKopaka )
irc.entities.append( ircZweq )
irc.entities.append( ircBerh )
irc.entities.append( ircRibot )

# NEKIT BATTLE
nekitbattleNekit = Entity(label="Nekit", x=600, y=600, visible=False, filename="nekit.png", dialog=dialog.nekit1)
nekitbattleVille_j = Entity(label="ville_j", x=100, y=600, visible=False, filename="ville_j.png", dialog=dialog.ville_j1)
nekitbattlePlay = Entity(label="play", x=100, y=100, visible=False, filename="apple.png", level=nekitbattle)
nekitbattle.entities.append( nekitbattleNekit )
nekitbattle.entities.append( nekitbattleVille_j )
nekitbattle.entities.append( nekitbattlePlay )

# ELMALAND
elmalandNin = Entity(label="niN & ?", x=150, y=250, clickable=True, filename="nin.jpg", dialog=dialog.nin1)
elmalandMarkku = Entity(label="Markku", x=150, y=550, visible=False, filename="markku.jpg", dialog=dialog.markku1)
elmalandNin2 = Entity(label="niN & RoniMox", x=550, y=250, visible=False, filename="nin.jpg", dialog=dialog.nin6)
elmalandRibot = Entity(label="ribot?", x=720, y=620, visible=False, clickable=True, dialog=dialog.ribot1)
elmaland.entities.append( elmalandNin )
elmaland.entities.append( elmalandMarkku )
elmaland.entities.append( elmalandNin2 )
elmaland.entities.append( elmalandRibot )

# NABLAND
nablandBartek = Entity(label="BarTek", x=150, y=250, clickable=True, filename="bartek.jpg", dialog=dialog.bartek1)
nablandLabs = Entity(label="Labs", x=700, y=600, clickable=True, filename="labs.png", dialog=dialog.labs1)
nablandBartek2 = Entity(label="BarTek", x=150, y=250, visible=False, filename="bartek.jpg", dialog=dialog.bartek3)
nabland.entities.append( nablandBartek )
nabland.entities.append( nablandLabs )
nabland.entities.append( nablandBartek2 )

# MIRANDA
mirandaCsybe = Entity(label="csybe", x=100, y=300, visible=False, clickable=True, filename="csybe.bmp", dialog=dialog.csybe1)
mirandaOnla = Entity(label="onlainari", x=80, y=500, visible=False, filename="csybe.bmp", dialog=dialog.onla1)
mirandaSleap = Entity(label="sleap", x=80, y=140, visible=False, filename="csybe.bmp", dialog=dialog.sleap1)
mirandaEpp = Entity(label="epp", x=280, y=140, visible=False, filename="csybe.bmp", dialog=dialog.epp1)
mirandaAnpalcactus= Entity(label="Anpal Cactus", x=280, y=300, visible=False, filename="csybe.bmp", dialog=dialog.anpalcactus1)
mirandaAkb = Entity(label="AKB", x=280, y=500, visible=False, filename="csybe.bmp", dialog=dialog.akb1)
mirandaXarthok = Entity(label="Xarthok", x=460, y=140, visible=False, filename="csybe.bmp", dialog=dialog.xarthok1)
mirandaTwipley = Entity(label="Twipley", x=460, y=300, visible=False, filename="csybe.bmp", dialog=dialog.twipley1)
mirandaXiphias = Entity(label="Xiphias", x=460, y=500, visible=False, filename="csybe.bmp", dialog=dialog.xiphias1)
miranda.entities.append( mirandaCsybe )
miranda.entities.append( mirandaOnla )
miranda.entities.append( mirandaSleap )
miranda.entities.append( mirandaEpp )
miranda.entities.append( mirandaAnpalcactus )
miranda.entities.append( mirandaAkb )
miranda.entities.append( mirandaXarthok )
miranda.entities.append( mirandaTwipley )
miranda.entities.append( mirandaXiphias )
