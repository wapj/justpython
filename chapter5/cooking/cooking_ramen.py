from package import RamenBag
from soup import PowderSoup, VegetableSoup
from noodles import Noodle

noodle = Noodle("보통면")
powder_soup = PowderSoup("분말 스프")
vegetable_soup = VegetableSoup("야채 스프")
ramen_pack = RamenBag("심라면", noodle, [powder_soup, vegetable_soup])


def open_package(pack):
    noodle, soups = pack.open()
    print(noodle)
    print(soups[0])
    print(soups[1])


open_package(ramen_pack)
