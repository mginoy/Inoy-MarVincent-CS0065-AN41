1.	What rules does the agent follow?
2.	How does the agent decide when to clean and when to move?
3.	What happens if both rooms are already clean at the start?
4.	How would you modify the agent to handle more than two rooms?



Answer the Questions

1. First one is cleaning the room if it is dirty then cleans it. Second is move to another room if it is already cleaned. 

2. The agents checks if it is is_dirty then cleans it if it is true. If it is false it calls move and changes to the other room.

3. It doesn’t have anything to clean so what will happen is it will just go switch rooms in every steps.

4. I think I might not use the names room a and room b. Instead, I will make the rooms names into an ordered list. Then make the agent just scan for dirty rooms then go to it.
