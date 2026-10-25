import optparse as opt
import webbrowser as web
import requests
from urllib.parse import quote

def main():
    url = "https://blog-cyberworm.com/search/"
    userAgent = {
        'user-agent': '[***] You have to enter your user-agent info. [***]'
    }

    parser = opt.OptionParser(
        """
        USAGE: python remoteSearch.py -e <A word about the blog post you are looking for in the site.>
        USAGE: python remoteSearch.py --extension <A word about the blog post you are looking for in the site.>
        """
    )
    parser.add_option("-e", "--extension", dest="extension", help="What do you lookin' for in the site?")
    (options, args) = parser.parse_args()
    extension = options.extension

    if not extension:
        parser.error('A search term is required (-e / --extension).')
    target_url = url + quote(extension, safe='')
    try:
        getStatus = requests.get(target_url, headers=userAgent, timeout=15)
    except requests.RequestException as exc:
        print(f'[ERROR] Search request failed: {exc}')
        return 1

    if options.extension == None:
        print(f"[!] Missing argument. Please, follow the usage.\n\n{parser.usage}")
    else:
        if getStatus.ok:
            sourceCode = getStatus.text
            if "0 Sonuç Bulundu." in sourceCode or "0 Results Found" in sourceCode:
                print(f"Not found a blog about '{extension}'.")
            else:
                web.open(target_url)
        else:
            print(f"Something went wrong. Status Code: '{getStatus.status_code}'")


if __name__ == "__main__":
    raise SystemExit(main())

