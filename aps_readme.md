
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

### 3. Run the Script
Navigate to the project folder and run:

```bash
python main.py <source_dir> <target_dir>
