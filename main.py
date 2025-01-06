from tkinter import *
import random
import csv

words_game = [
    "apple", "banana", "cat", "dog", "elephant", "flower", "garden", "house", "island", "jungle",
    "king", "lion", "mountain", "night", "ocean", "park", "queen", "river", "sun", "tree",
    "umbrella", "village", "water", "yellow", "zebra", "airplane", "balloon", "car", "door", "egg",
    "fish", "guitar", "hat", "ice", "juice", "kite", "lemon", "music", "notebook", "orange",
    "pencil", "question", "robot", "star", "table", "umbrella", "volcano", "window", "x-ray", "yarn",
    "zebra", "apple", "book", "candy", "dog", "evening", "friend", "gift", "happy", "interesting",
    "jump", "kind", "learn", "moon", "nice", "open", "quiet", "rest", "smile", "talk", "understanding",
    "victory", "work", "exam", "energy", "health", "laugh", "magic", "network", "option", "present",
    "quiet", "rainbow", "swim", "tea", "umbrella", "vacation", "wait", "exercise", "fox", "gold",
    "house", "ice", "jungle", "key", "luck", "moment", "nice", "open", "pear", "quick", "rose",
    "start", "tree", "unique", "voice", "wolf", "xylophone", "yellow", "zebra", "actor", "baker",
    "coach", "doctor", "engineer", "farmer", "gardener", "historian", "inventor", "journalist", "knight",
    "lawyer", "mechanic", "nurse", "officer", "pilot", "queen", "researcher", "singer", "teacher", "uncle",
    "volunteer", "writer", "actress", "balloon", "cactus", "diamond", "elephant", "fireplace", "gorilla",
    "helicopter", "iguana", "jellyfish", "kingfisher", "lighthouse", "mountain", "narwhal", "octopus", "penguin",
    "quail", "rainbow", "snow", "turtle", "unicorn", "volcano", "whale", "x-ray", "yeti", "zigzag",
    "artist", "banana", "cherry", "donut", "envelope", "fortune", "garage", "hat", "iguana", "jump",
    "keychain", "lemon", "melon", "notebook", "octagon", "puzzle", "quilt", "rocket", "sandwich", "train",
    "unicorn", "violin", "wolf", "xmas", "yarn", "zip", "actor", "bicycle", "chef", "doctor", "elephant",
    "flamingo", "goldfish", "helmet", "internet", "jelly", "koala", "lemonade", "monster", "news", "ocean"
]

running = True
time_left = 60
start_points = 0
word_to_give = ""
max_points = 0


def verify_max_points(arg):
    global max_points
    try:
        with open("max_points.txt", mode="r+") as file:
            # Se o argumento for 0, lê o arquivo
            if arg == 0:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Verifica se a linha não está vazia
                        max_points = int(row[0])  # Atualiza max_points com o valor do arquivo
                        print(f"max_points foi atualizado para: {max_points}")
                        break  # Interrompe o loop após ler o valor
                return max_points
            else:
                # Volta ao início do arquivo para reescrever
                file.seek(0)
                writer = csv.writer(file)
                writer.writerow([arg])  # Escreve o novo valor de max_points
                file.truncate()  # Garante que o restante do arquivo (se houver) seja apagado
                print(f"Valor de max_points {arg} foi gravado no arquivo.")
                # Atualiza a interface (presumivelmente uma label)
                record.config(text=f"Record: {verify_max_points(0)}")
    except FileNotFoundError:
        # Se o arquivo não for encontrado, cria o arquivo com valor 0
        print("Arquivo não encontrado. Criando arquivo com valor inicial de 0.")
        with open("max_points.txt", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([0])  # Cria o arquivo com valor 0
        max_points = 0  # Atualiza a variável global max_points
        record.config(text=f"{arg}")

def verify_winner():
    global start_points
    global max_points
    if start_points > max_points:
        verify_max_points(start_points)

def start_counting():
    global running
    reset_counter()
    running = True
    update_timer()
    give_word()

def reset_counter():
    time_counter.config(text="Time: 60:00")
    text_field.delete("1.0", "end-1c")

def stop_button():
    global running
    running = False
    reset_counter()

def give_word():
    global word_to_give
    global words_game
    word_to_give = random.choice(words_game)
    word_roletta.config(text=f"{word_to_give}")

def update_timer():
    global running
    global time_left
    if running:
        if time_left > 0:
            minutes, seconds = divmod(time_left, 60)
            time_counter.config(text=f"Time: {minutes:02}:{seconds:02}")  # Update the label
            time_left -= 1
            # Call the update_timer function again after 1000ms (1 second)
            root.after(1000, update_timer)
            count_words()
        else:
            time_counter.config(text="Time's up!")
            running = False
            verify_winner()

def count_words():
    global start_points
    text = text_field.get("1.0", "end-1c")
    words = text.split(" ")
    text_length = len(words)
    if len(words) >= 0:
        if words[text_length - 1] == "":
            # print(words[text_length - 2])
            if words[text_length - 2] == word_to_give != "":
                start_points += 1
                give_word()
    current_points.config(text=f"Words written: {start_points}")

# region UI
# -----------------------    Window
root = Tk()
root.title("Word counter")
root.minsize(500, 300)
root.config(padx=30, pady=30)
# -----------------------    Labels
# Title
window_title = Label(text="Word Counter", font=("Arial", 21))
window_title.grid(column=0, row=0, columnspan=3)
# Sub-text
sub_title = Label(text="Write the max words you can in 1 minute")
sub_title.grid(column=0, row=1, columnspan=3, padx=(10, 0), pady=(15, 15), sticky="w")
# word to type
word_roletta = Label(text="Press START when ready", font=("Arial", 12, "bold"))
word_roletta.grid(column=0, row=3, columnspan=3, pady=10)
# timer
time_counter = Label(text="Time: 01:00", font=("Arial", 15))
time_counter.grid(column=0, row=6, pady=(15, 5))
# current number of words
current_points = Label(text="Words written: 0", font=("Arial", 12), pady=5)
current_points.grid(column=0, row=7)
# total
record = Label(text=f"Record: {verify_max_points(0)}", font=("Arial", 12), pady=5)
record.grid(column=2, row=7)

# -----------------------    Buttons
# Button Start
button_start = Button(text="START", anchor="center", width=10, command=start_counting)
button_start.grid(column=0, row=5, pady=(5, 5), padx=(15, 5), sticky="w")
# Button Reset
button_reset = Button(text="RESET", anchor="center", width=8, command=reset_counter)
button_reset.grid(column=1, row=5, pady=(5, 5), padx=(0, 5), sticky="nsew")
# Button Stop
button_stop = Button(text="STOP", anchor="center", width=10, command=stop_button)
button_stop.grid(column=2, row=5, pady=(5, 5), padx=(15, 5), sticky="e")
# -----------------------    Entries
# text field
text_field = Text(width=50, height=5)
text_field.grid(column=0, row=2, padx=(10, 5), pady=(5, 10), rowspan=1, columnspan=3)

root.mainloop()
## endregion
