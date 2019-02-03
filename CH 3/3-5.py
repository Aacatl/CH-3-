guest_list = ['Jim Morrison', 'Jimi Hendrix', 'Janis Joplin']
message_zero = "Would you like to go out to dinner with me, " +guest_list[0] + "?"
message_one = "Would you like to go out to dinner with me, " +guest_list[1] + "?"
message_two = "Would you like to go out to dinner with me, " +guest_list[2] + "?"

print(message_zero)
print(message_one)
print(message_two)

print(guest_list[1] + "can't make it")

guest_list.remove('Jimi Hendrix')
guest_list.insert(1, 'Rick Sanchez')

print(message_one)