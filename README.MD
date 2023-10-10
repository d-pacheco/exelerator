# pdf-populator
Python scripts for populating a pdf from an excel spreadsheet

## Running the pdf populator
- next to `pdf populator.exe` have a `templates` and `data` folder
    - Inside of the templates folder place your template pdfs with the name structure "FileName - Template"
        - Where the FileName is the name of the template, and "- Template" is to inddicate that it is a tempalte file
        - Template will be replaced by the clientname1 outlined in the Python Data sheet
    - Inside of the data folder have your excel spreadsheet that you would like to pull the data from.
        - This excel file needs to have a sheet called "Python Data"
            - Inside this sheet, the first column will contain the name of the pdf fields to populate and the second field are the values

## Upgrading your pdf populator
When an update is available, go the specified url and download the source.zip file.
Once the download is complete, unzip the file and copy the `pdf populator.exe` file and replace your current `pdf populator.exe` file

## Version History
| Version | Changes                                                   |
|---------|-----------------------------------------------------------|
| 1.0     | initial version                                           |
| 1.1     | Fixed bug where numbers weren't populated in pdf properly |
| 1.2     | Added a version manager                                   |
| 1.3     | Added an executable to run the program                    |
| 1.4     | Program now runs on a loop until exit is selected         |

## Dev note
Making a new build, run the following command in the root of the directory
`python -m PyInstaller -F main.py -n 'pdf populator'`
