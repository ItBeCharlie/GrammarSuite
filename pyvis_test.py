from pyvis.network import Network


net = Network(directed=True)

net.add_node(0)
net.add_node(1)
net.add_node(2)
net.add_edge(0, 1)
net.add_edge(2, 1, label='Test')
net.add_edge(1, 2, label='Test2')
net.add_edge(0, 2)
net.show('basic.html')
