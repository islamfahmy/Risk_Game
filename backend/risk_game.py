#!/usr/bin/env python
# coding: utf-8

# In[248]:


import random
import asyncio
import websockets
import json
import time 


# In[249]:


class Territory:
    adjacent_territories_indices=[]
    adjacent_territories_obj=[]
    color=0
    heuristic=0
    armies=0
    tid=0
    def __init__(self,tid,adjacentTerritories=[],color=0,heuristic=0,armies=0):
        self.adjacent_territories_indices=adjacentTerritories
        self.color=color
        self.heuristic=heuristic
        self.armies=armies
        self.tid=tid
    def __str__(self):
        return "Territory ID: "+str(self.tid)+", color: "+str(self.color)+", heuristic: "+str(self.heuristic)+", armies: "+str(self.armies)
    def BST(self):
      sum=0
      for ter in self.adjacent_territories_obj:
        if(ter.color!=self.color):
          sum+=ter.armies
      return sum
    def BSR(self):
      return self.BST()/self.armies
    def NBSR(self):
      sigmaBSR = 0
      for ter in self.adjacent_territories_obj:
        if(ter.color==self.color):
          sigmaBSR+=ter.BSR()
      return self.BSR()/(self.BSR()+sigmaBSR)
     



# In[ ]:





# In[250]:


class Game:
    gameMap=""
    territories=[]
    state=0
    last_change=None
    last_change_counter=0
    last_armies=None 
    last_attacker= None 
    attack_action=""
    end=False
    def __init__(self,gameMap="Egypt",territories=[],state=0):
        self.gameMap=gameMap
        self.territories=self.setTerritories(gameMap)
        self.state=state
        self.construct_territory_graph()
        
    def setTerritories(self,gameMap="Egypt"):
        if gameMap=="Egypt":
            territories=[None,
                         Territory(tid=1,adjacentTerritories=[4,14],color=0,heuristic=0,armies=0),
                         Territory(2,[22,17,27],color=0,heuristic=0,armies=0),
                         Territory(3,[17,22,24,15],color=0,heuristic=0,armies=0),
                         Territory(4,[1,11,14,13,10,16],color=0,heuristic=0,armies=0),
                         Territory(5,[9,15,11,22,6],color=0,heuristic=0,armies=0),
                         Territory(6,[5,26,20,23,22],color=0,heuristic=0,armies=0),
                         Territory(7,[8,10,16,20,23],color=0,heuristic=0,armies=0),
                         Territory(8,[13,7,10],color=0,heuristic=0,armies=0),
                         Territory(9,[5,11],color=0,heuristic=0,armies=0),
                         Territory(10,[13,4,16,7,8],color=0,heuristic=0,armies=0),
                         Territory(11,[15,5,9,6,20,16,4,14,17],color=0,heuristic=0,armies=0),
                         Territory(12,[23,26,6,18,19],color=0,heuristic=0,armies=0),
                         Territory(13,[10,8,4],color=0,heuristic=0,armies=0),
                         Territory(14,[11,1,4,17],color=0,heuristic=0,armies=0),
                         Territory(15,[11,5,17,3,22],color=0,heuristic=0,armies=0),
                         Territory(16,[4,20,10,11],color=0,heuristic=0,armies=0),
                         Territory(17,[11,14,15,3,24,21,27,2],color=0,heuristic=0,armies=0),
                         Territory(18,[25,12,26,19],color=0,heuristic=0,armies=0),
                         Territory(19,[12,18,23],color=0,heuristic=0,armies=0),
                         Territory(20,[23,16,7,11,6],color=0,heuristic=0,armies=0),
                         Territory(21,[24,27,17,22],color=0,heuristic=0,armies=0),
                         Territory(22,[2,27,21,24,3,15,5,6,26,25],color=0,heuristic=0,armies=0),
                         Territory(23,[12,26,6,20,16,7],color=0,heuristic=0,armies=0),
                         Territory(24,[17,22,3,21],color=0,heuristic=0,armies=0),
                         Territory(25,[18,22,26],color=0,heuristic=0,armies=0),
                         Territory(26,[25,18,12,6,22,23],color=0,heuristic=0,armies=0),
                         Territory(27,[21,2,22,17],color=0,heuristic=0,armies=0),
                        ]
            return territories
    def startGame(self):    
        for turn in range(40):
            if turn%2==0:
                flag=True
                while(flag): 
                    i=random.randrange(1,27)
                    if(self.territories[i].color!=-1):
                        self.territories[i].color=1
                        self.territories[i].armies+=1
                        flag=False
            else:
                flag=True
                while(flag): 
                    i=random.randrange(1,27)
                    if(self.territories[i].color!=1):
                        self.territories[i].color=-1
                        self.territories[i].armies+=1
                        flag=False
        
                    
                    
    def construct_territory_graph(self):
        for ter in self.territories[1:]:
            ter.adjacent_territories_obj=[]
            for adj in ter.adjacent_territories_indices:
                ter.adjacent_territories_obj.append(self.territories[adj])
            


# In[251]:


class Agent:
    game_state=None
    color=0
    owned_territories=[]
    def __init__(self,color,game_state):
        self.color=color
        self.game_state=game_state
        self.owned_territories=[]
        for i in game_state.territories:
            if(i!=None):    
                if i.color == self.color:
                    self.owned_territories.append(i)
              

    def action():
        pass
    def get_new_state(self):
        if self.game_state.last_change != None:
            if(self.game_state.last_change in self.owned_territories):
                self.owned_territories.remove(self.game_state.last_change)
                last_change_counter=0
        #print(str(self.color)+" "+str(len(self.owned_territories)))
        if len(self.owned_territories)==0 or len(self.owned_territories)==27 :
            print("game endeed")
            print(str(len(self.owned_territories)))
            print(str(len(self.owned_territories)))
            print(str(self.game_state.last_change_counter))
            
            self.game_state.end=True
    def place_new_armies(self):
        pass


# In[252]:


class Agressive(Agent):
    def get_crowdest_territory(self):
        current_territory=self.owned_territories[0]
        m=current_territory.armies
        for i in self.owned_territories:
            if i.armies>m:
                m=i.armies
                current_territory=i
        return current_territory
    
    def __str__(self):
        return "Agressive Agent with color: "+str(self.color)+", number of owned territories: "+str(len(self.owned_territories))
    
    def place_new_armies(self):
        new_armies=max(3,int((len(self.owned_territories)/3)))
        max_territory=self.get_crowdest_territory()
        max_territory.armies+=new_armies  
        self.game_state.last_armies=max_territory;
    def action(self):
        self.get_new_state()
        if self.game_state.end==True:
            return
        self.place_new_armies()
        for i in self.owned_territories:
            for k in i.adjacent_territories_obj:
                if k.color== self.color:      
                    continue
                if k.armies+1<i.armies:
                    if i.armies>1:        
                        print(str(i)+" attacked "+str(k))
                        self.game_state.attack_action=str(i)+" attacked "+str(k)
                        k.color=self.color
                        k.armies=i.armies-k.armies
                        i.armies=1
                        self.game_state.territories[k.tid]=k
                        self.game_state.last_change=k
                        self.owned_territories.append(k)
                        self.game_state.last_attacker=i
                        return;
        
        self.game_state.last_change=None
        self.game_state.last_change_counter+=1


# In[253]:


class Passive(Agent):
    def get_least_territory(self):
        current_territory=self.owned_territories[0]
        m=current_territory.armies
        for i in self.owned_territories:
            if i.armies<m:
                m=i.armies
                current_territory=i
        return current_territory    
    def __str__(self):
        return "Passive Agent with color: "+str(self.color)+", number of owned territories: "+str(len(self.owned_territories))
    
    def action(self):
        self.get_new_state()
        if self.game_state.end==True:
            print("end")
            return
        self.place_new_armies()
        self.game_state.last_change_counter+=1
    def place_new_armies(self):
        new_armies=max(3,int((len(self.owned_territories)/3)))
        min_territory=self.get_least_territory()
        min_territory.armies+=new_armies  
        self.game_state.last_change=None
        self.game_state.last_armies=min_territory
    

# In[254]:
class Greedy(Agent) :
    def __str__(self):
        return "Pacifist Agent with color: "+str(self.color)+", number of owned territories: "+str(len(self.owned_territories))
    
    def defensive(self,ter) :
        maxown=0 
        maxenem=0
        for i in ter.adjacent_territories_obj :
            if i.color!=self.color :
                maxenem=max(i.armies,maxenem)
            else : 
                maxown=max(i.armies,maxown)
        return maxown-maxenem;    
    def action(self) :
      self.get_new_state()
      '''
      ter = None max(3,int((len(self.owned_territories)/3)))
      valo = 0 
      for i in self.owned_territories :
         temp = i.NBSR()
         print(temp)
         if temp>valo :
            print("gowa el if"+temp)
            ter = i 
            valo = i.NBSR

      new_armies=max(3,int((len(self.owned_territories)/3)))
      ter.armies+=new_armies'''
      maxTer= None 
      val = -9999999
      a=0
      attacker = None ;
      ra = random.randrange(0,len(self.owned_territories)-1)
      self.owned_territories[ra].armies+=max(3,int((len(self.owned_territories)/3)))
      print("placed " +str(self.owned_territories[ra].armies))
      self.game_state.last_armies=self.owned_territories[ra]
      for i in self.owned_territories :
        for j in i.adjacent_territories_obj :
         if j.color == self.color :
             continue
         if i.armies>j.armies+1 :
            temp = self.defensive(j)
            if temp>val : 
                a=i.armies
                val = temp 
                maxTer=j
                attacker=i 
      self.game_state.last_change=None
      if maxTer == None :
       return 
      self.game_state.attack_action=str(attacker)+" attacked "+str(maxTer)
      maxTer.color=self.color
      maxTer.armies=a- maxTer.armies-1
      attacker.armies=1
      self.owned_territories.append(maxTer)
      self.game_state.last_change=maxTer 
      self.game_state.last_attacker=attacker

class Astar(Agent):
    mp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def __str__(self):
        return "Pacifist Agent with color: "+str(self.color)+", number of owned territories: "+str(len(self.owned_territories))
    
    def defensive(self,ter) :
        maxown=0 
        maxenem=0
        for i in ter.adjacent_territories_obj :
            if i.color!=self.color :
                maxenem=max(i.armies,maxenem)
            else : 
                maxown=max(i.armies,maxown)
        return maxown-maxenem;    
    def action(self) :
      self.get_new_state()
      '''
      ter = None max(3,int((len(self.owned_territories)/3)))
      valo = 0 
      for i in self.owned_territories :
         temp = i.NBSR()
         print(temp)
         if temp>valo :
            print("gowa el if"+temp)
            ter = i 
            valo = i.NBSR

      new_armies=max(3,int((len(self.owned_territories)/3)))
      ter.armies+=new_armies'''
      maxTer= None 
      val = -9999999
      a=0
      attacker = None ;
      ra = random.randrange(0,len(self.owned_territories)-1)
      self.owned_territories[ra].armies+=max(3,int((len(self.owned_territories)/3)))
      print("placed " +str(self.owned_territories[ra].armies))
      self.game_state.last_armies=self.owned_territories[ra]
      for i in self.owned_territories :
        for j in i.adjacent_territories_obj :
         if j.color == self.color :
             continue
         if i.armies>j.armies+1 :
            temp = self.defensive(j)-3*self.mp[j.tid]
            if temp>val : 
                a=i.armies
                val = temp 
                maxTer=j
                attacker=i 
      self.game_state.last_change=None
      if maxTer == None :
       return 
      self.game_state.attack_action=str(attacker)+" attacked "+str(maxTer)
      self.mp[maxTer.tid]+=1
      maxTer.color=self.color
      maxTer.armies=a- maxTer.armies-1
      attacker.armies=1
      self.owned_territories.append(maxTer)
      self.game_state.last_change=maxTer 
      self.game_state.last_attacker=attacker
      


class Pacifist(Passive):
    def __str__(self):
        return "Pacifist Agent with color: "+str(self.color)+", number of owned territories: "+str(len(self.owned_territories))
    
    def action(self):
        self.get_new_state()
        if self.game_state.end==True:
            print("end")
            return
        self.place_new_armies()
        minimum_enemy_armies=10000
        minimum_enemy_territory=None
        for i in self.owned_territories:    
            if i.armies>1:
                for k in i.adjacent_territories_obj: 
                    if k.color== self.color:      
                        continue
                    if k.armies+1<i.armies:
                        if minimum_enemy_armies>k.armies:
                            ally_territory=i
                            minimum_enemy_armies=k.armies
                            minimum_enemy_territory=k
        
        if minimum_enemy_territory!=None:
            print(str(ally_territory)+" attacked "+str(minimum_enemy_territory))

            self.game_state.attack_action=str(ally_territory)+" attacked "+str(minimum_enemy_territory)
            minimum_enemy_territory.color=self.color
            ally_territory.armies=ally_territory.armies-minimum_enemy_armies
            minimum_enemy_territory.armies=1
            #self.game_state.territories[minimum_enemy_territory.tid]=minimum_enemy_territory
            self.game_state.last_change=minimum_enemy_territory
            self.owned_territories.append(minimum_enemy_territory)
            print(len(self.owned_territories))
        else:
            self.game_state.last_change=None
            self.game_state.last_change_counter+=1


# In[266]:

new_game=Game("Egypt")
new_game.startGame()
pacifist= Astar(color=-1,game_state=new_game)
agressive= Astar(color=1,game_state=new_game)
turn = 0
x=[]
i=0;
armi =[]
for ter in new_game.territories:
     if ter==None :
      continue 
     armi.append(ter.armies)
     if ter.color==0 :
        x.append("white")
     if ter.color==1 :
        x.append("blue")
     if ter.color==-1 :
        x.append("red")
     i+=1
async def server(websocket,path) :
  await websocket.send(json.dumps({
    'type':"init",
    "data":{"data":x,
    "armies":armi
    }
    })) 
  turn = 0
  cnt = 0
  while new_game.end==False:
    if turn==0:
        game_state=agressive.action()
    else:
        game_state=pacifist.action()
    turn=(turn+1)%2
    if new_game.last_change==None :
     continue 
    color = "a";
    if new_game.last_change.color==0 :
     color="white";
    if new_game.last_change.color==1 :
      color="blue"
    if new_game.last_change.color==-1 :
      color="red" 
    print("id "+str(new_game.last_change.tid)+" "+"color: "+str(color))
    new_game.attack_action+=" and placed "+str(new_game.last_armies.armies)+"new armies in Territory: "+str(new_game.last_armies.tid)
    await websocket.send(json.dumps({
        'type':"string",
         "data":new_game.attack_action+""
        }))
 
    if new_game.last_armies!=None :
        await websocket.send(json.dumps({
         'type':"army",
         "data":{
         "id":new_game.last_armies.tid,
         "armies":new_game.last_armies.armies
        }
        }))
    if new_game.last_attacker!=None :
        await websocket.send(json.dumps({
         'type':"army",
         "data":{
         "id":new_game.last_attacker.tid,
         "armies":new_game.last_attacker.armies
        }
        }))
    
    await websocket.send(json.dumps({
    'id':cnt,
    'type':"color",
    "data":{
    "id":new_game.last_change.tid,
    "color":color,
    "armies":new_game.last_change.armies
    }
    }))
    cnt+=1 
    time.sleep(0.1)
  print("55555")
  return  

start_server = websockets.serve(server,"localhost",8080)
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever()



    #print(new_game.end)


# In[267]:


for ter in new_game.territories:
    print(ter)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




