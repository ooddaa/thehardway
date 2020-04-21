1. Write

Ok it's time to write a game. It will be a very special kind of game. 
I don't know which one yet. But special. 

I need some environment. 
Let it be a room. Which has access to certain parallel universes. But
not to others. One portal will lead to a random place, others will always
lead to the same places. 

No it's a bad idea. Let's simplify. 

We have a house. 

It has 3 floors. There are 3 dors on each level. Only one door on the top 
level leads to the roof where a helicopter is waiting for us. 

So we start on first level and our goal - to leave the building by 
helicopter (mainly because it's cool). But there will be others who don't 
want us to get there without having to listen to their boring stupid ass shit. 
Let's call them 'office workers'. 

So it's a game about leaving an office. Any office. A game about success of 
leaving and perils that await a young Samurai if he does not. 

Of course there's the final Boss, on the roof, nearby the helicopter. Well, it
is worth mentioning, that it is his helicopter. In the beggining of the game. 
But by the time we get to the helicopter and the Boss, we should already have 
changed ownership of the helicopter so that Boss cannot prevent us from flying
away.

To do so you have to guess the password to Boss's laptop which you can obtain
from his secretary if you play it right. If you don't play it right, you end up
in morgue. Pretty simple. Or how a Kyrgiz would put it: 'арларгарды марградыэ'.

So the Samurai begins on first level with 3 doors available for him.


2. Extract 

Office
Office_Workers aka Enemies
Boss
Helicopter
Level
Door
Boring_shit
Secretary
Laptop
Samurai aka the Player

3. Class hierarchy 

* Location  # so that we could extend our game in further locations
    - get_info
    - enter
    * Office
        * Level 
            - leave
    * Morgue
        - restart
    * Roof
* Person
    - get_info
    - talk
    - tell_a_joke
    - gives
    - takes
    * Boss
        - greet
        - bid_farewell
        - reverse_triangle 
    * Office_Worker
        - slap
        - tell_to_f_off
    * Secretary
        - compliment
        - tell_off
    * Samurai
        - check chi 
* Thing
    - get_info
    - destroy
    - steal
    * Helicopter
        - fly_away
    * Door
        - get_info
        - unlock
        - read_the_note
        - go_through
        - return_to_the_level

        * SecretaryDoor
        * BossDoor
        * HRDoor
        * MorgueDoor
        * ToiletDoor
    * Boring_shit
        - listen
        - refuse_to_listen
        - actively_listen
    * Laptop
        - hack

* Map

