Daily Python Progress repo

#Day 0
Today i discovered that you can create a "__call__" function to make an object callable. I used this while trying to replicate the "Typer" library in python as my first project in this journey. I learned how basic Typer functions and tried my best recreating as much as i understood. My goal for tomorrow is to implement the "--help" and other commands inside my cli.

#Day 1
Today i tried to implement the boolean flags without needing correct order i.e any flag can come before or after any flag. During this i ran into some problems and confusion which i am going to dicuss with my friend helping me with this progress journey. I will try to implement more boolean flags and things that will help developers using my imagination and some inspiration online.

#Day 2
Today was a slow day i didnt have much idea on what to add on my app so i thought of adding a default command, initially my app would run help if no command was specified but now the user can specify default command and if there is no default command then it will run the help command with a message like "there is no default command". I also added the feature of creating aliases for the command by passing in a list "aliases = []" in the decorator.

#Day 3
Today i added support for argument checking, i.e. check if the number of passed arguments match the number of arguments required by the function and check if the passed argument is of same type as required by the function. While doing this i handled the boolean flags seperately and found out a bug in the code that i have fixed now.
