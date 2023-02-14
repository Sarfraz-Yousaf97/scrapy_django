# Usman's Podemon testing
# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iCrawler.settings')
# django.setup()
# import requests
# from django.core import files
# import io
# import os
# import os.path
# import pickle
# from django.conf import settings
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaIoBaseDownload
# # import schedule
# import time
# import tempfile
# import requests
# from  main.models import FreePatent

# # from buzzprout.utils.sendrequest import UploadtoBuzzprout
# file_path = os.path.join(settings.STATIC_ROOT, 'client_secrets.json')
# file_path_token = os.path.join(settings.STATIC_ROOT, 'token.pickle')
# # from get_new_token import get_refresed_token


# def new():
#     SCOPES = ['https://www.googleapis.com/auth/drive']

#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists(file_path_token):
#         with open(file_path_token, 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 file_path, SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open(file_path_token, 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('drive', 'v3', credentials=creds)
#     folder_id = '1sHf1ZcAIr-yluLdealQkmd2QtaK1Bw2c'
#     query  = f"parents ='{folder_id}'"
#     results = service.files().list(
#         q= query,
#         fields="nextPageToken, files(id, name)").execute()
#     items = results.get('files', [])
#     file_ides =[]
#     file_names = []

#     if not items:
#         print('No files found.')
#     else:
#         for item in items:
#             lf = tempfile.NamedTemporaryFile()
#             if item['name'].endswith('.mp3'):
#                 # print(item)
#                 already_downloaded = FreePatent.objects.filter(file_name = item['name']).first()
#                 if not already_downloaded:
#                     # print()
#                     print(item['name'])
#                     #  first 
#                     request = service.files().get_media(fileId=item['id'])
#                     fh = io.BytesIO()
#                     downloader = MediaIoBaseDownload(fd=fh, request= request)
#                     done = False
#                     while not done:
#                         print('Downloading ------------ ')
#                         status, done = downloader.next_chunk()
#                         print(f"[+] Downloading ------- {status.progress()*100} % ")
#                     fh.seek(0)
#                     lf.write(fh.read())
                    
#                     print('[+]  File downloaded ')