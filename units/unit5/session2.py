# Problem 1 write a method attack() that takes a pokemon object opponent and decreases hp by ther damage amount
# 
class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		newhp = self.hp - self.damage
		if self.hp - self.damage == 0:
			opponent.hp = 0
			print(opponent.name, 'fainted hp')

		else:
			print(self.name, 'dealt', self.damage, 'damage to', opponent.name)
			
pik = Pokemon('pikachu', 40, 400)
bulbasaur = Pokemon('bulbasaur', 20, 200)
opponent = bulbasaur
pik.attack(opponent)

# problem 2 create a normal python list as a linked list

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# problem 3 is to insert the head of the linked list
def add_first(head, new_node):
		pass
		head = new_node
		return new_node
		
node_10 = Node('Squirtle')
node_1 = Node ('Ditto')
node1 = Node('Jigglypuff')
node2 = Node('Wigglypuff')

node_10.next = node_1
node_1.next = node1
node1.next = node2
node_1 = add_first(node_1, node_1)
node_10 = add_first(node_10, node_10)


# print the first node
print(node_10.value, '->', node_10.next.value)
# printing the second node
print(node_1.value, '->', node_1.next.value)
# to create a new head we create a new node then set the new_head =  head &  new_head.next equal to node1

#print the rest of the nodes
print(node1.value, '->', node1.next.value)
print(node2.value, '->', node2.next)

# problem 4

