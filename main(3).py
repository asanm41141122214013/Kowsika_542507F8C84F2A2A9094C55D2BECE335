class AllRounder(Batsman,Bowler):
    def __init__(self):
        Batsman.__init__(self)
        Bowler.__init__(self)
        self.allrounder_rank = 0
    def get_all(self,sr,tr,hs,br,wt,ec,ht,bor,ar):
        Batsman.get_bat(self,sr,tr,hs,br)
        Bowler.get_bowl(self,wt,ec,ht,bor)
        self.allrounder_rank = 
    def disp_all(self):
        self.disp_bat()
        self.disp_bowl()
        print "All Rounder Rank:",self.allrounder_rank