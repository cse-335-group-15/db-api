# Uploading to AWS

Run these commands in the root directory of the project to generate the zip file (in powershell)
```powershell
mkdir upload
cp lambda_function.py,api_config.py,endpoints.py .\upload\
cp -r .\venv\Lib\site-packages\* .\upload\
Compress-Archive .\upload\* .\function.zip
rm -r .\upload
```

Then run this command to upload the zip, putting your name into the <username> spot
```
aws lambda update-function-code --function-name cse_335_fall_2024_<username>LambdaFunction --zip-file fileb://function.zip --profile <username>
```
