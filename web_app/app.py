from flask import Flask , request
app = Flask(__name__)




@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script>L_PREFER_CANVAS = false; L_NO_TOUCH = false; L_DISABLE_3D = false;</script>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.2.0/dist/leaflet.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.2.0/dist/leaflet.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" />
    <link rel="stylesheet" href="https://rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css" />
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>

            <style> #map_6b77ec2a3e9347f1b628ec94ca68e51c {
                position : relative;
                width : 100.0%;
                height: 100.0%;
                left: 0.0%;
                top: 0.0%;
                }
            </style>

</head>
<body>

            <div class="folium-map" id="map_6b77ec2a3e9347f1b628ec94ca68e51c" ></div>

</body>
<script>



                var bounds = null;


            var map_6b77ec2a3e9347f1b628ec94ca68e51c = L.map(
                                  'map_6b77ec2a3e9347f1b628ec94ca68e51c',
                                  {center: [36,-121],
                                  zoom: 5,
                                  maxBounds: bounds,
                                  layers: [],
                                  worldCopyJump: false,
                                  crs: L.CRS.EPSG3857
                                 });



            var tile_layer_db6f608759334327a50446d6927d0dae = L.tileLayer(
                'https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png',
                {
  "attribution": null,
  "detectRetina": false,
  "maxZoom": 18,
  "minZoom": 1,
  "noWrap": false,
  "subdomains": "abc"
}
                ).addTo(map_6b77ec2a3e9347f1b628ec94ca68e51c);


            var feature_group_ea4dbbd449944bd8a80f090a344995fb = L.featureGroup(
                ).addTo(map_6b77ec2a3e9347f1b628ec94ca68e51c);


            var circle_marker_41ab441e91e34abab5346e71010b32d5 = L.circleMarker(
                [-33.7253287,-69.1415063],
                {
  "bubblingMouseEvents": true,
  "color": "#ecf600",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ecf600",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_53b7c02f2d99452a882f2519c2f5162e = L.circleMarker(
                [-33.0218355,-68.8702373],
                {
  "bubblingMouseEvents": true,
  "color": "#a4d200",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#a4d200",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_aa64d4bfba6a47beaa537077c0c3565f = L.circleMarker(
                [-37.5625941,-64.2967601],
                {
  "bubblingMouseEvents": true,
  "color": "#ffdc00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffdc00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_ca14c6a8148d445dbd807b82020157de = L.circleMarker(
                [-34.6773649,-68.2452744],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd100",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd100",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_bbeb19117e4e4c6aacc286d19ca2d435 = L.circleMarker(
                [-33.4206328,-69.25176540000001],
                {
  "bubblingMouseEvents": true,
  "color": "#d5eb00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#d5eb00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_7ddae2191d814e9998952bd473af48c5 = L.circleMarker(
                [-33.431033500000005,-69.1998273],
                {
  "bubblingMouseEvents": true,
  "color": "#b7db00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#b7db00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_61d72db53a244795a0dc3a998241d5d7 = L.circleMarker(
                [-26.062050199999998,-65.97655060000001],
                {
  "bubblingMouseEvents": true,
  "color": "#ffb700",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffb700",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_6cd167422bf04b06a110503ee68b5f09 = L.circleMarker(
                [-38.9278065,-68.0384792],
                {
  "bubblingMouseEvents": true,
  "color": "#ff7900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff7900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_de7201a4764a46b59b4bec5a0ea055bc = L.circleMarker(
                [-39.052405799999995,-67.3628265],
                {
  "bubblingMouseEvents": true,
  "color": "#ff6600",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff6600",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_62f26f145673411e8802799a08214efc = L.circleMarker(
                [-38.58083060000001,-68.31468120000001],
                {
  "bubblingMouseEvents": true,
  "color": "#ff2100",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff2100",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_e98fdd13faca4913a04ce74a21264454 = L.circleMarker(
                [-39.0361745,-67.33095],
                {
  "bubblingMouseEvents": true,
  "color": "#ff4400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff4400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_dd2fbcbeebd1429dbcb41e1e7fe7dcf4 = L.circleMarker(
                [-33.013555600000004,-68.9113572],
                {
  "bubblingMouseEvents": true,
  "color": "#ff9600",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff9600",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_47b8418e3b804aeb843242ab0bbd0b89 = L.circleMarker(
                [-34.521645299999996,139.1488796],
                {
  "bubblingMouseEvents": true,
  "color": "#c6e300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#c6e300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_9d2b6a1af7d544209e13e42fb88ba2d1 = L.circleMarker(
                [-35.0052222,138.82105],
                {
  "bubblingMouseEvents": true,
  "color": "#a9d400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#a9d400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_c6b5ab768e8a446d941980b57d7af439 = L.circleMarker(
                [-41.067386600000006,147.1801722],
                {
  "bubblingMouseEvents": true,
  "color": "#ffe900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffe900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_ce84c864a8f6431daf941433b92cb6bb = L.circleMarker(
                [-42.764532,147.3865147],
                {
  "bubblingMouseEvents": true,
  "color": "#d9ed00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#d9ed00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_1a065322e9d04945a900ba6d0be8b6c1 = L.circleMarker(
                [-41.1744392,146.917816],
                {
  "bubblingMouseEvents": true,
  "color": "#f6fb00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#f6fb00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_be3f23d4ec154c3694ed0899eb7352cb = L.circleMarker(
                [-32.7752104,151.2991692],
                {
  "bubblingMouseEvents": true,
  "color": "#ffc800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffc800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_ede3ed276a724a5181ddbcb1821c25c6 = L.circleMarker(
                [-38.3227951,145.0985234],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_8b12a0d6a965476d9f51017a28f7169b = L.circleMarker(
                [-38.2718408,145.0976471],
                {
  "bubblingMouseEvents": true,
  "color": "#ffba00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffba00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_2532ef7856e542e09a042bafe018a403 = L.circleMarker(
                [-36.8292345,145.1376477],
                {
  "bubblingMouseEvents": true,
  "color": "#d1e800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#d1e800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_da2f0b70d04a4a79a680334e63d8f681 = L.circleMarker(
                [-37.6439517,145.5203451],
                {
  "bubblingMouseEvents": true,
  "color": "#9bcd00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#9bcd00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_9133b924886e45b184b325c24ba0f8a2 = L.circleMarker(
                [-37.6369601,145.52003069999995],
                {
  "bubblingMouseEvents": true,
  "color": "#399c00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#399c00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_f40001231d4e4ad0a40d039f308e7c61 = L.circleMarker(
                [-37.598685700000004,145.4113812],
                {
  "bubblingMouseEvents": true,
  "color": "#95ca00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#95ca00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_dc164dcd644f4c429074cf0149ab95ba = L.circleMarker(
                [-37.764239,145.2438813],
                {
  "bubblingMouseEvents": true,
  "color": "#fff300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fff300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_66725625deae4ce9ae78a85c2a3f0bea = L.circleMarker(
                [-37.6770622,145.3832385],
                {
  "bubblingMouseEvents": true,
  "color": "#edf700",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#edf700",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_b259db733bdd40afb163b92e3d1fc051 = L.circleMarker(
                [-32.538606300000005,149.6021054],
                {
  "bubblingMouseEvents": true,
  "color": "#ffc900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffc900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_1118f6f067d54350a18ce06e7126a957 = L.circleMarker(
                [47.9638861,16.7816906],
                {
  "bubblingMouseEvents": true,
  "color": "#c6e300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#c6e300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_7b12e7a405a1484ca9684c11c35628bd = L.circleMarker(
                [46.8336405,12.7884239],
                {
  "bubblingMouseEvents": true,
  "color": "#fff000",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fff000",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_c36b26a24a554c4685ae5038cdddefbc = L.circleMarker(
                [47.938628,16.7224042],
                {
  "bubblingMouseEvents": true,
  "color": "#deef00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#deef00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_5c1707a9093743e5a33525c36bf38735 = L.circleMarker(
                [49.8381315,-119.58249270000002],
                {
  "bubblingMouseEvents": true,
  "color": "#eaf500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#eaf500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_173f0d2a435a440b90396fabdf3b39a4 = L.circleMarker(
                [49.1021025,-119.53572790000001],
                {
  "bubblingMouseEvents": true,
  "color": "#aad500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#aad500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_f4205bba727b4beca2674584543e5044 = L.circleMarker(
                [43.147219899999996,-79.3654078],
                {
  "bubblingMouseEvents": true,
  "color": "#ffe400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffe400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_03dcc5e6a1c2473d9c07d1e39096bebf = L.circleMarker(
                [43.2499743,-79.1457448],
                {
  "bubblingMouseEvents": true,
  "color": "#e4f200",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#e4f200",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_dd227145ee9547e9829777fff4f54958 = L.circleMarker(
                [43.2170164,-79.06599969999998],
                {
  "bubblingMouseEvents": true,
  "color": "#f1f800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#f1f800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_19fbfdb697d640dd9f68f50d6d94564e = L.circleMarker(
                [43.163909999999994,-79.1135821],
                {
  "bubblingMouseEvents": true,
  "color": "#dcee00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#dcee00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_0c0fca9baa32463c9b99886d0a765063 = L.circleMarker(
                [-34.6160512,-71.2760551],
                {
  "bubblingMouseEvents": true,
  "color": "#e6f300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#e6f300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_d81be83e1bbe46beba1a6d6973dc8758 = L.circleMarker(
                [-32.8017211,-70.82589759999998],
                {
  "bubblingMouseEvents": true,
  "color": "#4fa800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#4fa800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_70238fd3a6b044959101e39a0358f398 = L.circleMarker(
                [-31.744600800000004,-70.95791329999999],
                {
  "bubblingMouseEvents": true,
  "color": "#ff9300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff9300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_e03b5d1910e84ebaa8ac1ba42af9475c = L.circleMarker(
                [-34.4902907,-70.90312349999998],
                {
  "bubblingMouseEvents": true,
  "color": "#cce600",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#cce600",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_c04ccffc9ba64ea7a1e75e38aac0d3d5 = L.circleMarker(
                [-37.5906439,-72.5208123],
                {
  "bubblingMouseEvents": true,
  "color": "#ffe300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffe300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_0a8496cb47844fe6a0ecc73b9d389ee5 = L.circleMarker(
                [-34.3340462,-70.76192409999999],
                {
  "bubblingMouseEvents": true,
  "color": "#ffe400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffe400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_a55ee8b8910b478394fcece83b0f6179 = L.circleMarker(
                [-33.3170397,-71.459914],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd700",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd700",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_d070ede80edc47c08a63d087db0096a4 = L.circleMarker(
                [-33.3565297,-71.3293519],
                {
  "bubblingMouseEvents": true,
  "color": "#f4fa00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#f4fa00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_f4e7e8334ed5400da8092c9ab98b5c90 = L.circleMarker(
                [-33.2896477,-71.3883551],
                {
  "bubblingMouseEvents": true,
  "color": "#f3f900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#f3f900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_84f52073877e420b9202355e42a4edff = L.circleMarker(
                [-33.3580699,-71.346525],
                {
  "bubblingMouseEvents": true,
  "color": "#c9e400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#c9e400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_0db4252ee33940049930a61fa15eaf23 = L.circleMarker(
                [-33.477621299999996,-71.478612],
                {
  "bubblingMouseEvents": true,
  "color": "#e4f200",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#e4f200",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_b636265b59524848b766ba07c207a016 = L.circleMarker(
                [-33.3188308,-71.42793780000002],
                {
  "bubblingMouseEvents": true,
  "color": "#ffcb00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffcb00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_f45e2a45be6549f1af2fe7d288cccb2b = L.circleMarker(
                [-33.6444803,-70.888209],
                {
  "bubblingMouseEvents": true,
  "color": "#c6e300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#c6e300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_1e3b46d221ee406288997ea8c7783135 = L.circleMarker(
                [-33.3696742,-71.292361],
                {
  "bubblingMouseEvents": true,
  "color": "#c6e300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#c6e300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_655c72132bb446278d76ad1ea7070c8c = L.circleMarker(
                [-34.5357527,-70.9814385],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd000",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd000",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_5372178675e64203a449e66479830ab5 = L.circleMarker(
                [-33.611748299999995,-71.4412717],
                {
  "bubblingMouseEvents": true,
  "color": "#eff700",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#eff700",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_533fa654051b4c53860308de18f577bb = L.circleMarker(
                [-34.56492539999999,-71.3831453],
                {
  "bubblingMouseEvents": true,
  "color": "#ffe600",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffe600",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_63c1c13033304ebabcd8039b97669982 = L.circleMarker(
                [-30.678539,-71.3801],
                {
  "bubblingMouseEvents": true,
  "color": "#ff7100",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff7100",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_4160f16ce078450a80a6636851630cce = L.circleMarker(
                [-34.7278279,-71.5934859],
                {
  "bubblingMouseEvents": true,
  "color": "#ffe500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffe500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_d6fa44b76f384b00ad3badd8ab1053c9 = L.circleMarker(
                [-33.7543928,-71.2311328],
                {
  "bubblingMouseEvents": true,
  "color": "#9bce00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#9bce00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_f69798d4a76d4febb725d7e6ec79cb86 = L.circleMarker(
                [-33.490563800000004,-70.54901009999998],
                {
  "bubblingMouseEvents": true,
  "color": "#fff900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fff900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_151669c75cb740308a2688a746afe6b2 = L.circleMarker(
                [-34.6235185,-71.2641673],
                {
  "bubblingMouseEvents": true,
  "color": "#d1e800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#d1e800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_44772c2c65ea425c99de9be913b888d2 = L.circleMarker(
                [50.9953406,-0.21300370000000002],
                {
  "bubblingMouseEvents": true,
  "color": "#ffe300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffe300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_8f152554471f43ceba7d925e54537915 = L.circleMarker(
                [50.4757933,-4.7831748],
                {
  "bubblingMouseEvents": true,
  "color": "#fff200",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fff200",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_eab3c6b4e9054e9c8cea3d50113917d8 = L.circleMarker(
                [46.164762700000004,4.6864105],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd200",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd200",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_fafeb5d49798447996483a57c768d170 = L.circleMarker(
                [47.9773864,7.2927564],
                {
  "bubblingMouseEvents": true,
  "color": "#71b800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#71b800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_48395617db434d3683afa53e37633de1 = L.circleMarker(
                [48.3975809,7.4401717000000005],
                {
  "bubblingMouseEvents": true,
  "color": "#fff900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fff900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_69ed89d511c84798a185a8093b1f742f = L.circleMarker(
                [48.5963833,7.5003955],
                {
  "bubblingMouseEvents": true,
  "color": "#ff5a00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff5a00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_852f9d24c84340329b3a855315175aa8 = L.circleMarker(
                [48.161060299999995,7.2960553],
                {
  "bubblingMouseEvents": true,
  "color": "#ddee00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ddee00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_71cd0be6080545789ead28dbd0e0c6f3 = L.circleMarker(
                [48.327799299999995,7.427023700000001],
                {
  "bubblingMouseEvents": true,
  "color": "#fdfe00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fdfe00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_a1f94438d6674fdfbdffa7140cf7ce55 = L.circleMarker(
                [48.0394023,7.3078201],
                {
  "bubblingMouseEvents": true,
  "color": "#ff9d00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff9d00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_a08daae6d6eb42819ccef9f3d52a331b = L.circleMarker(
                [48.318472899999996,7.4294268],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_da95dd37c8954037af9536e00f4df041 = L.circleMarker(
                [48.1399872,7.322439299999999],
                {
  "bubblingMouseEvents": true,
  "color": "#ff9b00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff9b00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_02d2f4f0a7ca4eb4935e3aa1e6649612 = L.circleMarker(
                [48.322678499999995,7.4523844],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd000",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd000",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_dfbab721d9704387ac40bb8894ebb9e9 = L.circleMarker(
                [48.3663094,7.448960799999999],
                {
  "bubblingMouseEvents": true,
  "color": "#fbfd00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fbfd00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_0a5d522f89164a11b4d35f8e5da27b43 = L.circleMarker(
                [48.1295775,7.283917999999999],
                {
  "bubblingMouseEvents": true,
  "color": "#ff5100",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff5100",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_282e9370b36d4bb194f7e8db80e859b5 = L.circleMarker(
                [47.9141037,7.2111550000000015],
                {
  "bubblingMouseEvents": true,
  "color": "#73ba00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#73ba00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_6e5ecbfa6a2e45a497951affd5db091c = L.circleMarker(
                [48.2209388,7.3647079],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd200",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd200",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_df1de5c730b3446890a73bf52648f4a8 = L.circleMarker(
                [48.1962867,7.3255449000000015],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_b67fcf88cfc040c880c3002065b2dbaf = L.circleMarker(
                [48.0613521,7.2986284],
                {
  "bubblingMouseEvents": true,
  "color": "#e2f100",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#e2f100",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_3d89fe2e9dba4a21bee149c59bbbb64a = L.circleMarker(
                [48.059146999999996,7.3081712],
                {
  "bubblingMouseEvents": true,
  "color": "#ff5e00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff5e00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_eedc8aeebcd44c2f81158c26b1305b4c = L.circleMarker(
                [48.038403100000004,7.3082677],
                {
  "bubblingMouseEvents": true,
  "color": "#ff8800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff8800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_86e318f6d0834eacb66ac4b82c36976e = L.circleMarker(
                [48.0939349,7.2805644],
                {
  "bubblingMouseEvents": true,
  "color": "#ff5d00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff5d00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_db219242662543d0af30f8843f9c01f3 = L.circleMarker(
                [48.034155299999995,7.2840675999999975],
                {
  "bubblingMouseEvents": true,
  "color": "#ff9300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff9300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_e96c762499384994aba0ad19cfefa6d6 = L.circleMarker(
                [48.1099501,7.281572200000001],
                {
  "bubblingMouseEvents": true,
  "color": "#ff6300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff6300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_58f675c0ddac45dfb77c3e7395298dd3 = L.circleMarker(
                [48.1815611,7.306267299999999],
                {
  "bubblingMouseEvents": true,
  "color": "#ddee00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ddee00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_1ea21c90952448b1a32670011318b137 = L.circleMarker(
                [48.5835391,7.5096982999999975],
                {
  "bubblingMouseEvents": true,
  "color": "#ffcb00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffcb00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_f45f3356c4224db5b1d9e5c9d86e812f = L.circleMarker(
                [48.34419329999999,7.4179682],
                {
  "bubblingMouseEvents": true,
  "color": "#ffd500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffd500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_117b7f4490644d3c87db2704e4ec5491 = L.circleMarker(
                [48.2445829,7.3791531],
                {
  "bubblingMouseEvents": true,
  "color": "#fff600",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fff600",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_b46568358ecf42e18f8103300d5216f1 = L.circleMarker(
                [48.550304499999996,7.4906421000000005],
                {
  "bubblingMouseEvents": true,
  "color": "#ffcf00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffcf00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_78af69be07e143b18ecea11556355e8b = L.circleMarker(
                [48.1053285,7.280700500000001],
                {
  "bubblingMouseEvents": true,
  "color": "#ff6000",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff6000",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_a028988fc15740cd8e5d4d621ce340af = L.circleMarker(
                [48.023444,7.2859505],
                {
  "bubblingMouseEvents": true,
  "color": "#bcde00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#bcde00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_f208722bb43943f39985d7cbb9691d48 = L.circleMarker(
                [47.0476898,4.8462926],
                {
  "bubblingMouseEvents": true,
  "color": "#c9e400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#c9e400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_a01cd4cd53424679b5d8bd5749f13216 = L.circleMarker(
                [46.9165935,4.6931733],
                {
  "bubblingMouseEvents": true,
  "color": "#fdfe00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fdfe00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_7c4b8c3db823401e87e801cf47cec94c = L.circleMarker(
                [46.9134209,4.7032145],
                {
  "bubblingMouseEvents": true,
  "color": "#d3e900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#d3e900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_0795182e711246e0b679ca51e831ca9c = L.circleMarker(
                [46.973192600000004,4.7952103],
                {
  "bubblingMouseEvents": true,
  "color": "#d7eb00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#d7eb00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_65bb878ebc21495d9e11d512e493a700 = L.circleMarker(
                [47.007510499999995,4.8002475],
                {
  "bubblingMouseEvents": true,
  "color": "#a8d400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#a8d400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_4dd3c77e5ac04e74aaf20437b94df3a9 = L.circleMarker(
                [47.1345237,4.9439704],
                {
  "bubblingMouseEvents": true,
  "color": "#dcee00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#dcee00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_32375312cd8e4fac9abfffd206898273 = L.circleMarker(
                [47.1326102,4.944554599999999],
                {
  "bubblingMouseEvents": true,
  "color": "#bbdd00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#bbdd00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_63a26861a82b490bb58825dae3387aa6 = L.circleMarker(
                [46.8385016,4.7150574],
                {
  "bubblingMouseEvents": true,
  "color": "#ffc500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffc500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_c43ad31508a44b3293837b7a436aac1f = L.circleMarker(
                [47.0503684,4.8693258],
                {
  "bubblingMouseEvents": true,
  "color": "#d6eb00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#d6eb00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_7c0720c8f76b47459d0f617765cb5042 = L.circleMarker(
                [47.027508600000004,4.823969],
                {
  "bubblingMouseEvents": true,
  "color": "#6ab500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#6ab500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_6ba4d93d20074d1185ce9d50aaaa4a8f = L.circleMarker(
                [39.022872,-123.36028999999999],
                {
  "bubblingMouseEvents": true,
  "color": "#eff700",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#eff700",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_3ad24d62e0174a3c9cddacf3e9be54d6 = L.circleMarker(
                [39.033753999999995,-123.346528],
                {
  "bubblingMouseEvents": true,
  "color": "#ffe800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ffe800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_e7f5b945ae8845fd89aa385d97f18938 = L.circleMarker(
                [39.017115000000004,-123.362051],
                {
  "bubblingMouseEvents": true,
  "color": "#daed00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#daed00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_312598778de24e8ea117c0ec64006eef = L.circleMarker(
                [39.114574,-123.513549],
                {
  "bubblingMouseEvents": true,
  "color": "#daed00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#daed00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_ea328caa06804346bc8e53f582334096 = L.circleMarker(
                [39.078613,-123.46444699999999],
                {
  "bubblingMouseEvents": true,
  "color": "#c0e000",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#c0e000",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_f171a0856eca4ad99b5d5d004b0d8f7e = L.circleMarker(
                [37.035276,-121.80353999999998],
                {
  "bubblingMouseEvents": true,
  "color": "#ff8f00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff8f00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_b19f7384351740cc8446889ee493cc45 = L.circleMarker(
                [39.148876,-123.547599],
                {
  "bubblingMouseEvents": true,
  "color": "#cde700",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#cde700",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_61df3cf4223e4097acb39fa81cb2ae6d = L.circleMarker(
                [39.047852,-123.439176],
                {
  "bubblingMouseEvents": true,
  "color": "#fff800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fff800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_fc4bdabbf7ad4727bb62c50ad9d6e305 = L.circleMarker(
                [39.027899,-123.388884],
                {
  "bubblingMouseEvents": true,
  "color": "#fff700",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fff700",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_01e58cab9e13404bac483781fef3aadf = L.circleMarker(
                [36.478214,-121.23823],
                {
  "bubblingMouseEvents": true,
  "color": "#a6d300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#a6d300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_7de03873ed6a46e59a62621389b5ea57 = L.circleMarker(
                [36.45616500000001,-121.232087],
                {
  "bubblingMouseEvents": true,
  "color": "#fffa00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#fffa00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_3e7204f9547a47c980c6e3908bac3eb1 = L.circleMarker(
                [36.391725,-121.37136299999999],
                {
  "bubblingMouseEvents": true,
  "color": "#90c800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#90c800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_23e81861d1184d5fad1d2d74944c4a04 = L.circleMarker(
                [37.182108,-122.159026],
                {
  "bubblingMouseEvents": true,
  "color": "#98cc00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#98cc00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_5f47a80850a849bfa819e494717fa586 = L.circleMarker(
                [37.267552,37.267552],
                {
  "bubblingMouseEvents": true,
  "color": "#8ac500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#8ac500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_489e93098ea04f9ca93a054812e2a82e = L.circleMarker(
                [37.108937,-121.890234],
                {
  "bubblingMouseEvents": true,
  "color": "#ff9900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#ff9900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_17def60097594538ba4164e10b204bdc = L.circleMarker(
                [36.99511500000001,-121.770508],
                {
  "bubblingMouseEvents": true,
  "color": "#f3f900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#f3f900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_7209d5b6de5240d2b7b38dd789d2363d = L.circleMarker(
                [36.393772,-121.38298300000001],
                {
  "bubblingMouseEvents": true,
  "color": "#8bc500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#8bc500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_e3a01830ddf747b4bc46c82d23c78582 = L.circleMarker(
                [36.383771,-121.360881],
                {
  "bubblingMouseEvents": true,
  "color": "#88c400",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#88c400",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_af8fe515431b414484e7409ef1961223 = L.circleMarker(
                [36.482796,-121.497309],
                {
  "bubblingMouseEvents": true,
  "color": "#a5d200",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#a5d200",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_c859324d81c343a597a041932c1261f0 = L.circleMarker(
                [36.472029,-121.482525],
                {
  "bubblingMouseEvents": true,
  "color": "#99cd00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#99cd00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_bb9ec9479b2c46b1b1229aaf8982f234 = L.circleMarker(
                [36.467042,-121.46628100000001],
                {
  "bubblingMouseEvents": true,
  "color": "#b2d900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#b2d900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_c8c48ea6900f4827851aacc2c7aaf315 = L.circleMarker(
                [36.441809,-121.46278400000001],
                {
  "bubblingMouseEvents": true,
  "color": "#bdde00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#bdde00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_87305266e87047cab2e992e00f934916 = L.circleMarker(
                [36.443034999999995,-121.43971699999999],
                {
  "bubblingMouseEvents": true,
  "color": "#a5d300",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#a5d300",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_4e62a5389c7b40aea7997f0f071f8a3b = L.circleMarker(
                [36.362173999999996,-121.34482],
                {
  "bubblingMouseEvents": true,
  "color": "#89c500",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#89c500",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_a44278aee4294770ab9fa24376548b1f = L.circleMarker(
                [36.453724,-121.44343400000001],
                {
  "bubblingMouseEvents": true,
  "color": "#73ba00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#73ba00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_bb8efcb1497646e5bc37e8b6b7d932ca = L.circleMarker(
                [36.455531,-121.452999],
                {
  "bubblingMouseEvents": true,
  "color": "#93c900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#93c900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_57a061f252b447d18a772025c2d5c646 = L.circleMarker(
                [36.402771,-121.41283],
                {
  "bubblingMouseEvents": true,
  "color": "#7bbd00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#7bbd00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_4479680043fb487089262975f529a73b = L.circleMarker(
                [36.341108,-121.364787],
                {
  "bubblingMouseEvents": true,
  "color": "#75bb00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#75bb00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_1501899b9e114a2a806a7599eeedfd13 = L.circleMarker(
                [36.457326,-121.457226],
                {
  "bubblingMouseEvents": true,
  "color": "#d6eb00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#d6eb00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_d29727cf05ee4388810c112d2c364d1f = L.circleMarker(
                [36.374571,-121.36705],
                {
  "bubblingMouseEvents": true,
  "color": "#3c9e00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#3c9e00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_c5e5053eb255436e9a30ed3b3d1fe7b3 = L.circleMarker(
                [36.486902,-121.50333899999998],
                {
  "bubblingMouseEvents": true,
  "color": "#b0d800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#b0d800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_4aa6877c71a841efa5bedb8ae09ab3a6 = L.circleMarker(
                [36.441119,-121.44108999999999],
                {
  "bubblingMouseEvents": true,
  "color": "#90c800",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#90c800",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_bc5d51c104414fcdad0fdbe5757bbc53 = L.circleMarker(
                [36.439721,-121.431541],
                {
  "bubblingMouseEvents": true,
  "color": "#b2d900",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#b2d900",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);


            var circle_marker_dff8ea34a5a648bcb766a3bb8fef8354 = L.circleMarker(
                [45.279849,-123.05049199999999],
                {
  "bubblingMouseEvents": true,
  "color": "#369b00",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "#369b00",
  "fillOpacity": 0.6,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5,
  "stroke": true,
  "weight": 3
}
                ).addTo(feature_group_ea4dbbd449944bd8a80f090a344995fb);

</script>
    '''






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
