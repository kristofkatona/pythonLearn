
# xxxox
# xoooo
# xoxox
# xoxxx
# xooxx
  #####
  
class maptitle:
  def __init__(self, statetextlist, keywordlist):
    self.statetextlist = statetextlist
    self.keywordlist = keywordlist
    self.currentstate = 0
  
  def use(self, object):
    #simplification you can only iterate through states
    state = object in self.keywordlist
    if state:
      self.currentstate = state
      
  def description(self):
  	return self.statetextlist[self.currentstate]
 
  
   
map = { (1,2) : maptitle({"A large gold statue of an exceptionally handsome dragonborn stands before you. His right hand is holding a golden rod.","A large gold statue of an exceptionally handsome dragonborn stands before you. His right hand is empty. A big golden rod lays on the ground", "A large gold statue of an exceptionally handsome dragonborn stands before you. His right hand is empty."},{"cheat","rod"}) 

}