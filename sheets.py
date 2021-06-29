import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import datetime

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


def call_sheets(user, description, amount, action, points):
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("InfiniaPoints").sheet1  # Open the spreadhseet

    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    # data = sheet.get_all_records()  # Get a list of all records
    # pprint(data)
    # row = sheet.row_values(3)  # Get a specific row
    # col = sheet.col_values(3)  # Get a specific column
    # cell = sheet.cell(1, 2).value  # Get the value of a specific cell
    if action == "add":
        points_computed = round(int(amount) * 0.333)
        insertRow = [now, user, description, amount, action, points_computed]
    elif action == "sub":
        insertRow = [now, user, description, "N/A", action, int(points)]

    sheet.append_row(insertRow)  # Insert the list as a row at index 4
    #
    # sheet.update_cell(2, 2, "CHANGED")  # Update one cell

    # numRows = sheet.row_count  # Get the number of rows in the sheet
