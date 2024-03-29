import pandas
import tkinter as tk
from tkinter import filedialog


def UploadAction():
    filename = filedialog.askopenfile()
    data = pandas.read_csv("{}".format(filename.name),skiprows=1)

    sorted_data = pandas.DataFrame(data).sort_values(["Venue Name", "Venue Area", "Cost"])
    cancelled_refunded_data = sorted_data[(sorted_data["Booking status"] == "cancelled")]


    while len(cancelled_refunded_data.index) > 0:
        first_data = sorted_data.head(1)

        first_data_venue_name = first_data.iloc[0]["Venue Name"]
        first_data_venue_area = first_data.iloc[0]["Venue Area"]

        to_delete_venue_name = sorted_data[sorted_data["Venue Name"] == first_data_venue_name]
        to_delete_venue_area = to_delete_venue_name[to_delete_venue_name["Venue Area"] == first_data_venue_area]

        data_dict = pandas.DataFrame(to_delete_venue_area)
        data_dict.to_csv("{},{}.csv".format(first_data_venue_name, first_data_venue_area))

        sorted_data = sorted_data[(sorted_data["Venue Name"] != first_data_venue_name) | (sorted_data["Venue Area"] != first_data_venue_area)]


root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()
