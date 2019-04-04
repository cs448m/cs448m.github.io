x = [
    9, 18, 21, 21, 17, 
   16, 11, 10, 10, 13, 
   16, 16, 11, 11, 12, 
   12, 11, 10, 10, 11, 
   16, 17, 21, 21, 18,
   9, 6, 6, 5, 4,
   4, 5, 11, 12, 16,
   16, 13, 3, 0, 0,
   3, 6, 6 
   ]

y = [
    0,  0,  3,  5,  5,
    4,  4,  5,  6,  6,
    9, 14, 14, 13, 12,
   11, 10, 10, 15, 16,
   16, 15, 15, 17, 21,
   21, 17, 10, 10, 11,
   23, 24, 24, 23, 23,
   25, 28, 28, 25,  8,
    6, 6, 3 
   ]

path = ''
xys = zip(x,y)
for i, xy in enumerate(xys):
    path += 'M' if i == 0 else 'L'
    path += f' {4*xy[0]},{4*xy[1]} '
path += 'Z'

svg = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   version="1.1"
   id="svg2">
  <g
     id="layer1">
    <path
       d="{path}"
       id="path2991"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
  </g>
</svg>
'''

print(svg)
