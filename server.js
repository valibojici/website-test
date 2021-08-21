let data = fetch('./output.json').
	then((data) => data.json()).
	then((data) => console.log(data));