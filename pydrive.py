# quickhand commands to manage GDrive

#load libs
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

#auth
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# **Read google drive document (not sheets)**
file_id = "12GsCQMTVr0hwMDk_o7hYAJ0KVJL_XXXXXXXXXXXXXXX"
file_name = 'myfile'
downloaded = drive.CreateFile({'id': file_id})
downloaded.GetContentFile(file_name)

#**Read data from google sheets**

#import libs
from google.colab import auth
import gspread
from google.auth import default

#authorize
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)

#read 'Sheet1' and transform to dataframe

url = 'https://docs.google.com/spreadsheets/d/12GsCQMTVr0hwMDk_o7hYAJ0KVJL_XXXXXXXXXXXXXXX/'
sheet_name = "Sheet1"
def read_sheet(url, sheet_name):
  workbook = gc.open_by_url(url)
  print("Google Sheets workbook loaded. Sheets: ", workbook.worksheets())
  worksheet = workbook.worksheet(sheet_name)
  values = worksheet.get_all_values()
  df = pd.DataFrame.from_records(data = values[1:], columns = values[0])
  return df
read_sheet(url, sheet_name)
