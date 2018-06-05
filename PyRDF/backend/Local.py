import ROOT

def local_executor(generator):
    """
    Execution of the event-loop
    in local environment

    """
    mapper = generator.get_callable()

    filenames_vec = ROOT.std.vector('string')()
    for f in generator.root_node.filelist:
        filenames_vec.push_back(f)

    TDF = ROOT.ROOT.RDataFrame(generator.root_node.treename, filenames_vec)

    output = mapper(TDF)

    output[0][0].GetValue()

    for val, node in zip(output[0], output[1]):
        node.value = val