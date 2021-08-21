#!/usr/bin/python

import json

with open('test.txt', 'r') as f:
	content = f.read()

	solution = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Expedita exercitationem culpa, corporis delectus quia quas placeat ipsam nobis aut ratione natus modi? Voluptas nobis harum unde modi aspernatur? Accusamus iste ipsam, atque non corporis odit obcaecati, labore molestias repellendus hic rem dolorem velit optio incidunt! Et, numquam libero nemo at placeat officia soluta corrupti aliquam animi ea magni ipsa quam expedita cumque perferendis atque recusandae ullam eum amet! Vel ipsam facere eum minima, officiis sunt doloremque totam mollitia aliquam non inventore saepe eos voluptate ratione. Dolores earum maxime labore nemo nobis dolorem porro deserunt omnis magni mollitia. Adipisci, maxime eum.<pre><code>int x = 5; </code></pre> recusandae ullam eum amet! Vel ipsam facere eum minima, officiis sunt doloremque totam mollitia aliquam non inventore saep"

	jsonData = json.dumps({'content' : content, 'solution' : solution})
	
	with open('output.json', 'w') as g:
		g.write(jsonData)

