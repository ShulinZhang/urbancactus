
$(document).ready(function() {
	L.AwesomeMarkers.Icon.prototype.options.prefix = 'ion';

	var layers = [];
	var layersList = {};

	for (var i = 0; i < python_data['map_types'].length; i++) {
		var map_type = python_data['map_types'][i];
		var markers = [];

		var icon = L.AwesomeMarkers.icon({
			icon: map_type.icon ? map_type.icon : 'record',
			markerColor: map_type.colour ? map_type.colour : 'blue',
		});

		for (var n = 0; n < map_type.markers.length; n++) {
			var marker_data = map_type.markers[n];
			var marker = L.marker([marker_data.latitude, marker_data.longitude], {
				icon: icon,
			});

			if (marker_data.link) {
				marker.bindPopup("<b><a href=\""+marker_data.link+"\">"+marker_data.name+"</a></b><br>"+marker_data.description);
			} else {
				marker.bindPopup("<b>"+marker_data.name+"</b><br>"+marker_data.description);
			}

			markers.push(marker);
		}

		var layer = L.layerGroup(markers);
		layers.push(layer);
		layersList[map_type.name] = layer;
	}

	var map = L.map('map', {
		center: [39.913818, 116.390625],
		zoom: 13,
		layers: layers,
		scrollWheelZoom: (python_data['disableMapScroll'] != true),
	});

	L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);

	if (layers.length > 0) {
		L.control.layers([], layersList).addTo(map);
	}

	if (python_data['disableLocationDetection'] != true) {
		map.locate({setView: true, maxZoom: 16});
	}
});
