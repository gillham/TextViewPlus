py -m make %* 

set /p build=<.build

echo %build%

if "%1" == "final" goto :final

echo TextView+ > about.txt
echo 0 >> about.txt
echo 2024 >> about.txt 
echo %build% >> about.txt
goto :bundle

:final

echo TextView+ > about.txt
echo 1.0 >> about.txt
echo 2024 >> about.txt 
echo Paul Hocker >> about.txt

:bundle

py -m bundleapp
