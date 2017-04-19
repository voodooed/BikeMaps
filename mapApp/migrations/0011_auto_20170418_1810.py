# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapApp', '0010_incident_impact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('districtName', models.CharField(max_length=250, verbose_name=b'District Name')),
            ],
        ),
        migrations.AddField(
            model_name='incident',
            name='bicycle_type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='What type of bicycle were you riding?', choices=[(b'Personal', "Personal (my own bicycle or a friend's)"), (b'Bike share', 'Bike share'), (b'Bike rental', 'Bike rental')]),
        ),
        migrations.AddField(
            model_name='incident',
            name='ebike',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Did the incident involve a pedal-assist electric bike (eBike)?', choices=[(b'Yes', 'Yes'), (b'No', 'No'), (b"I don't know", "I don't know")]),
        ),
        migrations.AddField(
            model_name='incident',
            name='personal_involvement',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Were you directly involved in the incident?', choices=[(b'Yes', 'Yes, this happened to me'), (b'No', 'No, I witnessed this happen to someone else')]),
        ),
        migrations.AddField(
            model_name='point',
            name='source',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Where did you first find out about BikeMaps.org?', choices=[(b'BikeMaps team', 'Directly from the BikeMaps.org team'), (b'BikeMaps swag', 'BikeMaps.org swag (e.g., seat cover, water bottle, etc.) without meeting the team'), (b'Traditional media', 'Traditional media (newspaper, TV, radio)'), (b'Another website', 'Link from another website'), (b'Word of mouth', 'Word of mouth'), (b'Social media', 'Social media (e.g., Twitter, Instagram, Facebook)'), (b'Other', 'Other'), (b"Don't remember", "I don't remember")]),
        ),
        migrations.AlterField(
            model_name='hazard',
            name='i_type',
            field=models.CharField(max_length=150, verbose_name='What type of hazard was it?', choices=[('Infrastructure', ((b'Curb', 'Curb'), (b'Island', 'Island'), (b'Train track', 'Train track'), (b'Pothole', 'Pothole'), (b'Road surface', 'Road surface'), (b'Poor signage', 'Poor signage'), (b'Speed limits', 'Speed limits'), (b'Blind corner', 'Blind corner or turn'), (b'Bike lane disappears', 'Bike lane disappears'), (b'Vehicles enter exit', 'Vehicles entering/exiting roadway'), (b'Dooring risk', 'Dooring risk zone'), (b'Vehicle in bike lane', 'Vehicle use of bike lane'), (b'Dangerous intersection', 'Dangerous intersection'), (b'Dangerous vehicle left turn', 'Dangerous vehicle left turn'), (b'Dangerous vehicle right turn', 'Dangerous vehicle right turn'), (b'Sensor does not detect bikes', 'Sensor does not pick up bikes'), (b'Steep hill', 'Steep hill - bike speed affected'), (b'Narrow road', 'Narrow road'), (b'Pedestrian conflict zone', 'Pedestrian conflict zone'), (b'Other infrastructure', 'Other (Please describe)'))), ('Environmental', ((b'Icy/Snowy', 'Icy/Snowy'), (b'Poor visibility', 'Poor visibility (fog, snow, smoke etc.)'), (b'Broken glass', 'Broken glass on road'), (b'Wet leaves', 'Wet leaves on road'), (b'Gravel rocks or debris', 'Gravel, rocks or debris on road/path'), (b'Construction', 'Construction'), (b'Other', 'Other (Please describe)'))), ('Human Behaviour', ((b'Poor visibility', 'Poor visibility'), (b'Parked car', 'Parked car'), (b'Traffic flow', 'Traffic flow'), (b'Driver behaviour', 'Driver behaviour'), (b'Cyclist behaviour', 'Cyclist behaviour'), (b'Pedestrian behaviour', 'Pedestrian behaviour'), (b'Congestion', 'Congestion'), (b'Other', 'Other (Please describe)')))]),
        ),
        migrations.AlterField(
            model_name='incident',
            name='riding_on',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Where were you riding your bike?', choices=[('Busy street', ((b'Busy street cycle track', 'On a cycle track (separated bike lane)'), (b'Busy street bike lane', 'On a painted bike lane'), (b'Busy street, no bike facilities', 'On a street with no bicycle facility'))), ('Quiet street', ((b'Quiet street bike lane', 'On a local street bikeway (bike route)'), (b'Quiet street, no bike facilities', 'On a street with no bicycle facility'))), ('Off-Street', ((b'Cycle track', 'On a physically separated bike lane (cycle track)'), (b'Mixed use trail', 'On a multi-use path'), (b'Sidewalk', 'On a sidewalk'))), (b"Don't remember", "I don't remember")]),
        ),
        migrations.AlterField(
            model_name='point',
            name='age',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='What is your birth year?', choices=[(b'2004', b'2004'), (b'2003', b'2003'), (b'2002', b'2002'), (b'2001', b'2001'), (b'2000', b'2000'), (b'1999', b'1999'), (b'1998', b'1998'), (b'1997', b'1997'), (b'1996', b'1996'), (b'1995', b'1995'), (b'1994', b'1994'), (b'1993', b'1993'), (b'1992', b'1992'), (b'1991', b'1991'), (b'1990', b'1990'), (b'1989', b'1989'), (b'1988', b'1988'), (b'1987', b'1987'), (b'1986', b'1986'), (b'1985', b'1985'), (b'1984', b'1984'), (b'1983', b'1983'), (b'1982', b'1982'), (b'1981', b'1981'), (b'1980', b'1980'), (b'1979', b'1979'), (b'1978', b'1978'), (b'1977', b'1977'), (b'1976', b'1976'), (b'1975', b'1975'), (b'1974', b'1974'), (b'1973', b'1973'), (b'1972', b'1972'), (b'1971', b'1971'), (b'1970', b'1970'), (b'1969', b'1969'), (b'1968', b'1968'), (b'1967', b'1967'), (b'1966', b'1966'), (b'1965', b'1965'), (b'1964', b'1964'), (b'1963', b'1963'), (b'1962', b'1962'), (b'1961', b'1961'), (b'1960', b'1960'), (b'1959', b'1959'), (b'1958', b'1958'), (b'1957', b'1957'), (b'1956', b'1956'), (b'1955', b'1955'), (b'1954', b'1954'), (b'1953', b'1953'), (b'1952', b'1952'), (b'1951', b'1951'), (b'1950', b'1950'), (b'1949', b'1949'), (b'1948', b'1948'), (b'1947', b'1947'), (b'1946', b'1946'), (b'1945', b'1945'), (b'1944', b'1944'), (b'1943', b'1943'), (b'1942', b'1942'), (b'1941', b'1941'), (b'1940', b'1940'), (b'1939', b'1939'), (b'1938', b'1938'), (b'1937', b'1937'), (b'1936', b'1936'), (b'1935', b'1935'), (b'1934', b'1934'), (b'1933', b'1933'), (b'1932', b'1932'), (b'1931', b'1931'), (b'1930', b'1930'), (b'1929', b'1929'), (b'1928', b'1928'), (b'1927', b'1927'), (b'1926', b'1926'), (b'1925', b'1925'), (b'1924', b'1924'), (b'1923', b'1923'), (b'1922', b'1922'), (b'1921', b'1921'), (b'1920', b'1920'), (b'1919', b'1919'), (b'1918', b'1918'), (b'1917', b'1917'), (b'1916', b'1916'), (b'1915', b'1915'), (b'1914', b'1914'), (b'1913', b'1913'), (b'1912', b'1912'), (b'1911', b'1911'), (b'1910', b'1910'), (b'1909', b'1909'), (b'1908', b'1908'), (b'1907', b'1907'), (b'1906', b'1906'), (b'1905', b'1905')]),
        ),
    ]
