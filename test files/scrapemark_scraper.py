__author__ = 'ilu'
from scrapemark import scrape

print scrape(
    """
    <h2>::{{}}</h2>
    """
    , url='https://projecteuler.net/problem=1.html'
)
