import pandas as pd
import re

def produce_high():
    #Python3 tools/synth_image.py --style_image examples/style_images/1_10_22_download.jpg --text_corpus HumanInsulin/SolubleInsulin
    myFile = open("tools/sample.txt", mode="r+")
    df = pd.read_csv('flipkart_images/catalog_dump_09nov22.csv') 
    i = 0
    for name in df['SaltName'].unique():
        i += 1
        name = re.sub(r'\W+', '', name)
        #synth_image_head('examples/style_images/1_10_22_download.jpg', 'HumanInsulin/SolubleInsulin', 'test')
        if i != 1936:
            print('Python3 tools/synth_image.py' + ' --style_image ' + 'examples/style_images/1_10_22_download'+str(i)+'.jpg' + ' --text_corpus ' + name, file=myFile)
        else:
            break
produce_high()
