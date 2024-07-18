#pip install flask pandas openpyxl
# uncomment the top line to install prequities

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load the Excel file
file_path = 'SCC WEEK 28 REPORT 2024.xlsx'
excel_data = pd.ExcelFile(file_path)

@app.route('/')
def index():
    # Display the sheet names
    sheet_names = excel_data.sheet_names
    return render_template('index.html', sheet_names=sheet_names)

@app.route('/sheet', methods=['POST'])
def sheet():
    sheet_name = request.form['sheet_name']
    df = excel_data.parse(sheet_name)
    # Convert the dataframe to HTML form
    data_html = df.to_html(classes='data', header="true")
    return render_template('sheet.html', sheet_name=sheet_name, data_html=data_html, columns=df.columns)

@app.route('/edit', methods=['POST'])
def edit():
    sheet_name = request.form['sheet_name']
    df = excel_data.parse(sheet_name)
    
    # Update the dataframe with new values from the form
    for col in df.columns:
        if col in request.form:
            df[col] = request.form.getlist(col)
    
    # Save the updated dataframe back to the Excel file
    with pd.ExcelWriter(file_path, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
