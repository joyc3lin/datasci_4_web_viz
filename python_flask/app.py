from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg') # required for local development and g-shell
import matplotlib.pyplot as plt
import io
import base64

import warnings
warnings.simplefilter("ignore", UserWarning)

app = Flask(__name__)

# Load the dataset
url = "https://raw.githubusercontent.com/joyc3lin/datasci_4_web_viz/main/dataset/PLACES__Local_Data_for_Better_Health__County_Data_2023_release.csv"
df = pd.read_csv(url)
df_kidney = df[(df['MeasureId'] == 'KIDNEY') & (df['Data_Value_Type'] == 'Age-adjusted prevalence')]

@app.route('/', methods=['GET', 'POST'])
def index():
    counties = sorted(df_kidney['LocationName'].unique())
    selected_county = request.form.get('county') or counties[0]
    
    img = create_plot(selected_county)
    
    return render_template("index.html", counties=counties, selected_county=selected_county, img=img)

def create_plot(county):
    overall_avg = df_kidney['Data_Value'].mean()
    selected_county_avg = df_kidney[df_kidney['LocationName'] == county]['Data_Value'].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(['Selected County', 'Overall Average'], [selected_county_avg, overall_avg], color=['gold', 'forestgreen'])
    ax.axhline(selected_county_avg, color='gray', linestyle='dashed', alpha=0.7)
    ax.set_ylabel('Data Value (Age-adjusted prevalence) - Percent')
    ax.set_ylim(0, 30)
    ax.set_title('kidney Disease Age-adjusted Prevalence Comparison')
    
    # Convert plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return base64.b64encode(img.getvalue()).decode()

if __name__ == '__main__':
    app.run(debug=True)