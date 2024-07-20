# Exelerator
A Python program for populating a pdf from an Excel spreadsheet


## Running the Excelerator
- next to `Exelerator.exe` have a `templates` and `data` folder. These should be automatically generated the 
first time you run `Exelerator.exe`
    - Inside the templates folder place your template pdfs with the name structure "FileName - Template"
        - Where the FileName is the name of the template, and "- Template" is to indicate that it is a template file
        - Template will be replaced by the `clientname1_field` outlined in the data sheet
    - Inside the data folder have your Excel spreadsheet that you would like to pull the data from.
        - This Excel file needs to have a sheet called `Python Data` or whatever is configured under `data_sheet_name` 
            in your `config.cfg` file (See [Config Explanation](#default-config-explanation) for more details)
            - Inside this sheet, the first column will contain the name of the pdf fields to populate and the 
                second field are the values
            - The first row will not be read. This should simply be your headers.


## Example Datasheet Format
| Field Name                    | Field Value   |
|:------------------------------|---------------|
| `clientname1_field`           | Jon Doe       |
| `clientname2_field`           | Jane Doe      |
| `fundcoderedemption1_field`   | AAA 111       |
| `fundnameredemption1_field`   | Fund Series A |
| `fundamountredemption1_field` | 100           |


## Upgrading your Exelerator
When an update is available, go the specified url and download the source.zip file.
Once the download is complete, unzip the file and copy the `Exelerator.exe` file and replace 
your current `Exelerator.exe` file


## Default Config Explanation
- `data_sheet_name`: The name of the sheet in your excel file that has the values for the program to look up and use 
when populating a PDF
- `client_field_name`: The name of the key inside of your data sheet that has the clients name. This is used when 
generating the PDF file name
- `font_size`: The size of the font for the annotations when generating a new PDF


## Version History
| Version | Changes                                                                                                                                           |
|:-------:|---------------------------------------------------------------------------------------------------------------------------------------------------|
|   1.0   | initial version                                                                                                                                   |
|   1.1   | Fixed bug where numbers weren't populated in pdf properly                                                                                         |
|   1.2   | Added a version manager                                                                                                                           |
|   1.3   | Added an executable to run the program                                                                                                            |
|   1.4   | Program now runs on a loop until exit is selected                                                                                                 |
|   1.5   | Added logging and auto generate folders on first run                                                                                              |
|   1.6   | Added a config file to be generated and verified on launch                                                                                        |
|   1.7   | Fixed an issues with child and parent annotations                                                                                                 |
|   1.8   | - Improved console experience<br/>- Automatically selects excel file if only one is available<br/>- Folder `generated` created for populated PDFs |


## Dev note
Making a new build, run the following command in the root of the directory
`python -m PyInstaller -F main.py -n 'Exelerator'` or by running `build_new_release.sh`
