import mapnik
m = mapnik.Map(3840,2160)
m.background = mapnik.Color('steelblue')
# MAP 1 DUNIA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#7FFF00')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Reyhan',s)
ds = mapnik.Shapefile(file="countries/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Reyhan')
m.layers.append(layer)
# BATAS AKHIR MAP 1 DUNIA

# MAP 2 France 
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color(' #00008B')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Darkblue'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Reyhan2',s)
ds = mapnik.Shapefile(file="map France/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Reyhan2')
m.layers.append(layer)
# BATAS AKHIR MAP 2 France

# MAP 3 Lesotho
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#8A2BE2')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color(' Blueviolet'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Reyhan2',s)
ds = mapnik.Shapefile(file="map Lesotho/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Reyhan2')
m.layers.append(layer)
# BATAS AKHIR MAP 3 Lesotho

# MAP 4 Romania 
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#7FFFD4')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Aquamarine'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Reyhan2',s)
ds = mapnik.Shapefile(file="map Romania/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Reyhan2')
m.layers.append(layer)
# BATAS AKHIR MAP 4 Romania

# MAP 5 Swaziland 
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FF1493')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Deeppink'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Reyhan2',s)
ds = mapnik.Shapefile(file="map Swaziland/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Reyhan2')
m.layers.append(layer)
# BATAS AKHIR MAP 4 Swaziland

# MAP 6 Turkey 
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FFD700')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Gold'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Reyhan2',s)
ds = mapnik.Shapefile(file="map Turkey/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Reyhan2')
m.layers.append(layer)
# BATAS AKHIR MAP 6 Turkey

 
m.zoom_all()
mapnik.render_to_file(m,'world.jpeg','jpeg')
print "rendered image to 'world.jpeg'"
