import os

def title(title):
    os.system(f"title {title}")

def clear():
    os.system("cls")

def pause():
    os.system("pause >nul")


if __name__ == "__main__":
    title("Error")
    print("You can not run this script directly. Press any key to exit.")
    os.system("pause >nul && exit")

