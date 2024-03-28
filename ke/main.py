from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# execute(['scrapy', 'crawl', 'ke_new'])
# execute(['scrapy', 'crawl', 'ke_rent'])
execute(['scrapy', 'crawl', 'ke_sec'])
