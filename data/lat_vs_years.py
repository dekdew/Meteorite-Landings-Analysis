import pandas as pd
import matplotlib.pyplot as plt
import pygal
from pygal.style import RedBlueStyle

data = pd.read_csv('data.csv')
data = data[(data.reclat != 0) & (data.reclong != 0)]
data.info()

valt = data.groupby('nametype').get_group('Valid').copy()
valt.dropna(inplace=True)
valt.info()

plt.scatter(valt.year,valt.reclat,color='g',alpha=0.4)
plt.xlim(1900,2013)
plt.ylim(-90,90)
plt.ylabel('Latitude')
plt.xlabel('Year')
plt.title('Meteorite recorded latitude vs year')
plt.show()

v_class = valt['recclass'].value_counts()

v_class_2 = valt.copy()

v_class_2.recclass.replace(to_replace=['Acapulcoite', 'Acapulcoite/Lodranite', 'Acapulcoite/lodranite',
'Lodranite', 'Lodranite-an', 'Winonaite', 'Achondrite-prim', 'Angrite', 'Aubrite', 'Aubrite-an', 'Ureilite', 'Ureilite-an', 'Ureilite-pmict',
'Brachinite', 'Diogenite', 'Diogenite-an', 'Diogenite-olivine', 'Diogenite-pm', 'Eucrite', 'Eucrite-Mg rich', 'Eucrite-an', 'Eucrite-br',
'Eucrite-cm', 'Eucrite-mmict', 'Eucrite-pmict', 'Eucrite-unbr', 'Howardite', 'Lunar', 'Lunar (anorth)', 'Lunar (bas. breccia)',
'Lunar (bas/anor)', 'Lunar (bas/gab brec)', 'Lunar (basalt)', 'Lunar (feldsp. breccia)', 'Lunar (gabbro)', 'Lunar (norite)',
'Martian', 'Martian (OPX)', 'Martian (chassignite)', 'Martian (nakhlite)', 'Martian (shergottite)', 'C','C2','C4','C4/5',
'C6','C1-ung', 'C1/2-ung','C2-ung','C3-ung', 'C3/4-ung','C4-ung','C5/6-ung','CB', 'CBa', 'CBb', 'CH/CBb', 'CH3', 'CH3 ', 'CI1', 'CK', 'CK3',
'CK3-an', 'CK3.8', 'CK3/4', 'CK4', 'CK4-an', 'CK4/5', 'CK5', 'CK5/6', 'CK6', 'CM', 'CM-an', 'CM1', 'CM1/2', 'CM2', 'CM2-an',
'CO3', 'CO3 ', 'CO3.0', 'CO3.1', 'CO3.2', 'CO3.3', 'CO3.4', 'CO3.5', 'CO3.6', 'CO3.7', 'CO3.8', 'CR', 'CR-an', 'CR1', 'CR2', 'CR2-an',
'CV2', 'CV3', 'CV3-an', 'OC', 'OC3','H', 'H(5?)', 'H(?)4', 'H(L)3', 'H(L)3-an', 'H-an','H-imp melt', 'H-melt rock', 'H-metal', 'H/L3', 'H/L3-4', 'H/L3.5',
'H/L3.6', 'H/L3.7', 'H/L3.9', 'H/L4', 'H/L4-5', 'H/L4/5', 'H/L5', 'H/L6', 'H/L6-melt rock', 'H/L~4', 'H3', 'H3 ', 'H3-4', 'H3-5',
'H3-6', 'H3-an', 'H3.0', 'H3.0-3.4', 'H3.1', 'H3.10', 'H3.2', 'H3.2-3.7', 'H3.2-6', 'H3.2-an', 'H3.3', 'H3.4', 'H3.4-5',
'H3.4/3.5', 'H3.5', 'H3.5-4', 'H3.6', 'H3.6-6', 'H3.7', 'H3.7-5', 'H3.7-6', 'H3.7/3.8', 'H3.8', 'H3.8-4', 'H3.8-5', 'H3.8-6',
'H3.8-an', 'H3.8/3.9', 'H3.8/4', 'H3.9', 'H3.9-5', 'H3.9-6', 'H3.9/4', 'H3/4', 'H4', 'H4 ', 'H4(?)', 'H4-5', 'H4-6', 'H4-an',
'H4/5', 'H4/6', 'H5', 'H5 ', 'H5-6', 'H5-7', 'H5-an', 'H5-melt breccia', 'H5/6', 'H6', 'H6 ', 'H6-melt breccia', 'H6/7',
'H7', 'H?','H~4', 'H~4/5', 'H~5', 'H~6','L', 'L(?)3', 'L(H)3', 'L(LL)3', 'L(LL)3.05', 'L(LL)3.5-3.7', 'L(LL)5', 'L(LL)6',
'L(LL)~4', 'L-imp melt', 'L-melt breccia', 'L-melt rock', 'L-metal', 'L/LL', 'L/LL(?)3', 'L/LL-melt rock', 'L/LL3', 'L/LL3-5', 'L/LL3-6',
'L/LL3.10', 'L/LL3.2', 'L/LL3.4', 'L/LL3.5', 'L/LL3.6/3.7', 'L/LL4', 'L/LL4-6', 'L/LL4/5', 'L/LL5', 'L/LL5-6', 'L/LL5/6', 'L/LL6',
'L/LL6-an', 'L/LL~4', 'L/LL~5', 'L/LL~6', 'L3', 'L3-4', 'L3-5', 'L3-6', 'L3-7', 'L3.0', 'L3.0-3.7', 'L3.0-3.9', 'L3.05', 'L3.1',
'L3.10', 'L3.2', 'L3.2-3.5', 'L3.2-3.6', 'L3.3', 'L3.3-3.5', 'L3.3-3.6', 'L3.3-3.7', 'L3.4', 'L3.4-3.7', 'L3.5', 'L3.5-3.7',
'L3.5-3.8', 'L3.5-3.9', 'L3.5-5', 'L3.6', 'L3.6-4', 'L3.7', 'L3.7-3.9', 'L3.7-4', 'L3.7-6', 'L3.7/3.8', 'L3.8', 'L3.8-5',
'L3.8-6', 'L3.8-an', 'L3.9', 'L3.9-5', 'L3.9-6', 'L3.9/4', 'L3/4', 'L4', 'L4 ', 'L4-5', 'L4-6', 'L4-an', 'L4-melt rock', 'L4/5', 'L5',
'L5 ', 'L5-6', 'L5-7', 'L5/6', 'L6', 'L6 ', 'L6-melt breccia', 'L6-melt rock', 'L6/7', 'L7', 'LL', 'LL(L)3', 'LL-melt rock', 'LL3',
'LL3-4', 'LL3-5', 'LL3-6', 'LL3.0', 'LL3.00', 'LL3.1', 'LL3.1-3.5', 'LL3.10', 'LL3.15', 'LL3.2', 'LL3.3', 'LL3.4', 'LL3.5', 'LL3.6',
'LL3.7', 'LL3.7-6', 'LL3.8', 'LL3.8-6', 'LL3.9', 'LL3.9/4', 'LL3/4', 'LL4', 'LL4-5', 'LL4-6', 'LL4/5', 'LL4/6', 'LL5', 'LL5-6', 'LL5-7',
'LL5/6', 'LL6', 'LL6 ', 'LL6(?)', 'LL6/7', 'LL7', 'LL7(?)', 'LL<3.5', 'LL~3', 'LL~4', 'LL~4/5', 'LL~5', 'LL~6',
'L~3', 'L~4', 'L~5', 'L~6','Relict H','Relict OC', 'EH','EH-imp melt', 'EH3', 'EH3/4-an', 'EH4', 'EH4/5', 'EH5', 'EH6',
'EH6-an', 'EH7', 'EH7-an', 'EL3', 'EL3/4', 'EL4', 'EL4/5', 'EL5', 'EL6', 'EL6 ', 'EL6/7', 'EL7','E','E3','E4',
'E5','E6', 'K', 'K3','R', 'R3', 'R3-4', 'R3-5', 'R3-6', 'R3.4', 'R3.5-6', 'R3.6', 'R3.7', 'R3.8', 'R3.8-5', 'R3.8-6', 'R3.9', 'R3/4', 'R4',
'R4/5', 'R5', 'R6'],value='Stony meteorites',inplace=True)

v_class_2.recclass.replace(to_replace=['Pallasite', 'Pallasite, PES','Pallasite, PMG',
'Pallasite, PMG-an', 'Pallasite, ungrouped', 'Pallasite?', 'Mesosiderite', 'Mesosiderite-A','Mesosiderite-A1',
'Mesosiderite-A2', 'Mesosiderite-A3','Mesosiderite-A3/4', 'Mesosiderite-A4', 'Mesosiderite-B','Mesosiderite-B1',
'Mesosiderite-B2', 'Mesosiderite-B4','Mesosiderite-C', 'Mesosiderite-C2', 'Mesosiderite-an','Mesosiderite?'],value='Stony–iron meteorites',inplace=True)

v_class_2.recclass.replace(to_replace=['Iron, IC', 'Iron, IC-an', 'Iron, IIAB', 'Iron, IIAB-an',
'Iron, IIC', 'Iron, IID', 'Iron, IID-an','Iron, IIF', 'Iron, IIG', 'Iron, IIIAB', 'Iron, IIIAB-an', 'Iron, IIIAB?', 'Iron, IIIE',
'Iron, IIIE-an', 'Iron, IIIF', 'Iron, IVA', 'Iron, IVA-an', 'Iron, IVB', 'Iron, IAB complex', 'Iron, IAB-MG','Iron, IAB-an', 'Iron, IAB-sHH',
'Iron, IAB-sHL', 'Iron, IAB-sLH','Iron, IAB-sLL', 'Iron, IAB-sLM', 'Iron, IAB-ung', 'Iron, IAB?','Iron, IIE', 'Iron, IIE-an', 'Iron, IIE?', 'Iron','Iron?','Relict iron', 'Iron, ungrouped'],value='Iron meteorites',inplace=True)

v_class_2.recclass.replace(to_replace=['Chondrite-fusion crust', 'Fusion crust','Impact melt breccia', 'Enst achon-ung','Stone-uncl', 'Stone-ung',
'Unknown', 'Achondrite-ung', 'Chondrite-ung', 'Enst achon', 'E-an', 'E3-an', 'E5-an'],value='Unknown-Ungrouped',inplace=True)

stony = len(v_class_2[v_class_2.recclass == 'Stony meteorites'])
istony = len(v_class_2[v_class_2.recclass == 'Stony–iron meteorites'])
iron = len(v_class_2[v_class_2.recclass == 'Iron meteorites'])
unknown = len(v_class_2[v_class_2.recclass == 'Unknown-Ungrouped'])


class_chart = pygal.Pie(half_pie=True, style=RedBlueStyle)
class_chart.title = 'Meteorites classified by material in %'
class_chart.add('Stony meteorites', stony)
class_chart.add('Iron meteorites', iron)
class_chart.add('Stony–iron meteorites', istony)
class_chart.add('Unknown-Ungrouped', unknown)
class_chart.render_to_file('../static/img/class.svg')

