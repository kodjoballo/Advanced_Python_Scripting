
# ⚡ Advanced Python Scripting

## 📌 Description
This project demonstrates advanced **Python scripting** techniques, focusing on **file management, directory traversal, command-line arguments, and subprocess management**.  

It allows you to:  
- Copy files and directories  
- Search for game-related directories (`*_game`)  
- Compile `.go` files automatically (using the Go compiler)  
- Generate a `metadata.json` file with game details  

This script uses:
- `os` for filesystem operations  
- `sys` for command-line arguments  
- `shutil` for copying directories  
- `subprocess` for running terminal commands (like compiling Go code)  

---

## 🚀 How to Run

### 1. Install Python
Ensure you have **Python 3.x** installed.  

### 2. Install Go
Since this project compiles `.go` files, you must install **Go**:  
👉 [Download Go](https://go.dev/)

Project Steps / Requirements

- Find all game directories from /data
- Create a new game /games directory
- Copy and remove the "game" suffix of all games into the /game directory
- Create a .json file with the information about the games
- Compile all of the game code
- Run all of the game code

### 3. Run the Script
Navigate to the project folder and run:


python main_get_game_data.py <source_dir> <target_dir>

In our case, the source is the data folder

python main_get_game_data.py data target

<p align="center">

![image alt](https://github.com/kodjoballo/Advanced_Python_Scripting/blob/main/Screenshot%202025-08-24%20235703.png?raw=true)

</p>




### Click down 👇 to view the source code 

[source code](https://github.com/kodjoballo/Advanced_Python_Scripting/blob/main/main_get_game_data.py)
