import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import pandas as pd 

def format_y(y_value, tick_number):
    if y_value <=200000:
        y_value = str(int(y_value//1000)) + 'k'
    else:
        y_value = ''
    return y_value

def format_x(x_value, tick_number):
    x_value = mdates.num2date(x_value)
    if x_value.year == 2002:
        return x_value.year
    else:
        x_value = x_value.year - 2000
        if x_value < 10:
            return "'0" + str(x_value)
        else:
            return "'" + str(x_value)


gunshot_data = pd.read_csv('CDC_gunshot_injuries.csv', index_col = 0, parse_dates=True, usecols=[0, 1, 10, 11])
gunshot_data.columns = ['Injuries', 'Lower', 'Upper']

#gunshot_data.Injuries = [int(i) for i in gunshot_data.Injuries]

plt.figure(facecolor = '#F0F0F0')
plt.style.use('ggplot')
plt.title("The CDC's gun injury estimates are getting less reliable", fontsize=14, pad=35, fontweight='heavy')
plt.gcf().text(0.1, 0.9, "The CDC's yearly estimates of nonfatal firearm injuries, including the 95% confidence interval for each year", ha='left', wrap=True)
plt.margins(0)
plt.ylim(0, 250000)
plt.tick_params(axis='y', length=0)

ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_y))
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_x))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

ax.fill_between(gunshot_data.index, gunshot_data.Lower, gunshot_data.Upper, facecolor = 'gray', alpha =0.6)
plt.plot(gunshot_data.Injuries, '--', color="white")
plt.gcf().text(0.30, 0.35, 'Estimate', color = 'white', fontsize=13)
plt.plot(gunshot_data.Lower, '-', color = '#000000', linewidth=2.5)
plt.plot(gunshot_data.Upper, '-', color = '#000000', linewidth=2.5)
plt.gcf().text(0.54, 0.54, 'Uncertainty', rotation=22, fontsize=13, fontweight='heavy')

plt.show()
