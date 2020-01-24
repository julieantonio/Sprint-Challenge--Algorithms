#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)


b)


c)

## Exercise II
Start from the middle floor (given 100 floors, current_floor=50)
Check if egg breaks when dropped from middle floor(eggs = 1)

If egg breaks, set pointer to middle floor number of bottom set, check if egg breaks from middle floor of bottom set (given 100 floors, current_floor = 25, floor_count = 25, eggs = eggs + 1)

If egg does not break, check if egg breaks from the middle floor of the top set(given 100 floors, current_floor = 75, floor_count=25, eggs = eggs + 1)
Repeat until there is one floor left in the set that is being tested. (floor_count = 1)

The runtime complexity of this solution would be O(log n) because the number of steps taken to get to the solution only increases as n(number of floors) doubles

