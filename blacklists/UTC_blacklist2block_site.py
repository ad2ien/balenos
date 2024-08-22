# parse files from UTC university, check urls and add them to json file
import json
import concurrent.futures
import time
import ping3

block_list_template_file = "./block_site_template.json"

folders = [
  # "ads -> publicite",
  ##   "adult",
  # "aggressive -> agressif",
  "agressif",
  "arjel",
  "associations_religieuses",
  "astrology",
  # "audio-video",
  # "bank",
  "bitcoin",
  # "blog",
  # "celebrity",
  # "chat",
  "child",
  "cleaning",
  "cooking",
  ##   "cryptojacking",
  "dangerous_material",
  "dating",
  "ddos",
  "dialer",
  "doh",
  # "download",
  "drogue",
  # "drugs -> drogue",
  # "educational_games",
  "examen_pix",
  # "exceptions_liste_bu",
  "fakenews",
  # "filehosting",
  # "financial",
  # "forums",
  "gambling",
  "games",
  "hacking",
  # "jobsearch",
  "lingerie",
  # "liste_blanche",
  # "liste_bu",
  # "mail -> forums",
  "malware",
  # "manga",
  "marketingware",
  "mixed_adult",
  # "mobile-phone",
  "phishing",
  # "porn -> adult",
  # "press",
  # "proxy -> redirector",
  "publicite",
  # "radio",
  "reaffected",
  "redirector",
  "remote-control",
  "residential-proxies",
  "sect",
  "sexual_education",
  # "shopping",
  # "shortener",
  # "social_networks",
  # "special",
  # "sports",
  "stalkerware",
  # "strict_redirector",
  # "strong_redirector",
  # "translation",
  "tricheur",
  "tricheur_pix",
  # "update",
  # "violence -> agressif",
  # "vpn",
  "warez",
  # "webmail",
]

def ping(url):
  try:
    response = ping3.ping(url, unit='ms')
  except:
    print(f"!!! Error : {url}")
    return

  if response:
    # print(url + " is up!")
    return url
  else:
    return None


def main():

  # TODO download and unzip
  ## write temporary result in a file to be  to be able to do in several times

  urls_to_test = []
  url_to_block = set()

  for folder in folders:
    # read domain file
    with open(f"blacklists/{folder}/domains", "r") as f:
      lines = f.readlines()

      for line in lines:
        url=f"https://{line.strip()}"
        urls_to_test.append(url)

    print(f"Testing {len(urls_to_test)} urls from {folder}...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
      future_to_url = {executor.submit(ping, url, 5): url for url in urls_to_test}
      time1 = time.time()
      for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            continue
        if data != None:
            url_to_block.add(data)
            print(".", end='')

      # dump results in a temp file
      time2 = time.time()
      print(f'Took {time2-time1:.2f} s')
  
  print("url test finished, build da json")

  with open(block_list_template_file) as json_file:
    block_list_config = json.load(json_file)
    block_list_config["blocked"] = list(url_to_block)
    with open("block_list_config.json", 'w') as outfile:
      outfile.write(json.dumps(block_list_config, indent=2))
        
  print("End of building the file for block list")

if __name__ == "__main__":
    main()