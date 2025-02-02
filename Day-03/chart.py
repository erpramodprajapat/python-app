#openpyxl:

import openpyxl

from openpyxl.chart import BarChart,Reference

wb=openpyxl.Workbook()

sheet=wb.active

for i in range(10):
    sheet.append([i])

values = Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10)

chart = BarChart()

chart.add_data(values)

chart.title="BAR-CHART"

chart.x_axis.title="X_AXIS"
chart.y_axis.title="Y_AXIS"

sheet.add_chart(chart,"E5")

wb.save("C:\\py-tt\\Day-03\\bar_chart.xlsx")
print("Bar chart created ... open file")

