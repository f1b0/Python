import re
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class WebFetcher(object):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('-headless')
        self.driver = Firefox(executable_path='geckodriver', firefox_options=self.options)

    def quit_browser(self):
        self.driver.quit()

    def get_page(self, site):
        self.driver.get(site)
        return self.driver.page_source

    @staticmethod
    def get_links(page_source):

        def clean_link_list(dirty_list_input):
            clean_list = []
            for x in range(0, len(dirty_list_input)):
                quoted = re.compile('"[^"]*"')
                for value in quoted.findall(dirty_list_input[x]):
                    startIndex = value.find('\"')
                    if startIndex != -1:  # i.e. if the first quote was found
                        endIndex = value.find('\"', startIndex + 1)
                        if startIndex != -1 and endIndex != -1:  # i.e. both quotes were found
                            if 'http' not in value[startIndex + 1:endIndex]:
                                pass
                            else:
                                clean_list.append(value[startIndex + 1:endIndex])
            return clean_list

        def check_dupplicates(incomming):
            clean_list = []
            for x in incomming:
                if x not in clean_list:
                    clean_list.append(x)
                else:
                    pass
            return clean_list

        code_lines = str(page_source).strip().splitlines()
        link_list = []
        for x in range(0, len(code_lines)):
            if 'http' in code_lines[x]:
                link_list.append(code_lines[x].lstrip())
        not_quotes = clean_link_list(link_list)
        check = check_dupplicates(not_quotes)
        return check


if __name__ == "__main__":
    site = 'WEB_PAGE'
    b = WebFetcher()
    page_source = b.get_page(site)
    link_list = b.get_links(page_source)

    for link in link_list:
        print(link)

    b.quit_browser()
