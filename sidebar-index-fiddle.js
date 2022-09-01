var paradas = {
    "type" : "FeatureCollection",
    "name" : "paradas",
    "crs": {
        "type": "name",
        "properties": {
          "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    },
    "features" : [
        { 
            "type" : "Feature", 
            "properties" : {  
                "nome" : "Parada 1", 
                "imagem" : "<img src='1.jpg' alt='maptime logo gif' width='350px'/>",
                "descricao" : "Test."
            }, 
            "geometry" : { 
                "type" : "Point", 
                "coordinates" : [
                    -38.55222702026367,
                    -3.7864725817550275
                ] 
            }
        },
      { 
            "type" : "Feature", 
            "properties" : {  
                "nome" : "Parada 2", 
                "imagem" : "<img src='2.jpg' alt='maptime logo gif' width='350px'/>",
                "descricao" : "Test 2."
            }, 
            "geometry" : { 
                "type" : "Point", 
                "coordinates" : [
                    -36.55222702026367,
                    -3.7864725817550275
                ] 
            }
        },
      { 
            "type" : "Feature", 
            "properties" : {  
                "nome" : "Parada 3", 
                "imagem" : "<img src='3.jpg' alt='maptime logo gif' width='350px'/>",
                "descricao" : "Test 3."
            }, 
            "geometry" : { 
                "type" : "Point", 
                "coordinates" : [
                    -34.55222702026367,
                    -3.7864725817550275
                ] 
            }
        }
    ]
};  

var map = L.map("map", {
  center: [-3.7864725817550275, -38.55222702026367],
  zoom: 4
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var rotas = L.geoJSON(paradas, {
  onEachFeature: onEachFeature
}).addTo(map);

function onEachFeature(feature, layer) {
  layer.on('click', function(e) {
    $(".nome").html(feature.properties.nome);
    $(".imagem").html(feature.properties.imagem);
    $(".descricao").html(feature.properties.descricao);
  });
}