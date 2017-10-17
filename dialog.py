import pygame, os
import rooms

game = None

class Dialog():
    "Rendered from rooms, as each dialog belongs to an entity."
    def __init__(self, enterdlg=None, enterroom=None, nextdlg=None, showrooms=[], hiderooms=[], showentities=[], hideentities=[]):
        self.lines = []
        self.line = None
        self.enterdlg = enterdlg # the dialog to start when this dialog ends
        self.enterroom = enterroom # the room to enter when this dialog ends
        self.nextdlg = nextdlg # the dialog to start next time clicking this entity
        self.showrooms = showrooms # the rooms to make visible when this dialog ends
        self.hiderooms = hiderooms # the rooms to hide when this dialog ends
        self.showentities = showentities # the entities to show when this dialog ends
        self.hideentities = hideentities # the entities to hide when this dialog ends

    def render(self):
        if not self.line:
            return

        game.gui.dialog( self.line )

    def lineislast(self):
        return self.line == self.lines[-1]
        
    def linehasoptions(self):
        return 'options' in self.line.keys()

    def next(self):
        "Triggers when entity is left clicked, and goes to next line unless there are options on the current."
        #print(self.line, len(self.lines) - 1, self.lines)
        #print( self.entity )
        if not self.line:
            # init dialog
            self.line = self.lines[0]

        elif self.linehasoptions():
            # don't proceed with dialog, since selecting an option needs to be done
            pass

        elif not self.lineislast():
            # next line exists
            index = self.lines.index(self.line)
            self.line = self.lines[index + 1]

        else:
            # reset
            self.line = None
            if self.nextdlg:
                self.donextdlg(self.nextdlg)

            if self.enterdlg:
                self.doenterdlg(self.enterdlg)

            if self.showentities:
                self.doshowentities(self.showentities)

            if self.hideentities:
                self.dohideentities(self.hideentities)
        game.current_dialog = self

    def prev(self):
        if not self.line:
            return
        index = self.lines.index(self.line)
        if index > 0:
            self.line = self.lines[index - 1]
        game.current_dialog = self

    def triggeroption(self, n):
        if n and 'options' in self.line.keys() and n <= len(self.line['options']):
            #print('trigger option ' + str(n))
            option = self.line['options'][n - 1]
            self.line = None
            if option.enterdlg:
                self.doenterdlg(option.enterdlg)

    def donextdlg(self, dlg):
        #self.line = None
        self.entity.dialog = dlg
        game.current_dialog = dlg
        dlg.entity = self.entity # make next dlg entity same as this one

    def doenterdlg(self, dlg):
        self.donextdlg(dlg)
        dlg.next() # init next dlg

    def doshowentities(self, entities):
        "Since rooms imports dialog, dialog cannot import rooms before that, and therefore cannot use its globals on import. Hence use getattr."
        for entityStr in entities:
            entity = getattr(rooms, entityStr)
            entity.visible = True
            entity.clickable = True

    def dohideentities(self, entities):
        "Since rooms imports dialog, dialog cannot import rooms before that, and therefore cannot use its globals on import. Hence use getattr."
        for entityStr in entities:
            entity = getattr(rooms, entityStr)
            entity.visible = False
            entity.clickable = False

class Option():
    def __init__(self, text, enterdlg=None, enterroom=None, showrooms=[], hiderooms=[], showentities=[], hideentities=[]):
        self.text = text
        self.enterdlg = enterdlg # the dialog to start when this option is chosen
        self.enterroom = enterroom # the room to enter when this option is chosen
        self.showrooms = showrooms # the rooms to make visible when this option is chosen
        self.hiderooms = hiderooms # the rooms to hide when this option is chosen
        self.showentities = showentities # the entities to show when this option is chosen
        self.hideentities = hideentities # the entities to hide when this option is chosen

#
# ZYNTIFOX
#
zyntifox7 = Dialog(showentities=['flattrackElg'])
zyntifox6 = Dialog()
zyntifox5 = Dialog(showentities=['warmupPlay', 'worldFlattrack'])
zyntifox4 = Dialog(nextdlg=zyntifox5)
zyntifox3 = Dialog(enterdlg=zyntifox4)
zyntifox2 = Dialog(enterdlg=zyntifox4)
zyntifox1 = Dialog()

# warmup
zyntifox1.lines.append( dict(line="<zyntifox> Hi!1 you new? Click me again.") )
zyntifox1.lines.append( dict(line="<zyntifox> Right click me to go back.") )
options = []
options.append( Option("oke", enterdlg=zyntifox4) )
options.append( Option("no", enterdlg=zyntifox3) )
options.append( Option("o,o", enterdlg=zyntifox2) )
zyntifox1.lines.append( dict(line="<zyntifox> To answer me you use number keys, ok?", options=options) )

zyntifox2.lines.append( dict(line="<zyntifox> whatever") )
zyntifox3.lines.append( dict(line="<zyntifox> yes!!!1") )

zyntifox4.lines.append( dict(line="<zyntifox> oke, so.. you must complete all levels.. i think.. or skip?") )
zyntifox4.lines.append( dict(line="<zyntifox> anyway, press ESC to go back to wurld") )
zyntifox4.lines.append( dict(line="<zyntifox> also, you cane play this lev") )
zyntifox4.lines.append( dict(line="<zyntifox> just click the apple") )
zyntifox4.lines.append( dict(line="<zyntifox> where's the apple?") )
zyntifox4.lines.append( dict(line="<zyntifox> ?") )

zyntifox5.lines.append( dict(line="<zyntifox> Jsut click the apple to höyl for a beter time?") )

# flattrack
zyntifox6.lines.append( dict(line="<zyntifox> Hi!1 you new?") )
zyntifox6.lines.append( dict(line="<zyntifox> Oh, it's you again.") )
options = []
options.append( Option("zeth") )
options.append( Option("elbono") )
options.append( Option("elg", enterdlg=zyntifox7) )
zyntifox6.lines.append( dict(line="<zyntifox> Do jeu even remember who you ar?", options=options) )
zyntifox7.lines.append( dict(line="<zyntifox> ?") )


#
# ELG
#
elg1 = Dialog(showentities=['worldSlesk'])
elg1.lines.append( dict(line="<elg> i remember u") )
elg1.lines.append( dict(line="<elg> oh, teh thirdz internal?") )
elg1.lines.append( dict(line="<elg> i forget the name") )
elg1.lines.append( dict(line="<elg> no wait, it was... uhm... SLESKT?") )

#
# SKINTOR
#
skintor2 = Dialog()
skintor1 = Dialog(nextdlg=skintor2)
skintor5 = Dialog(nextdlg=skintor1, showentities=['worldIrc'])
skintor4 = Dialog(nextdlg=skintor1, showentities=['worldMopolauta'])
skintor3 = Dialog(nextdlg=skintor1)

skintor1.lines.append( dict(line="<skint0r> oh its you") )
skintor1.lines.append( dict(line="<skint0r> or?") )
skintor1.lines.append( dict(line="<skint0r> you forgot your name?") )
skintor2.lines.append( dict(line="<skint0r> anyway, ask me anything") )
options = []
options.append( Option("What's my tt?", enterdlg=skintor3) )
options.append( Option("Where's mopolauta?", enterdlg=skintor4) )
options.append( Option("Where's irc", enterdlg=skintor5) )
skintor2.lines.append( dict(line="<skint0r> except what u want to know", options=options) )
skintor3.lines.append( dict(line="<skint0r> tt?") )
skintor3.lines.append( dict(line="<skint0r> i think you can see teh") )
skintor3.lines.append( dict(line="<skint0r> but dunoz if implemented") )
skintor4.lines.append( dict(line="<skint0r> lauta eh?") )
skintor4.lines.append( dict(line="<skint0r> hmm i forgot maybe") )
skintor4.lines.append( dict(line="<skint0r> i thinkz, look at wurld mape") )
skintor5.lines.append( dict(line="<skint0r> irc?") )
skintor5.lines.append( dict(line="<skint0r> what is this?") )
skintor5.lines.append( dict(line="<skint0r> #across?") )
skintor5.lines.append( dict(line="<skint0r> hmmz") )
skintor5.lines.append( dict(line="<skint0r> one idea") )
skintor5.lines.append( dict(line="<skint0r> maybe") )
skintor5.lines.append( dict(line="<skint0r> could try") )
skintor5.lines.append( dict(line="<skint0r> ...") )
skintor5.lines.append( dict(line="<skint0r> wurld mape o,o") )

#skintor2.lines.append( dict(line="<skint0r> you can also intsta-quit with CTRL+Q") )

#
# MOPOLAUTA
#
mopolauta4 = Dialog()
mopolauta4a = Dialog(showentities=['worldElmaland'], nextdlg=mopolauta4)
mopolauta4b = Dialog(nextdlg=mopolauta4)
mopolauta4c = Dialog(nextdlg=mopolauta4)
mopolauta4d = Dialog(nextdlg=mopolauta4)
mopolauta3 = Dialog(showentities=['mopolautaXiit2'], hideentities=['mopolautaXiit'])
mopolauta2 = Dialog(showentities=['ircAbula'])
mopolauta1 = Dialog(showentities=['worldNekitbattle'])
mopolauta1.lines.append( dict(line="<Juski> What is name of namber 04. I Forgoted?") )
mopolauta1.lines.append( dict(line="<Nekit> )") )
mopolauta1.lines.append( dict(line="<Nekit> int04 = in and out") )

mopolauta2.lines.append( dict(line="<berh> i tell u if 39 mins club") )

mopolauta3.lines.append( dict(line="<Thorze> cant founded how to c tt") )
mopolauta3.lines.append( dict(line="<BarteK> ...") )
mopolauta3.lines.append( dict(line="*** it's spelled BarTek ***") )
mopolauta3.lines.append( dict(line="*** sorry ***") )
mopolauta3.lines.append( dict(line="*** sorry off topic ***") )
mopolauta3.lines.append( dict(line="<BarTek> ...") )
mopolauta3.lines.append( dict(line="<BarTek> Thorze: u need find lost internals") )
mopolauta3.lines.append( dict(line="<milagros> already found them") )
mopolauta3.lines.append( dict(line="<milagros> can you beat my tt?") )
mopolauta3.lines.append( dict(line="<milagros> i will not tell you mine") )

options = []
options.append( Option("ask about elmaland", enterdlg=mopolauta4a) )
options.append( Option("ask about nabland", enterdlg=mopolauta4b) )
options.append( Option("ask about ribot", enterdlg=mopolauta4c) )
options.append( Option("ask about mopogirl", enterdlg=mopolauta4d) )
mopolauta4.lines.append( dict(line="<berh> you forgot who you are? lol", options=options) )
mopolauta4a.lines.append( dict(line="<berh> elmaland?") )
mopolauta4a.lines.append( dict(line="<berh> you think you can find answers there?") )
mopolauta4a.lines.append( dict(line="<berh> uhm, sure i know where it is") )
mopolauta4a.lines.append( dict(line="*** guess where ***") )
mopolauta4b.lines.append( dict(line="<berh> nabland?") )
mopolauta4b.lines.append( dict(line="<berh> never heard of it") )
mopolauta4c.lines.append( dict(line="<berh> ribot?") )
mopolauta4c.lines.append( dict(line="<berh> yes i know") )
mopolauta4c.lines.append( dict(line="<berh> but i won't tell") )
mopolauta4d.lines.append( dict(line="<berh> mopogirl?") )
mopolauta4d.lines.append( dict(line="<berh> did you even play Elmaland RPG™ o,o") )

#
# IRC
#

#across
across3 = Dialog()
across2 = Dialog(nextdlg=across3)
across1 = Dialog(nextdlg=across2)
across6 = Dialog(nextdlg=across1, showentities=['ircEol'])
across5 = Dialog(nextdlg=across1)
across4 = Dialog(nextdlg=across1)
across1.lines.append( dict(line="<yoosef> wb") )
across1.lines.append( dict(line="<chris_> hi") )
across1.lines.append( dict(line="*** silence 3 hours ***") )
across2.lines.append( dict(line="<ville_j> i'm pro") )
across2.lines.append( dict(line="*** silence 5 hours ***") )
options = []
options.append( Option("What's funny?", enterdlg=across4) )
options.append( Option("Where's eol?", enterdlg=across5) )
options.append( Option("You going to mars?", enterdlg=across6) )
across3.lines.append( dict(line="<Orcc> håhå, funny in eol", options=options) )
across4.lines.append( dict(line="*** silence 2 hours ***") )
across5.lines.append( dict(line="<Orcc> o,o") )
across6.lines.append( dict(line="<Orcc> .") )

#irc_eol
eol1 = Dialog(showentities=['nekitbattleNekit'])
eol1.lines.append( dict(line="<Mz> battle pls?") )
eol1.lines.append( dict(line="<Nekit> )") )
eol1.lines.append( dict(line="<Nekit> hill?") )
eol1.lines.append( dict(line="<Mz> wheres battle :") )
eol1.lines.append( dict(line="<Mz> :D") )

abulaIrc3 = Dialog(showentities=['elmalandNin2', 'ircAcross'], hideentities=['elmalandMarkku'])
abulaIrc1 = Dialog()
abulaIrc1a = Dialog(nextdlg=abulaIrc1)
abulaIrc1b = Dialog(nextdlg=abulaIrc1)
abulaIrc1c = Dialog(nextdlg=abulaIrc1, showentities=['mopolautaTt'], hideentities=['ircAcross'])
abulaIrc2 = Dialog()

options = []
options.append( Option("not really", enterdlg=abulaIrc1a) )
options.append( Option("well..", enterdlg=abulaIrc1b) )
options.append( Option("what?", enterdlg=abulaIrc1c) )
abulaIrc1.lines.append( dict(line="<Abula> you cheated?", options=options) )
abulaIrc1a.lines.append( dict(line="<Abula> not?") )
abulaIrc1a.lines.append( dict(line="<Abula> are you a ribot follower?") )
abulaIrc1b.lines.append( dict(line="<Abula> well what?") )
abulaIrc1b.lines.append( dict(line="<Abula> did you talk to ribot?") )
abulaIrc1c.lines.append( dict(line="<Abula> your IP was logged on mopolauta") )
abulaIrc1c.lines.append( dict(line="<Abula> you replied on cheat topic") )
abulaIrc1c.lines.append( dict(line="<Abula> ban") )
abulaIrc1c.lines.append( dict(line="<Abula> reason: ribot follower") )

abulaIrc2.lines.append( dict(line="<Abula> niN didn't talk to me yet") )

abulaIrc3.lines.append( dict(line="<Abula> unbanned for now") )

berhIrc1 = Dialog(showentities=['worldMind'])
berhIrc1.lines.append( dict(line="<berh> oh yu had 39tt?") )
berhIrc1.lines.append( dict(line="<berh> yu alredy know how to xiit?") )
berhIrc1.lines.append( dict(line="<berh> well then...") )
berhIrc1.lines.append( dict(line="<berh> i tell you this:") )
berhIrc1.lines.append( dict(line="<berh> ribot") )
berhIrc1.lines.append( dict(line="<berh> is coming to irc") )
berhIrc1.lines.append( dict(line="<berh> soon") )

ribotIrc2 = Dialog()
ribotIrc1 = Dialog(nextdlg=ribotIrc2)
ribotIrc1.lines.append( dict(line="<ribot> what can i do for you?") )
ribotIrc1.lines.append( dict(line="<ribot> your mission statement?") )
ribotIrc1.lines.append( dict(line="<ribot> hmm let's see") )
ribotIrc1.lines.append( dict(line="<ribot> did you talk to niN?") )
ribotIrc1.lines.append( dict(line="<ribot> oh oke") )
ribotIrc1.lines.append( dict(line="<ribot> did you go to miranda?") )
ribotIrc1.lines.append( dict(line="<ribot> i see") )
ribotIrc1.lines.append( dict(line="<ribot> did ville_j find a date?") )
ribotIrc1.lines.append( dict(line="<ribot> oh so it's under control?") )
ribotIrc1.lines.append( dict(line="<ribot> so it took 30 years?") )
ribotIrc1.lines.append( dict(line="<ribot> anyway, did you join 39 mins club?") )
ribotIrc1.lines.append( dict(line="<ribot> oh you did find ribot?") )
ribotIrc1.lines.append( dict(line="<ribot> well then") )
ribotIrc1.lines.append( dict(line="<ribot> your next mission is...") )
ribotIrc1.lines.append( dict(line="<ribot> stop playing this game") )
ribotIrc1.lines.append( dict(line="<ribot> go to mopolauta") )
ribotIrc1.lines.append( dict(line="<ribot> tell them you finished") )
ribotIrc1.lines.append( dict(line="<ribot> hurry up!") )
ribotIrc1.lines.append( dict(line="<ribot> before anyone is ahead of you") )
ribotIrc2.lines.append( dict(line="*** GAME OVER ***") )
ribotIrc2.lines.append( dict(line="*** 3D GFX - internet ***") )
ribotIrc2.lines.append( dict(line="*** STORY - ribot ***") )
ribotIrc2.lines.append( dict(line="*** PROGRAMMING - ribot ***") )
ribotIrc2.lines.append( dict(line="*** EPILOGUE: ***") )
ribotIrc2.lines.append( dict(line="*** Because of your efforts ***") )
ribotIrc2.lines.append( dict(line="*** This future was created: ***") )
ribotIrc2.lines.append( dict(line="*** MoSH-MaN prevented climate change ***") )
ribotIrc2.lines.append( dict(line="*** epp became a pro coder ***") )
ribotIrc2.lines.append( dict(line="*** Orcc went to mars ***") )
ribotIrc2.lines.append( dict(line="*** jonsykkel got back to coking and cofing ***") )
ribotIrc2.lines.append( dict(line="*** lousku still didn't like to do fan service ***") )
ribotIrc2.lines.append( dict(line="*** onla traveled into other dimensions ***") )
ribotIrc2.lines.append( dict(line="*** niN and RoniMox had many new höylä children ***") )
ribotIrc2.lines.append( dict(line="*** Abula lost the power to ban anyone ***") )
ribotIrc2.lines.append( dict(line="*** [FM] did not stop any more people from touching flowers ***") )
ribotIrc2.lines.append( dict(line="*** berh and milagros became best friends ***") )
ribotIrc2.lines.append( dict(line="*** Bjenn became a buddhist monk ***") )
ribotIrc2.lines.append( dict(line="*** he now has compassion for you ***") )
ribotIrc2.lines.append( dict(line="*** and ribot... ***") )
ribotIrc2.lines.append( dict(line="*** well, ribot was doing more ribot stuff ***") )
ribotIrc2.lines.append( dict(line="*** which you know very little about ***") )
ribotIrc2.lines.append( dict(line="*** still today ***") )
ribotIrc2.lines.append( dict(line="*** and kumiorava ***") )
ribotIrc2.lines.append( dict(line="*** kept doing kumiorava stuff ***") )
ribotIrc2.lines.append( dict(line="*** which you also have no clue about ***") )
ribotIrc2.lines.append( dict(line="*** good bye ***") )
ribotIrc2.lines.append( dict(line="*** ps. ***") )
ribotIrc2.lines.append( dict(line="*** Nekit found his true love ***") )
ribotIrc2.lines.append( dict(line="*** ps2. ***") )
ribotIrc2.lines.append( dict(line="*** go to mopolauta ***") )
ribotIrc2.lines.append( dict(line="*** NOW!!! ***") )

#
# NEKIT
#
nekit1 = Dialog()
nekit4 = Dialog(showentities=['nekitbattleVille_j'], nextdlg=nekit1)
nekit2 = Dialog(nextdlg=nekit1)
nekit3 = Dialog(nextdlg=nekit1)

# nekit battle
nekit1.lines.append( dict(line="<Nekit> im here)") )
nekit1.lines.append( dict(line="<Nekit> )") )
options = []
options.append( Option("Alina", enterdlg=nekit2) )
options.append( Option("ALina", enterdlg=nekit4) )
options.append( Option("Anila", enterdlg=nekit3) )
nekit1.lines.append( dict(line="<Nekit> girl in which im in love = ?", options=options) )

nekit2.lines.append( dict(line="<Nekit> Alina=?") )
nekit3.lines.append( dict(line="<Nekit> Anila=?") )

nekit4.lines.append( dict(line="<Nekit> poss :D)))") )
nekit4.lines.append( dict(line="<Nekit> ez helpe just)") )
nekit4.lines.append( dict(line="<Nekit> i like her morally") )

#
# VILLE J
#
ville_j1 = Dialog(showentities=['nekitbattlePlay','mopolautaXiit'])
# nekit battle
ville_j1.lines.append( dict(line="<ville_j> shit game") )
ville_j1.lines.append( dict(line="<ville_j> shit lev") )
ville_j1.lines.append( dict(line="<ville_j> (yet i made uphill generator)") )

#
# NIN & RONIMOX
#

nin7 = Dialog()
nin6 = Dialog(nextdlg=nin7, showentities=['worldMiranda'])
nin5 = Dialog(showentities=['worldNabland', 'ircAbula2'], hideentities=['ircAbula'])
nin4 = Dialog()
nin4a = Dialog(nextdlg=nin4)
nin4b = Dialog(nextdlg=nin4)
nin3 = Dialog(nextdlg=nin4)
nin2 = Dialog(nextdlg=nin3)
nin1 = Dialog(nextdlg=nin2)
nin1.lines.append( dict(line="<niN> oh hi :)") )
nin1.lines.append( dict(line="<niN> berh lied to me about MopoGirl..") )
nin1.lines.append( dict(line="<niN> in Elmaland RPG™") )
nin1.lines.append( dict(line="<niN> oops") )
nin1.lines.append( dict(line="<niN> sorry for spoiler") )
nin1.lines.append( dict(line="<niN> so I found mopogirl and banged it :)") )

nin2.lines.append( dict(line="<RoniMox> mopogirl?") )
nin2.lines.append( dict(line="<RoniMox> the name's RONI MOX, mopoboy") )
nin2.lines.append( dict(line="<RoniMox> banged???") )
nin2.lines.append( dict(line="<niN> :)") )
nin2.lines.append( dict(line="<RoniMox> IT?") )
nin2.lines.append( dict(line="<niN> ;)") )
nin2.lines.append( dict(line="<RoniMox> IT???") )
nin2.lines.append( dict(line="<niN> ;) ;)") )
nin2.lines.append( dict(line="<RoniMox> IT???!!!111 :'''''''(((((((") )
nin2.lines.append( dict(line="<niN> ;) ;) ;)") )

nin3.lines.append( dict(line="<RoniMox> WTF???") )
nin3.lines.append( dict(line="<RoniMox> :(((") )
nin3.lines.append( dict(line="<niN> just kidding sweety") )
nin3.lines.append( dict(line="<niN> you know i luv ya") )
nin3.lines.append( dict(line="<RoniMox> o,o") )

nin4.lines.append( dict(line="<niN> anyways :)") )
nin4.lines.append( dict(line="<niN> you forgot who you are?") )
options = []
options.append( Option("ask about your name", enterdlg=nin4a) )
options.append( Option("ask about ribot", enterdlg=nin4b) )
options.append( Option("talk to niN", enterdlg=nin5) )
nin4.lines.append( dict(line="<RoniMox> I remember you", options=options) )
nin4a.lines.append( dict(line="<RoniMox> your name? can't remember...") )
nin4b.lines.append( dict(line="<RoniMox> ribot told me you'd come") )

nin5.lines.append( dict(line="<niN> so you found ribot yet?") )
nin5.lines.append( dict(line="<niN> hmmz... probably nobody knows where he is") )
nin5.lines.append( dict(line="<niN> oh Abula banned you? :)") )
nin5.lines.append( dict(line="<niN> I'll talk to him, don't worry :)") )
nin5.lines.append( dict(line="<RoniMox> nabs like you should just go to nabland n_n") )

nin6.lines.append( dict(line="<niN> where Miranda is?") )
nin6.lines.append( dict(line="<niN> well... I'll show you on the map") )

nin7.lines.append( dict(line="<niN> sure I like Miranda") )
nin7.lines.append( dict(line="<niN> but I gotta stay in Elmaland") )
nin7.lines.append( dict(line="<niN> I own it now") )
nin7.lines.append( dict(line="<RoniMox> WE own it now") )

#
# BARTEK
#
bartek1 = Dialog()
bartek1a = Dialog(nextdlg=bartek1)
bartek1b = Dialog(nextdlg=bartek1)
bartek1c = Dialog(nextdlg=bartek1)
bartek1d = Dialog(nextdlg=bartek1)
bartek2 = Dialog(nextdlg=bartek1, showentities=['elmalandMarkku'], hideentities=['elmalandNin'])
bartek3 = Dialog(showentities=['ircZweq'])

options = []
options.append( Option("ask about your name", enterdlg=bartek1a) )
options.append( Option("ask about ribot", enterdlg=bartek2) )
options.append( Option("ask about lost internals", enterdlg=bartek1b) )
options.append( Option("ask about Abula", enterdlg=bartek1c) )
options.append( Option("ask about Ramone", enterdlg=bartek1d) )
bartek1.lines.append( dict(line="<BarTek> what do you want nab?", options=options) )
bartek1a.lines.append( dict(line="<BarTek> yuor name?") )
bartek1a.lines.append( dict(line="<BarTek> nevar seen you before nab") )
bartek1b.lines.append( dict(line="<BarTek> ah yes") )
bartek1b.lines.append( dict(line="<BarTek> them LOST INTERNALZ™") )
bartek1b.lines.append( dict(line="<BarTek> YOU MUST FIND") )
bartek1b.lines.append( dict(line="<BarTek> THEM") )
bartek1b.lines.append( dict(line="<BarTek> they are best thing that happened") )
bartek1b.lines.append( dict(line="<BarTek> even Balazs approved of them") )
bartek1c.lines.append( dict(line="<BarTek> Abula?") )
bartek1c.lines.append( dict(line="<BarTek> he banned you?!") )
bartek1c.lines.append( dict(line="<BarTek> if he banned you...") )
bartek1c.lines.append( dict(line="<BarTek> it's because you deserve it!") )
bartek1c.lines.append( dict(line="<BarTek> nab") )
bartek1d.lines.append( dict(line="<BarTek> Ramone?") )
bartek1d.lines.append( dict(line="<BarTek> he's not even in this game") )
bartek1d.lines.append( dict(line="<BarTek> why?") )
bartek1d.lines.append( dict(line="<BarTek> because he didn't make any lost internals") )
bartek2.lines.append( dict(line="<BarTek> you looking for ribot?") )
bartek2.lines.append( dict(line="<BarTek> forget about ribot!") )
bartek2.lines.append( dict(line="<BarTek> you must find...") )
bartek2.lines.append( dict(line="<BarTek> TEH LOST INTERNALZZZ!!!11") )

bartek3.lines.append( dict(line="<BarTek> TEH LOST INTERNALZZZ!!!11") )
bartek3.lines.append( dict(line="<BarTek> you founed?") )
bartek3.lines.append( dict(line="<BarTek> i lost 3") )
bartek3.lines.append( dict(line="<BarTek> oke i tell u secret") )
bartek3.lines.append( dict(line="<BarTek> for tt") )
bartek3.lines.append( dict(line="<BarTek> if u find all") )

#
# LABS
#
labs1 = Dialog()

labs1.lines.append(dict(line="<Labs> why am i in nabland?"))
labs1.lines.append(dict(line="<Labs> i'm not a nab"))

#
# MARKKU
#
markku1 = Dialog()
markku2 = Dialog(nextdlg=markku1, showentities=['ircAbula3'], hideentities=['ircAbula2'])
markku1a = Dialog(nextdlg=markku1)
markku1b = Dialog(nextdlg=markku1)
markku1c = Dialog(nextdlg=markku1)
markku1d = Dialog(nextdlg=markku1)
markku2a = Dialog(nextdlg=markku1)
markku2b = Dialog(nextdlg=markku1)
markku2c = Dialog(nextdlg=markku1)

options = []
options.append( Option("ask about ribot", enterdlg=markku1a) )
options.append( Option("ask about immense coldness", enterdlg=markku1b) )
options.append( Option("ask about absurdness", enterdlg=markku1c) )
options.append( Option("ask about lost internals", enterdlg=markku1d) )
markku1.lines.append( dict(line="<Markku> yes?", options=options) )
markku1a.lines.append( dict(line="<Markku> ribot?") )
options = []
options.append( Option("where is Miranda?", enterdlg=markku2) )
options.append( Option("what is Miranda?", enterdlg=markku2a) )
options.append( Option("are you in [FM]?", enterdlg=markku2b) )
options.append( Option("have you been in Miranda?", enterdlg=markku2c) )
markku1a.lines.append( dict(line="<Markku> he is in Miranda of course", options=options) )
markku1b.lines.append( dict(line="<Markku> your body was liek immense coldness -> commence illness") )
markku1c.lines.append( dict(line="<Markku> nat absurd at all when you don't think about it") )
markku1d.lines.append( dict(line="<Markku> lost internals?") )
markku1d.lines.append( dict(line="<Markku> didn't try them") )

markku2.lines.append( dict(line="<Markku> where Miranda is?") )
markku2.lines.append( dict(line="<Markku> I really don't know") )
markku2a.lines.append( dict(line="<Markku> it's ribot's homeland") )
markku2b.lines.append( dict(line="<Markku> yes, i think so") )
markku2b.lines.append( dict(line="<Markku> why?") )
markku2b.lines.append( dict(line="<Markku> Abula said so") )
markku2c.lines.append( dict(line="<Markku> no, not really") )
markku2c.lines.append( dict(line="<Markku> ribot explained how to go there") )
markku2c.lines.append( dict(line="<Markku> but it didn't make any sense") )

#
# CSYBE
#
csybe7 = Dialog(showentities=['mirandaOnla', 'mirandaSleap', 'mirandaEpp'])
csybe6 = Dialog(nextdlg=csybe7)
csybe5 = Dialog(nextdlg=csybe6)
csybe4 = Dialog(nextdlg=csybe5)
csybe3 = Dialog(nextdlg=csybe4)
csybe2 = Dialog(nextdlg=csybe3)
csybe1 = Dialog(nextdlg=csybe2, showentities=['mirandaCsybe'])

csybe1.lines.append( dict(line="<csybe> pǝʇɐʌᴉʇɔɐ uoᴉsuǝdsns-bǝʍz") )
csybe1.lines.append( dict(line="<csybe> oops") )
csybe1.lines.append( dict(line="<csybe> zweq-suspension activated") )
csybe1.lines.append( dict(line="<csybe> ribot?") )
csybe1.lines.append( dict(line="<csybe> i'm not ribot") )

csybe2.lines.append( dict(line="<csybe> i'm a device with which you can communicate with team [KARMA]") )
csybe2.lines.append( dict(line="<csybe> ribot does not identify with the human mind-body singularity") )
csybe2.lines.append( dict(line="<csybe> you want to find ribot?") )
csybe2.lines.append( dict(line="<csybe> wait an minute...") )

csybe3.lines.append( dict(line="<csybe> let me hook you up with...") )

# sparrow
csybe4.lines.append( dict(line="<sparrow> hello, are you there?") )

csybe5.lines.append( dict(line="<sparrow> hey there!") )
csybe5.lines.append( dict(line="<sparrow> are you alright?") )
csybe5.lines.append( dict(line="<sparrow> how's everything been so far?") )

csybe6.lines.append( dict(line="<sparrow> oh you forgot everything...") )
csybe6.lines.append( dict(line="<sparrow> don't worry") )
csybe6.lines.append( dict(line="<sparrow> we prepared for this") )

csybe7.lines.append( dict(line="<sparrow> let's take you back to 2046") )
csybe7.lines.append( dict(line="<sparrow> (that's forward for you)") )
csybe7.lines.append( dict(line="<sparrow> kuchitsu proved ribot's old theory mathematically") )
csybe7.lines.append( dict(line="<sparrow> that levels were indeed levels") )
csybe7.lines.append( dict(line="<sparrow> not merely tracks") )
csybe7.lines.append( dict(line="<sparrow> levels in the way of fractal holograms") )
csybe7.lines.append( dict(line="<sparrow> where varying density creates loopholes in spacetime") )
csybe7.lines.append( dict(line="<sparrow> which is why elasto mania has to run in low gravity (lunar)") )
csybe7.lines.append( dict(line="<sparrow> or high pressure (aquatic)") )
csybe7.lines.append( dict(line="<sparrow> oh, ribot was wrong about that?") )
csybe7.lines.append( dict(line="<sparrow> more wrong than jonsykkel apparently") )
csybe7.lines.append( dict(line="<sparrow> anyway...") )
csybe7.lines.append( dict(line="<sparrow> bounces create anamolies in spacetime") )
csybe7.lines.append( dict(line="<sparrow> if the wheel breaks out of the topology of a level") )

#
# ONLA
#
onla1 = Dialog()

onla1.lines.append( dict(line="<onla> as milagros had thought that levels were tracks") )
onla1.lines.append( dict(line="<onla> elma2 took decades to complete") )
onla1.lines.append( dict(line="<onla> after kuchitsu's discovery, smibu had to start over") )
onla1.lines.append( dict(line="<onla> coding chris-bits with quantum computers") )

#
# SLEAP
#
sleap1 = Dialog()

sleap1.lines.append( dict(line="<sleap> jonsykkel became president of elmaland") )
sleap1.lines.append( dict(line="<sleap> because of his new level JUNP2") )
sleap1.lines.append( dict(line="<sleap> the best level ever made") )
sleap1.lines.append( dict(line="<sleap> but he got corrupted because of this: human centipede") )
sleap1.lines.append( dict(line="<sleap> and his coking skilz") )
sleap1.lines.append( dict(line="<sleap> although he mastered milagros' coding skills") )
sleap1.lines.append( dict(line="<sleap> in the long run he couldn't compete with team [KARMA]") )

#
# EPP
#
epp1 = Dialog( showentities=['mirandaAnpalcactus'] )

epp1.lines.append( dict(line="<epp> kuchitsu made yet another discovery") )
epp1.lines.append( dict(line="<epp> that milagros never could figure out:") )
epp1.lines.append( dict(line="<epp> ...") )
epp1.lines.append( dict(line="<epp> it was this:") )
epp1.lines.append( dict(line="<epp> reverse alovolt.") )

#
# ANPAL CACTUS
#
anpalcactus1 = Dialog(showentities=['mirandaAkb'])

anpalcactus1.lines.append( dict(line="<anpalcactus> It was a new elma2 team which first did it.") )
anpalcactus1.lines.append( dict(line="<anpalcactus> Team [KARMA] which ribot started.") )
anpalcactus1.lines.append( dict(line="<anpalcactus> Spef was the top player of all time.") )
anpalcactus1.lines.append( dict(line="<anpalcactus> Even though there was one whose skills...") )
anpalcactus1.lines.append( dict(line="<anpalcactus> No it wasn't ZWEQ") )
anpalcactus1.lines.append( dict(line="<anpalcactus> ZWEQ could just not believe Abula manipulated him") )
anpalcactus1.lines.append( dict(line="<anpalcactus> In elma2 second generation") )
anpalcactus1.lines.append( dict(line="<anpalcactus> [FM] decided without discussion") )
anpalcactus1.lines.append( dict(line="<anpalcactus> who was allowed to touch flowers") )
anpalcactus1.lines.append( dict(line="<anpalcactus> Abula alone chose who could join [FM]") )
anpalcactus1.lines.append( dict(line="<anpalcactus> and they could never get caught cheating") )

#
# AKB
#
akb1 = Dialog(showentities=['mirandaXarthok'])

akb1.lines.append( dict(line="<AKB> hi benson you are chinese") )
akb1.lines.append( dict(line="<AKB> EVERYBODY WALK THE DINOSAUR") )

#
# XARTHOK
#
xarthok1 = Dialog(showentities=['mirandaTwipley'])

xarthok1.lines.append( dict(line="<Xarthok> eol2 started a new social media team") )
xarthok1.lines.append( dict(line="<Xarthok> with SveinR, Lousku and yoosef") )
xarthok1.lines.append( dict(line="<Xarthok> this team was maintaining the communications") )
xarthok1.lines.append( dict(line="<Xarthok> and was also hosting EOL2 battles, league and cups") )
xarthok1.lines.append( dict(line="<Xarthok> Kopaka? he was too depressed...") )
xarthok1.lines.append( dict(line="<Xarthok> team [KARMA] exceled too quickly in ranks") )
xarthok1.lines.append( dict(line="<Xarthok> but milagros couldn't detect any cheats") )
xarthok1.lines.append( dict(line="<Xarthok> team [FM] kept changing the physics of elma2") )
xarthok1.lines.append( dict(line="<Xarthok> so that Karlis and jokke could win") )
xarthok1.lines.append( dict(line="<Xarthok> and make it harder to cheat") )
xarthok1.lines.append( dict(line="<Xarthok> Balazs had not approved of this") )
xarthok1.lines.append( dict(line="<Xarthok> but could not care enough to ever contact the community") )
xarthok1.lines.append( dict(line="<Xarthok> it had the opposite effect of what team [FM] had hoped") )
xarthok1.lines.append( dict(line="<Xarthok> Jappe2 could adapt faster than anyone on the bike") )
xarthok1.lines.append( dict(line="<Xarthok> and kuchitsu in the Labs") )
xarthok1.lines.append( dict(line="<Xarthok> Jappe2 was said to be the best player") )
xarthok1.lines.append( dict(line="<Xarthok> until Spef joined [KARMA], much later") )
xarthok1.lines.append( dict(line="<Xarthok> yes there was one more") )
xarthok1.lines.append( dict(line="<Xarthok> one player, thought to be even betterh than Spef") )
xarthok1.lines.append( dict(line="<Xarthok> but he never played") )

#
# TWIPLEY
#
twipley1 = Dialog(showentities=['mirandaXiphias'])

twipley1.lines.append( dict(line="<Twipley> the ONE could already travel across dimensions with this:") )
twipley1.lines.append( dict(line="<Twipley> across") )
twipley1.lines.append( dict(line="<Twipley> he would not compete for there was no competition") )
twipley1.lines.append( dict(line="<Twipley> BarTek helped team [FM] by hiding the internals") )
twipley1.lines.append( dict(line="<Twipley> to promote his own Lost Internals™") )
twipley1.lines.append( dict(line="<Twipley> he could never join [FM] however") )
twipley1.lines.append( dict(line="<Twipley> years later becoming Abula's bitter enemy") )
twipley1.lines.append( dict(line="<Twipley> that's when it started") )
twipley1.lines.append( dict(line="<Twipley> Jappe2 performed a brutal-reverse-alovolt") )
twipley1.lines.append( dict(line="<Twipley> with a wheel superposition bug bounce") )
twipley1.lines.append( dict(line="<Twipley> this was at the same time as team [KARMA] satellite") )
twipley1.lines.append( dict(line="<Twipley> caught up to team [FM]'s") )
twipley1.lines.append( dict(line="<Twipley> having gone straight in curved space of 4D-ballooniverse") )
twipley1.lines.append( dict(line="<Twipley> the twin paradox collapse occured") )
twipley1.lines.append( dict(line="<Twipley> because of the satallites different acceleration-free speeds") )
twipley1.lines.append( dict(line="<Twipley> the fractals of level vertex were now open") )
twipley1.lines.append( dict(line="<Twipley> and Jappe2 the first backwards time traveler") )

#
# XIPHIAS
#
xiphias1 = Dialog(showentities=['ircKopaka'])

xiphias1.lines.append( dict(line="<xiphias> team [KARMA] contacted ribot's younger self") )
xiphias1.lines.append( dict(line="<xiphias> through dreams") )
xiphias1.lines.append( dict(line="<xiphias> in those days there were attempts to start teams") )
xiphias1.lines.append( dict(line="<xiphias> to prevent a disaster in the 2060's") )
xiphias1.lines.append( dict(line="<xiphias> those teams were team [c0ol] and team [¿]") )
xiphias1.lines.append( dict(line="<xiphias> destroyed by BarTek") )
xiphias1.lines.append( dict(line="<xiphias> the disaster?") )
xiphias1.lines.append( dict(line="<xiphias> jonsykkel joining [FM]") )
xiphias1.lines.append( dict(line="<xiphias> now it's you, kumiorava...") )
xiphias1.lines.append( dict(line="<xiphias> who have been sent to the past to stop the disaster") )
xiphias1.lines.append( dict(line="<xiphias> you must find ribot!") )
xiphias1.lines.append( dict(line="<xiphias> he's the only one who can decode your mission statement") )
xiphias1.lines.append( dict(line="<xiphias> in your parallel dimension anamoly") )
xiphias1.lines.append( dict(line="<xiphias> protip: he's not in the lost internals") )
xiphias1.lines.append( dict(line="<xiphias> protip2: use the interzone suspension") )
xiphias1.lines.append( dict(line="<xiphias> if you want to copy TorInge's style") )

#
# KOPAKA
#
kopaka1 = Dialog()

kopaka1.lines.append( dict(line="<kopaka> lost internals?") )
kopaka1.lines.append( dict(line="<kopaka> BarTek lost them in the world map") )
kopaka1.lines.append( dict(line="<kopaka> ribot?") )
kopaka1.lines.append( dict(line="<kopaka> he has a hideout in Elmaland") )

#
# RIBOT
#
ribot1 = Dialog(showentities=['elmalandRibot'])

ribot1.lines.append( dict(line="<ribotAWAY> ribot can not be reached right now") )

#
# LOST INTERNALS
#
lost29 = Dialog(showentities=['worldLost29', 'nablandBartek2'], hideentities=['nablandBartek'])
lost29.lines.append( dict(line="<BarTek> wooho you founded it!") )

lost54 = Dialog(showentities=['worldLost54', 'nablandBartek2'], hideentities=['nablandBartek'])
lost54.lines.append( dict(line="<BarTek> wooho you founded it!") )

lost55 = Dialog(showentities=['worldLost55', 'nablandBartek2'], hideentities=['nablandBartek'])
lost55.lines.append( dict(line="<BarTek> wooho you founded it!") )

lostinf = Dialog()
lostinf.lines.append( dict(line="<BarTek> oke!") )
lostinf.lines.append( dict(line="<BarTek> yeah!!!") )
lostinf.lines.append( dict(line="<BarTek> you fuond all!!!") )
lostinf.lines.append( dict(line="<BarTek> i tell u secret") )
lostinf.lines.append( dict(line="<BarTek> for tt") )
lostinf.lines.append( dict(line="<BarTek> press") )
lostinf.lines.append( dict(line="<BarTek> ...") )
lostinf.lines.append( dict(line="<BarTek> T") )

#
# ZWEQ
#
zweq2 = Dialog()
zweq1 = Dialog(nextdlg=zweq2)

zweq1.lines.append( dict(line="<ZWEQ> TorInge copy my style") )
zweq1.lines.append( dict(line="<ZWEQ> to use new zweq suspension") )
zweq1.lines.append( dict(line="<ZWEQ> you must find 8 koriander") )
zweq1.lines.append( dict(line="<ZWEQ> 3 mushroom") )
zweq1.lines.append( dict(line="<ZWEQ> 20 apples") )

zweq2.lines.append( dict(line="<ZWEQ> or you can just copy TorInge style") )
zweq2.lines.append( dict(line="<ZWEQ> use teh clipboard") )

#
# MIND
#
mind3 = Dialog(showentities=['worldBalazs'])
mind2 = Dialog(nextdlg=mind3)
mind1 = Dialog(nextdlg=mind2)

mind1.lines.append( dict(line="<> hmm") )
mind1.lines.append( dict(line="<> seems I'm inside my mind now") )
mind1.lines.append( dict(line="<> let's review this...") )
mind1.lines.append( dict(line="<> according to ville_j") )
mind1.lines.append( dict(line="<> my mind is part of me") )
mind1.lines.append( dict(line="<> and it is my consciousness") )

mind2.lines.append( dict(line="<> so...") )
mind2.lines.append( dict(line="<> anyone who will talk to me here") )
mind2.lines.append( dict(line="<> is not real") )
mind2.lines.append( dict(line="<> unless others here can see them") )

mind3.lines.append( dict(line="<ribot> hi") )
mind3.lines.append( dict(line="<> hmm?") )
mind3.lines.append( dict(line="<> are you real?") )
mind3.lines.append( dict(line="<ribot> depends what 'real' means to you") )
mind3.lines.append( dict(line="<> can anyone see this?") )
mind3.lines.append( dict(line="<lousk> i can") )
mind3.lines.append( dict(line="<ville_j> not me") )
mind3.lines.append( dict(line="<> hmm...") )
mind3.lines.append( dict(line="<> so this is all just in my mind?") )

#
# BALAZS
#
balazs1  = Dialog(showentities=['ircRibot'])

balazs1.lines.append( dict(line="<Balazs> MILAGROS WAS RIGHT") )
balazs1.lines.append( dict(line="<Balazs> REALITY IS COMPUTER SIMULATION") )
balazs1.lines.append( dict(line="<Balazs> I AM GOD") )
balazs1.lines.append( dict(line="<Balazs> WHY DO I ALLOW THIS SUFFERING") )
balazs1.lines.append( dict(line="<Balazs> IN THIS UNIVERSE?") )
balazs1.lines.append( dict(line="<Balazs> I'M NOT EVIL") )
balazs1.lines.append( dict(line="<Balazs> I JUST DON'T HAVE TIME FOR YOU") )
balazs1.lines.append( dict(line="<Balazs> CSABA?") )
balazs1.lines.append( dict(line="<Balazs> YES, CSABA IS JESUS") )


# xiit: Karlis, I'm team FM, doesn't count; milagros, do you even wr? btw, i'm always right; therefore you are always wrong; berh, you can xiit this game XD
# bartek: this game has wrong internals; pro tip: find lost internals; abula it's ribot stuff; you like or not; also check out our new xiit force
# wcup: dr luni, kopaka
# ville_j nekit battle: i made uphill generator; still i complain about levs; btw, this game sux
# elmaland: niN, berh lied, ribot didn't kill mopogirl; i founeded her and banged her; labs
# mopolauta: sveinR, tj, akb, moshman, jappe2
# irc: jykkel, yoosef (wb), lousku, onla, epp
# RoniMox, xiphias
# toringe: did i dream you are mushroom bread or did you dream i am moshman bread?
# kuchitsu
# TL
# elma 2: smibu (i'm sure elma 2 will be relaeased before 2035)
# kumiorava