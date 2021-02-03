# Web-Scraping
Script to download images given a keyword from Chrome.

## Execution
1. Clone the git repository using 
`git clone https://github.com/archisha-chandel/Web-Scraping.git`
2. Open command prompt/ VS Code. Make changes in `main.py`
```
# Download the Chrome Driver as per the Chrome version you are using.
# Put the path for your Chrome Driver here.
# I have added the path for version-88.

DRIVER_PATH = os.path.join('./Web-Scraping/Driver','chromedriver.exe')
wd = webdriver.Chrome(executable_path= DRIVER_PATH)


from search_and_download import search_and_download

# search_term is the keyword for the images you are looking for
search_term = "flower"
search_and_download(
    search_term = search_term,
    driver_path = DRIVER_PATH,
    target_path = os.path.join('./Web-Scraping','images'), # folder to store images
    number_images = 10 # number of images you want to download
)
```
After making these changes, run `python main.py`
3. All the images will be downloaded in `images` folder under the folder name
same as the `search_term`.

## Contributions
Any contribution or issue related to this repository is welcome. 