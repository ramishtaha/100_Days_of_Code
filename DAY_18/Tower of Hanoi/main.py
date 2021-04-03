# Recursive Python function to solve the tower of hanoi
import tower


def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        tower.move(source, destination)
        # tower.print_tower('Source', disks)
        # tower.print_tower('Destination', disks)
        # tower.print_tower('Auxiliary', disks)
        tower.print_towers(disks)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from", source, "to", destination)
    tower.move(source, destination)
    # tower.print_tower('Source', disks)
    # tower.print_tower('Destination', disks)
    # tower.print_tower('Auxiliary', disks)
    tower.print_towers(disks)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


n = disks = int(input("Enter the Number of Disks: "))
tower.init_tower_a(disks)
# tower.print_tower('Source', disks)
# tower.print_tower('Destination', disks)
# tower.print_tower('Auxiliary', disks)
tower.print_towers(disks)
TowerOfHanoi(n, 'Source', 'Destination', 'Auxiliary')
