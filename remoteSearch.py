import optparse as opt
import webbrowser as web
import requests

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

    getStatus = requests.get(f"{url}{extension}", headers=userAgent)

    if options.extension == None:
        print(f"[!] Missing argument. Please, follow the usage.\n\n{parser.usage}")
    else:
        if getStatus.ok:
            sourceCode = getStatus.text
            if "0 Sonuç Bulundu." in sourceCode or "0 Results Found" in sourceCode:
                print(f"Not found a blog about '{extension}'.")
            else:
                web.open(f"{url}{extension}")
        else:
            print(f"Something went wrong. Status Code: '{getStatus.status_code}'")


if __name__ == "__main__":
    main()

