total = 0
print 'How many numbers do you want to add'
swag = raw_input()
swag = int(swag)
for x in range(swag):
    print 'Enter number'
    swagy = raw_input()
    swagy = int(swagy)
    total = total + swagy
    print total
    
total = []
print 'How many numbers do you want to add'
swag = raw_input()
swag = int(swag)
for x in range(swag):
    print 'Enter number'
    swagy = raw_input()
    swagy = int(swagy)
    total.append(swagy)
    print sum(total)
    
list = []
print 'what number would you like to factorial'
swag = int(raw_input())
# [1,2,3,4,5,6]
for x in range(swag):
    total = total * x
    print total 
    

