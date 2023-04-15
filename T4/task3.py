#Reference material from later in the course referred to.
#Assign variables for time to qualify and read input for swimming, cycling and running times.  
qual_t = 100
t_swim = float(input ("How many minutes long was the swim?"))
t_cycl = float(input ("How many minutes long was the cycling?"))
t_run = float(input ("How many minutes long was the run?"))

#calculate and display total triathlon time:
t_total = (float(t_swim + t_cycl + t_run))

#Compare total time to qualifying time to determine award
if (t_total <= qual_t): award = "Provincial Colours"
elif (t_total <= int(qual_t + 5)): award = "Provincial Half Colours"
elif (t_total <= int(qual_t + 10)): award = "Provincial Scroll" 
elif (t_total > qual_t + 10) : award = ("No award")

#Display total time and award status: 
print (f"Total time is {t_total} minutes, {award} awarded")