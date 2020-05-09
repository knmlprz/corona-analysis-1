import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os
from time import sleep


def scrape_page_data(npages, delay=0.01):
    """
    Scrapes dataset from http://policja.pl/pol/form/1,Informacja-dzienna.html

    :param npages Number of pages to scrape
    :param delay Seconds of delay between requests

    """
    # Container for data
    data = []

    url_template = r"http://policja.pl/pol/form/1,Informacja-dzienna.html?page={}"

    for i in range(0, npages):
        # Try again max 100 times
        for attempt in range(0, 100):
            try:
                # Load webpage
                web = urllib.request.urlopen(url_template.format(i))
                soup = BeautifulSoup(web.read(), "lxml")

                # Find table with data
                table = soup.find(
                    "table", {"class": "table-listing margin_b20"}
                ).find_all("tr")

                # Parse tr tags
                for ntr in range(1, len(table)):
                    tds = table[ntr].find_all("td")
                    row = {}

                    # Parse td tags (rows)
                    for ntd in range(0, len(tds)):
                        row[tds[ntd]["data-label"]] = tds[ntd].string

                    print("\033[92mRow found: {:.80} \033[0m".format(str(row)))
                    data.append(row)
                break
            except urllib.error.HTTPError:
                print("\033[93mHttp error. Trying again... \033[0m")
                sleep(delay)

    df = pd.DataFrame(data)
    print(df)

    # Dump df to csv
    outdir = "./Data"
    outname = "policjapl" + ".csv"
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    df.to_csv(os.path.join(outdir, outname), sep="\t")


if __name__ == "__main__":
    scrape_page_data(10, 0.05)
