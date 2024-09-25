#coding=utf-8
import pandas as pd
from upsetplot import from_indicators, plot,from_contents
from matplotlib import pyplot

def test_intersection_before_contamination():
    path="/home/jiaojguan2/2024GRF_proposal/before_remove_contamination/"

    dvf_virus = set(pd.read_csv(path + 'dvf_virus.csv')["contig"])
    genomad_virus = set(pd.read_csv(path + "genomad_virus.csv")["contig"])
    viralm_virus = set(pd.read_csv(path + "viralm_virus.csv")["contig"])
    vs2_virus = set(pd.read_csv(path + "vs2_virus.csv")["contig"])

    union_virus = genomad_virus | dvf_virus | viralm_virus |vs2_virus
    print("union virus:", len(union_virus))

    contents = {"Virsorter2": vs2_virus,
                "DeepVirFinder": dvf_virus,
                "ViraLM": viralm_virus,
                "geNomad": genomad_virus}

    example = from_contents(contents)
    print(example)

    # plot(example, show_counts="{:,}", sort_by="cardinality")
    # pyplot.savefig("compare_4_identification_virus_before_conmination.jpg")

# test_intersection_before_contamination()