import tkinter as tk
import numpy as np

def create_scales():
    # Get the number of Scale bars from the user input
    global num_scales
    num_scales = int(scale_entry.get())
    #
    initial_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    # Create the specified number of Scale bars with unique names
    for i in range(0, num_scales):
        name = driver_names[i]
        if i <= (num_scales-1)/2:
            frame = frame1
        else:
            frame = frame2
        scale = tk.Scale(frame, from_=1, to=100, orient=tk.HORIZONTAL, label=name,length=120)
        scale.set(initial_values[i])
        scale.pack(side=tk.TOP, pady=5)
        scales.append(scale)

def start_race():
    num_scales = int(scale_entry.get())
    driver_ability = []
    for scale in scales:
        driver_ability.append(scale.get())

    weather_condition = selected_weather.get()
    print(weather_condition)

    track = selected_track.get()
    print(track)

    global total_laps
    total_laps = int(selected_lap_count.get())
    print(total_laps)

    lap_times = np.zeros((num_scales, total_laps))

    for i in range(1, total_laps-1):
        generate_lap(lap_times, i, driver_ability, weather_condition)

def generate_lap(lap_times, current_lap, driver_ability, weather_condition):
    lap_times[current_lap] = 10*driver_ability 




driver_names = ["Verstappen","Leclerc","Hamilton","Alonso","Ocon","Norris","Magnussen","Bottas","Albon","Tsunoda",
                "Perez","Sainz","Russell","Stroll","Gasly","Piastri", "Hulkenberg","Zhou","Sargeant","De Vries"]

track_names = [
    "Bahrain International Circuit",
    "Imola Circuit",
    "Algarve International Circuit",
    "Circuit de Barcelona-Catalunya",
    "Circuit de Monaco",
    "Baku City Circuit",
    "Circuit Paul Ricard",
    "Red Bull Ring",
    "Silverstone Circuit",
    "Hungaroring",
    "Spa-Francorchamps",
    "Circuit Zandvoort",
    "Autodromo Nazionale di Monza",
    "Sochi Autodrom",
    "Marina Bay Street Circuit",
    "Suzuka International Racing Course",
    "Circuit of the Americas",
    "Autódromo Hermanos Rodríguez",
    "Autódromo José Carlos Pace",
    "Jeddah Corniche Circuit",
    "Yas Marina Circuit"
]

weather_names = ["Extremely hot","Sunny","Cloudy","Damp","Rain","Extreme wet"]


# Create a tkinter window
root = tk.Tk()
root.title("Scale Example")
root.geometry("1200x800")

# Create a scrollbar and canvas to hold the Scale bars
canvas_scrollbar = tk.Scrollbar(root)
canvas_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas = tk.Canvas(root, yscrollcommand=canvas_scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas_scrollbar.config(command=canvas.yview)

# Create a frame to hold the Scale bars on the canvas
canvas_frame = tk.Frame(canvas)
canvas.create_window((0,0), window=canvas_frame, anchor=tk.NW)

# Create an Entry widget to accept the number of Scale bars from the user
scale_entry = tk.Entry(canvas_frame, width=5)
scale_entry.pack()

# Create a button to create the Scale bars based on the user input
create_button = tk.Button(canvas_frame, text="Create Scales", command=create_scales)
create_button.pack()

# Create two frames to hold the Scale bars
frame1 = tk.Frame(canvas_frame)
frame1.pack(side=tk.LEFT, padx=10)
frame2 = tk.Frame(canvas_frame)
frame2.pack(side=tk.LEFT, padx=10)
frame3 = tk.Frame(canvas_frame)
frame3.pack(side=tk.LEFT, padx=10)

# Create an empty list to hold the Scale widgets
scales = []

# Set the size of the canvas window to fit the contents
canvas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

#
selected_track = tk.StringVar(root)
selected_track.set(track_names[0])
track_option_menu = tk.OptionMenu(frame3, selected_track, *track_names)
track_option_menu.pack(side=tk.TOP, padx=10)

selected_weather = tk.StringVar(root)
selected_weather.set(weather_names[0])
weather_option_menu = tk.OptionMenu(frame3, selected_weather, *weather_names)
weather_option_menu.pack(side=tk.TOP, padx=10)

selected_lap_count = tk.IntVar(root)
selected_lap_count.set(50)

label = tk.Label(frame3, text="Enter the number of laps here")
label.pack()
lap_count_menu = tk.Entry(frame3, text="Lap Count")
lap_count_menu.pack()

start_race_button = tk.Button(frame3, text="Start Race", command=start_race)
start_race_button.pack()










# Start the tkinter main loop
root.mainloop()


