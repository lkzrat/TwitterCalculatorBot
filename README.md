# __Calculator bot__
#### **Description**: twitter bot made in python that replies tweets with simple math operations with the answer. here is a [video demo](youtube.com).
#### **Twitter account**: [@calculatorbot_](https://twitter.com/calculatorbot_)
#### **How to use it**:
> When the bot is online and someone tweets "*some math operation*" mentioning [@calculatorbot_](https://twitter.com/calculatorbot_), if the *math operation* is in the ***accepted formats*** the bot will reply this tweet with the right answer.
#### ***Accepted formats***:
>- Addition "A + B"
>- Subtraction "A - B"
>- Multiplication "A * B"
>- Division (float) "A / B, (floor) A // B"
>- Exponecial "A ** B"
>- Math Expressions ✅ Ex: ((A + B) / (C - D))**E
>- Floating numbers ✅ (always use a dot)
>- Negative numbers ✅
>- pi(π) and e ✅ Ex: "e ** (2 * pi)" or "e ** (2 * π)"
>- Complex results are instable
#### **How it works**:
>The software has 2 stages:
>- **Searching mentions**: Every 5 seconds the algorithm searchs for tweets with "@calculatorbot_" in it, if there is no metions it prints in the terminal screen "[No mentions found]", else it prints "[x mentions found]" and the software goes to the next stage.
>- **Verifying and replying**: if the tweet isn't in the ***accepted formats*** the bot will reply "Wrong format 😟 look in my profile for ***accepted formats***", else if the tweet was already answered the bot won't do nothing (to check if the tweet was answered or not, the bot uses a .csv file with all the tweet ids of the answered tweets), else the bot will reply the answer and prints "[tweet id, text, answered]" in the terminal screen.
>- **On/Off**: Once you run the code the bot is on, to turn off it just press Cntrl-C in the terminal. When the bot turns on it tweets "I'm online", when it turns off it deletes the "I'm online" tweet
### **Credits**:
>- Created by Luk_dev for CS50py
>- Twitter: [@lkz_rat](https://twitter.com/lkz_rat)
>- Instagram: [@lkz_rat](https://www.instagram.com/lkz_rat/)