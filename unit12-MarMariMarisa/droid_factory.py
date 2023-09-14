import droids
import array_queue
import node_stack
def unload_shipments(filename,belt):
    with open(filename) as file:
        for line in file:
            part = line.strip()
            if part != "":
                belt.enqueue(part)

def install_part(droid,my_belt,their_belt):
    #grab the part from my_belt
    #install part to the droid
    if not my_belt.is_empty():
        part = my_belt.dequeue()
        if droid.needs_part(part):
            droid.install(part)
        else:
            their_belt.enqueue(part)
    return droid.is_complete()

def assemble_droids(my_belt,their_belt):
    container = node_stack.Stack()
    cargo_ship = [] #a list of containers
    #worker number one - assembles protocol droids
    p_number = 0
    protocol = droids.Droid(p_number)
    #worker number 2 - assembles astromech droids
    a_number = 0
    astromech = droids.Droid(a_number,droids.ASTROMECH)
    while not my_belt.is_empty() or not their_belt.is_empty():
        completed = install_part(protocol,my_belt,their_belt)
        if completed:
            #print(repr(protocol))
            container.push(protocol)
            if container.size() == 5:
                cargo_ship.append(container)
                container = node_stack.Stack()
            p_number += 1
            protocol = droids.Droid(p_number)
    #worker number 2 - assembles astromech droids
        completed = install_part(astromech,their_belt,my_belt)
        if completed:
            #print(repr(astromech))
            container.push(astromech)
            if container.size() == 5:
                cargo_ship.append(container)
                container = node_stack.Stack()
            a_number += 1
            astromech = droids.Droid(a_number,droids.ASTROMECH)
    return cargo_ship

def unpack(cargo_ship):
    for container in cargo_ship:
        while not container.is_empty():
            droid = container.pop()
            print(repr(droid))

def main():
    filename = "droid_parts/parts_0005_0005.txt"
    belt = array_queue.Queue()
    unload_shipments(filename,belt)
    their_belt = array_queue.Queue()
    cargo_ship = assemble_droids(belt,their_belt)
    print(cargo_ship)

    unpack(cargo_ship)
    


main()            

