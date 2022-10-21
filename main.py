from easylib import randomgen, graphbuilder
generator = randomgen.Generator(length=10)

graphs = graphbuilder.Graphbuilder(shape="square")
for x in range(0, 120):
    graphs.append(graphbuilder.Graph(graphbuilder.Set(x=generator.List(internalDataFunction=generator.Int), y=generator.List(internalDataFunction=generator.Int))))
graphs.build()
