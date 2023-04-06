import tkinter as tk
from tkinter import ttk
import numpy as np

def create_scales():
    # Get the number of Scale bars from the user input
    global num_scales
    num_scales = int(scale_entry.get())
    #num_scales = 20 
    #
    initial_values = [0.0,0.6,0.45,0.45,0.9,1.2,1.5,1.45,1.45,1.45,0.45,0.75,0.45,0.75,1.45,1.65,1.5,1.65,1.8,1.5]
    # Create the specified number of Scale bars with unique names
    for i in range(0, num_scales):
        name = driver_names[i]
        colour = driver_colours[name]
        if i <= (num_scales-1)/2:
            frame = frame1
        else:
            frame = frame2
        scale = tk.Scale(frame, from_=0.0, to=2.5, orient=tk.HORIZONTAL, resolution=0.05, label=name,length=120, troughcolor=colour)
        scale.set(initial_values[i])
        scale.pack(side=tk.TOP, pady=5)
        scales.append(scale)

def start_race():
    global num_scales
    num_scales = int(scale_entry.get())

    global driver_ability
    driver_ability = []
    for scale in scales:
        driver_ability.append(scale.get())

    global weather_condition
    weather_condition = selected_weather.get()
    print(weather_condition)

    global track 
    track = selected_track.get()
    print(track)

    global total_laps
    total_laps = int(selected_lap_count.get())
    print(total_laps)

    lap_times = np.zeros((num_scales, total_laps))

def simulate_qualifying(): 
    # create a list of tuples containing driver name and qualifying time
    driver_qualifying_times = []
    for i, name in enumerate(driver_names):
        quali_time = round(tracks[track]*(1 + weather_penalty(weather_condition)) + driver_ability[i] + np.random.normal(0, 0.5), 3)
        driver_qualifying_times.append((name, quali_time))

    # sort the list of tuples by qualifying time
    driver_qualifying_times.sort(key=lambda x: x[1])

    # recreate the labels in the sorted order
    for i, (name, quali_time) in enumerate(driver_qualifying_times):
        driver_name = tk.Label(table, text=name, bg=driver_colours[name], width=12)
        driver_name.grid(row=i, column=0)

        lap_time = tk.Label(table, text=str(quali_time))
        lap_time.grid(row=i, column=1)


def weather_penalty(weather_condition):
    if (weather_condition in ("Extremely hot", "Sunny", "Cloudy")):
        return 0
    elif (weather_condition == "Damp"):
        return 0.1
    elif (weather_condition == "Rain"):
        return 0.4
    else:
        return 0.8

def simulate_race():
    driver_lap_times = []
    for i, name in enumerate(driver_names):
        lap_times = round(tracks[track]*(1 + weather_penalty(weather_condition)) + driver_ability[i] + np.random.normal(0, 0.5), 3)
        #driver_lap_times.append((name,lap_times))
        driver_lap_times.append((name,cumulative_lap_times[name]))
        cumulative_lap_times[name] = cumulative_lap_times[name] + lap_times

    # sort the list of tuples by qualifying time
    driver_lap_times.sort(key=lambda x: x[1])

    # recreate the labels in the sorted order
    for i, (name, lap_times) in enumerate(driver_lap_times):
        driver_name = tk.Label(race_table, text=name, bg=driver_colours[name], width=12)
        driver_name.grid(row=i, column=0)

        race_time = tk.Label(race_table, text=str(cumulative_lap_times[name]))
        race_time.grid(row=i, column=2)

        fastest_lap = tk.Label(race_table, text=str(lap_times))
        fastest_lap.grid(row=i, column=3)
    pass

driver_names = ["Verstappen","Leclerc","Hamilton","Alonso","Ocon","Norris","Magnussen","Bottas","Albon","Tsunoda",
                "Perez","Sainz","Russell","Stroll","Gasly","Piastri", "Hulkenberg","Zhou","Sargeant","De Vries"]

driver_colours =  {"Verstappen":'#0600EF', "Leclerc":'#DC0000', "Hamilton": '#00D2BE', "Alonso":'#0090FF', "Ocon":'#0090FF', "Norris":'#FF8700',
                    "Magnussen":'#F0D787', "Bottas":'#960018', "Albon":'#005AFF', "Tsunoda":'#000000', "Perez": '#0600EF', "Sainz": '#DC0000',
                    "Russell": '#00D2BE', "Stroll": '#0090FF', "Gasly":'#0090FF',"Piastri":'#FF8700', "Hulkenberg":'#F0D787', "Zhou":'#960018',
                    "Sargeant":'#005AFF',"De Vries":'#000000'}

tracks = {"Albert Park": 76.732, "Bahrain International Circuit": 87.264, "Shanghai International Circuit": 91.095, "Baku City Circuit": 100.495}
         
weather_names = ["Extremely hot","Sunny","Cloudy","Damp","Rain","Extreme wet"]

global cumulative_lap_times
cumulative_lap_times = {"Verstappen":0.0, "Leclerc":0.0, "Hamilton": 0.0, "Alonso":0.0, "Ocon":0.0, "Norris":0.0,
                    "Magnussen":0.0, "Bottas":0.0, "Albon":0.0, "Tsunoda":0.0, "Perez": 0.0, "Sainz": 0.0,
                    "Russell": 0.0, "Stroll": 0.0, "Gasly":0.0,"Piastri":0.0, "Hulkenberg":0.0, "Zhou":0.0,
                    "Sargeant":0.0,"De Vries":0.0}

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
frame4 = tk.Frame(canvas_frame, width=100)
frame4.pack(side=tk.LEFT, padx=20)
frame5 = tk.Frame(canvas_frame)
frame5.pack(side=tk.LEFT, padx=20)

# Create an empty list to hold the Scale widgets
scales = []

# Set the size of the canvas window to fit the contents
canvas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

title_label = tk.Label(frame1, text="Driver ability", font=('Arial', 16, 'bold'))
title_label.pack(side='top', padx=5, pady=5, anchor='nw')

title_label = tk.Label(frame2, text="", font=('Arial', 16, 'bold'))
title_label.pack(side='top', padx=5, pady=5, anchor='nw')

title_label = tk.Label(frame3, text="Race Settings", font=('Arial', 16, 'bold'))
title_label.pack(side='top', padx=5, pady=5, anchor='nw')

title_label = tk.Label(frame4, text="Quali Results", font=('Arial', 16, 'bold'))
title_label.pack(side='top', padx=5, pady=5, anchor='nw')

title_label = tk.Label(frame5, text="Race Results", font=('Arial', 16, 'bold'))
title_label.pack(side='top', padx=5, pady=5, anchor='nw')

#
selected_track = tk.StringVar(root)
selected_track.set(next(iter(tracks)))
track_option_menu = tk.OptionMenu(frame3, selected_track, *tracks)
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

# create a treeview with 3 columns
table = ttk.Treeview(frame4, columns=('Driver','Lap time'))
table.column('Driver', width=100, stretch=tk.NO)
table.column('Lap time', width=100, anchor=tk.CENTER)

# set the column title for the 'name' column
#table.heading('name', text='Name')

# pack the table widget
table.pack()

for i, name in enumerate(driver_names):
    # insert driver name into column 0
    driver_name = tk.Label(table, text=name, bg = driver_colours[name], width=12)
    driver_name.grid(row=i, column=0)

    # insert lap time of 0.0 into column 1
    lap_time = tk.Label(table, text="0.0")
    lap_time.grid(row=i, column=1)

qualify_button = tk.Button(frame4, text="Simulate Qualifying", command=simulate_qualifying)
qualify_button.pack(side='top', pady=10)

# create a treeview with 3 columns
race_table = ttk.Treeview(frame5, columns=('Driver','Finish Position','Interval','Fastest Lap','Pit Strategy'))
race_table.column('Driver', width=100, stretch=tk.NO)
race_table.column('Finish Position', width=100, anchor=tk.CENTER)
race_table.column('Interval', width=100, anchor=tk.CENTER)
race_table.column('Fastest Lap', width=100, anchor=tk.CENTER)
race_table.column('Pit Strategy', width=100, anchor=tk.CENTER)
race_table.pack()

race_button = tk.Button(frame5, text="Start Race", command=simulate_race)
race_button.pack(side='top', pady=10)

for i, name in enumerate(driver_names):
    # insert driver name into column 0
    driver_name = tk.Label(race_table, text=name, bg = driver_colours[name], width=12)
    driver_name.grid(row=i, column=0)

    # insert lap time of 0.0 into column 1
    finish_position = tk.Label(race_table, text=i+1)
    finish_position.grid(row=i, column=1)

    # insert lap time of 0.0 into column 1
    race_time = tk.Label(race_table, text="0.0")
    race_time.grid(row=i, column=2)

    fastest_lap  = tk.Label(race_table, text="200")
    fastest_lap.grid(row=i, column=3)

    pit_strategy = tk.Label(race_table, text="Start: S, Lap 19:  M")
    pit_strategy.grid(row=i, column=4)

# Start the tkinter main loop
root.mainloop()


