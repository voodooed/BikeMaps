# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2020-04-22 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapApp', '0013_auto_20190423_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='age',
            field=models.CharField(blank=True, choices=[(b'2007', b'2007'), (b'2006', b'2006'), (b'2005', b'2005'), (b'2004', b'2004'), (b'2003', b'2003'), (b'2002', b'2002'), (b'2001', b'2001'), (b'2000', b'2000'), (b'1999', b'1999'), (b'1998', b'1998'), (b'1997', b'1997'), (b'1996', b'1996'), (b'1995', b'1995'), (b'1994', b'1994'), (b'1993', b'1993'), (b'1992', b'1992'), (b'1991', b'1991'), (b'1990', b'1990'), (b'1989', b'1989'), (b'1988', b'1988'), (b'1987', b'1987'), (b'1986', b'1986'), (b'1985', b'1985'), (b'1984', b'1984'), (b'1983', b'1983'), (b'1982', b'1982'), (b'1981', b'1981'), (b'1980', b'1980'), (b'1979', b'1979'), (b'1978', b'1978'), (b'1977', b'1977'), (b'1976', b'1976'), (b'1975', b'1975'), (b'1974', b'1974'), (b'1973', b'1973'), (b'1972', b'1972'), (b'1971', b'1971'), (b'1970', b'1970'), (b'1969', b'1969'), (b'1968', b'1968'), (b'1967', b'1967'), (b'1966', b'1966'), (b'1965', b'1965'), (b'1964', b'1964'), (b'1963', b'1963'), (b'1962', b'1962'), (b'1961', b'1961'), (b'1960', b'1960'), (b'1959', b'1959'), (b'1958', b'1958'), (b'1957', b'1957'), (b'1956', b'1956'), (b'1955', b'1955'), (b'1954', b'1954'), (b'1953', b'1953'), (b'1952', b'1952'), (b'1951', b'1951'), (b'1950', b'1950'), (b'1949', b'1949'), (b'1948', b'1948'), (b'1947', b'1947'), (b'1946', b'1946'), (b'1945', b'1945'), (b'1944', b'1944'), (b'1943', b'1943'), (b'1942', b'1942'), (b'1941', b'1941'), (b'1940', b'1940'), (b'1939', b'1939'), (b'1938', b'1938'), (b'1937', b'1937'), (b'1936', b'1936'), (b'1935', b'1935'), (b'1934', b'1934'), (b'1933', b'1933'), (b'1932', b'1932'), (b'1931', b'1931'), (b'1930', b'1930'), (b'1929', b'1929'), (b'1928', b'1928'), (b'1927', b'1927'), (b'1926', b'1926'), (b'1925', b'1925'), (b'1924', b'1924'), (b'1923', b'1923'), (b'1922', b'1922'), (b'1921', b'1921'), (b'1920', b'1920'), (b'1919', b'1919'), (b'1918', b'1918'), (b'1917', b'1917'), (b'1916', b'1916'), (b'1915', b'1915'), (b'1914', b'1914'), (b'1913', b'1913'), (b'1912', b'1912'), (b'1911', b'1911'), (b'1910', b'1910'), (b'1909', b'1909'), (b'1908', b'1908')], max_length=15, null=True, verbose_name='What is your birth year?'),
        ),
    ]
