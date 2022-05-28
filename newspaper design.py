# challenge accepted My name is Ayush and im Class 12th
# code
### Practice 2 tkinter news Harry challenge
from tkinter import *

news = Tk()

# defining the geometry of the news paper window
news.geometry("1450x900")

# inserting the ackground color to the window
news.configure(bg = "lightyellow")


# defining the title of the window
news.title("THE TIMES OF INDIA")

#  Inserting the name of the news paper as heading
news_head = Label(text = "THE TIMES OF INDIA", font = "roboto 20 bold", bg = "lightgrey", fg = "black", pady = 10)
news_head.pack(side = TOP, fill = X )

# Insetrting the date of the day 
news_date = Label(text = "1 AUGUST 2021 SUNDAY",font = "roboto 10 bold")
news_date.place(x = 1100, y = 30)

# Inserting the first news text
news_txt = Label(text = """Electric cars to remain in slow lane in India.""", font = "helvetica 20 bold", bg = "grey")
news_txt.place(x = 350, y = 65)

news_txt2 = Label(text = """Shally Seth Mohile\nJanuary 18, 2021
\nAmeya Joshi, a Mumbai-based businessman, bought a Tata Nexon EV in May 2020.
After eight months,Joshi says the experience has been “very satisfying and exhilarating”
Be it the range, charging time, safety or overall driving performance, the Nexon EV ticks 
all the boxes.“I haven’t been near a fuel pump for two months,” says Joshi, 35, who owns 
two other cars powered by petrol and diesel. The stamp of approval by buyers like Joshi 
comes two decades after Chetan Maini, founder of Reva Electric Car Co (RECC),gave India 
its first electric car. The tiny all-electric two-seaterhit the market in 2001 when the 
concept of an electric car was much ahead of its time. Reva failed to gain traction,mainly
because it cost twice as much as a four-seater compact.""", font = "roboto 15 italic", bg = "lightgrey", fg = "black")
news_txt2.place(x = 10, y = 130 )

# inserting the news 2
news_txt_2 = Label(text = "Ola CEO Bhavish Aggarwal shared an image where he claimed to be in a discussion on the launch date of the new scooter", 
                  font = "roboto 15 bold", bg = "grey")
news_txt_2.place(x = 50, y = 430)

# inserting the main 2nd news
news_txt__2 = Label(text = """Ola Electric is in the process of deciding a launch date for their first electric Ola Scooter.
Ola CEO, Bhavish Aggarwal has dropped a tweet hinting that the launch is around the corner.
Additionally, the CEO also launched another poll for the scooter that indicates that the 
company will be providing a unique delivery experience or at least an option for those who 
want it.""", bg = "lightgrey", font = ("roboto 15 italic"))
news_txt__2.place(x = 410, y = 480)

news.mainloop()