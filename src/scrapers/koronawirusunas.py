import json
import re
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os
from sys import stderr

URL = "https://www.koronawirusunas.pl"
PATTERN = re.compile("var\sdataSource_mobilnosc")

def scrape_page_data():
    """
    Scrapes dataset from koronawirus.pl

    """
    # Load webpage
    web = urllib.request.urlopen(URL)
    soup = BeautifulSoup(web.read(), "lxml")

    # Get first scrpit tag that contains PATTERN
    script = soup.find('script', text=PATTERN)
    # Get all strings like 'var * = *;'
    js_vars_data = re.findall(
        r'var.*?=\s*(.*?);', script.string, re.DOTALL | re.MULTILINE)

    js_vars_names = re.findall(r"var\s*(\S*)", script.string)
    print(js_vars_names)

    print(script)
    # Parse each var to json array
    for i in range(0, len(js_vars_data)):
        # Substitute key: val to "key" val
        r = re.sub(r'([{\s,])(\w+)(:)', r'\1"\2"\3', js_vars_data[i])

        # Fix ',' before } ]
        r = re.sub(r",[ \t\r\n]*}", "}", r)
        r = re.sub(r",[ \t\r\n]*\]", "]", r)

        try:
            o = json.loads(r)
            # Each array looks like [{"key": val, ...}, {"key: val}...]
            # Load it directly to dataframe
            df = pd.DataFrame(o)

            # Export df to "./Data/koronawirusunas/file_name.csv"
            # Create directory if not exists
            outdir = "./data/koronawirusunas"
            outname = js_vars_names[i] + ".csv"
            if not os.path.exists(outdir):
                os.makedirs(outdir)

            df.to_csv(os.path.join(outdir, outname), sep="\t")

            print("\033[92mFrame found: {:.20} \033[0m".format(
                js_vars_names[i]))
            print(df)

        except json.decoder.JSONDecodeError:
            # Decoder Exception.
            print("Data skipped: {:.20}".format(r), file=stderr)


if __name__ == '__main__':
    scrape_page_data()
