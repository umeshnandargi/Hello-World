import openpyxl as xl

wb = xl.load_workbook('emissiondata_refined.xlsx')
sheet = wb['Sheet1']
headcell = sheet['y1']
headcell.value = "Emisssion level"

for row in range(2, sheet.max_row+1):
    co2_cell= sheet[f's{row}']
    co_cell = sheet[f't{row}']
    nox_cell = sheet[f'u{row}']
    particulate_cell = sheet[f'v{row}']
    limit_cell = sheet[f'y{row}']
    if co2_cell.value > 164 or co_cell.value > 219 or nox_cell.value > 231 or particulate_cell.value > 1:
        limit_cell.value = "Beyond limits"
    elif co2_cell.value < 164 and co_cell.value < 219 and nox_cell.value < 231 and particulate_cell.value < 1:
        limit_cell.value = "Under limits"
    else:
        limit_cell.value = "Marginally under limits"

wb.save('corrected_emissions.xlsx')
