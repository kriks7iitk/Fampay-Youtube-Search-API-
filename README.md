# Fampay-Youtube-Search-API-


Task completed:

1 - Make API to fetch data using Youtube API in given intervel(1 min) from server side

2 - Make GET API Views to give Json Response for desired querry in paginated response

3 - Make JS function to  request data in given intervel from server in client side

4 - Make Dashboard to view videos album(Bonus Task)

5 - Added filter option to filter data based on date-time or duration of videos(Bonus Task)-----(done in frontend)

Task Not completed :

1 - List of API keys in case quota complete (Bnous Task)


## APIs  - 

Video_list Class(ListAPIview) to list all the video data pagianted by 1   - -url = http://127.0.0.1:8000/search/videolist  -- ------GET API to get all object

Video_detail Class API to render dashboard html page   -URL  =   http://127.0.0.1:8000/search/

Data_Interval Claas(LIstview API) to refresh the data on dashboard at given intervel  -url  = http://127.0.0.1:8000/search/refresh

def get_data()   -  Call in givnen Interval from server side to fetch data in evry one min

def start()    -  utility function to update data   ----used in AppConfig


## Instruction


Before opening make sure that python is installed on your PC
Given project is done using Django Framework and Frontend side development is done using JS,HTML and CSS

----Everything is done in virtual environment is to make easy for other user to open and run website easily without adding extra libraries .so please activate virtual environment before running App---


Step 1 : Go to Master Branch

Step 2 : Download Project file

Step 3 : Unzip File 

Step 5 : cd to env using command prompt

Step 6 : Start virtual env by going to script and run activate in command prompt

step 7 : cd ..  -> cd Youtubeapi  (chabge directory to django project)

step 8 : python manage.py runserver

step 9 : server is ready ..copy given local host address to chrome and view file

