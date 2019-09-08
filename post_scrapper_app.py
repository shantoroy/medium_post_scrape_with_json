import json
from medium_post_scrapper import MediumScrapper
try:
    from local_settings import *
except FileNotFoundError as fx:
    print(str(fx))


if __name__ == '__main__':
    file_name_list = ["ethereum.json", "blockchain.json", "smart-contract.json",
                      "solidity.json", "vyper.json", "ripple.json",
                      "remix.json", "metamask.json", "bitcoin.json"]
    tag_list = ["ethereum", "blockchain", "smart contract", "solidity", "vyper", "ripple",
                "remix", "metamask", "bitcoin"]

    for file_name, tag in zip(file_name_list, tag_list):
        scrapper = MediumScrapper(tag, CHROME_DRIVER_PATH=CHROME_DRIVER_PATH)
        output_filename = file_name
        data = scrapper.get_post_contents()
        with open(output_filename, 'w') as fp:
            json.dump(data, fp)
        print("Check JSON file: {}".format(output_filename))
        print("Total posts: {}".format(len(data)))
