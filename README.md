# HTMLtoCSV

This simple application uses BeautifulSoup and tkinter to convert QGIS HTML reports to CSV files.

The following is an example of a report generated by QGIS: 
```
Analyzed file: exported.tif (band 1)

Minimum value: 3298

Maximum value: 3901

Range: 603

Sum: 324123

Mean value: 3523.076086956522

Standard deviation: 138.2584165667783

Sum of the squares: 1739500.467391304

```

The output will look like:


|Label             |Value                                                                                                                                                                |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Analyzed file     |file.tif (band 1)|
|Minimum value     |3298                                                                                                                                                                 |
|Maximum value     |3901                                                                                                                                                                 |
|Range             |603                                                                                                                                                                  |
|Sum               |324123                                                                                                                                                               |
|Mean value        |3523.076086956522                                                                                                                                                    |
|Standard deviation|138.2584165667783                                                                                                                                                    |
|Sum of the squares|1739500.467391304                                                                                                                                                    |

# How to run
1. If you do not have Python installed, download it from [here](https://www.python.org/downloads/).
2. Run the command `pip install beautifulsoup4` to install the required packages.
3. Run the command `python app.py` to run the application.
4. Select the HTML file you want to convert.

# License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

